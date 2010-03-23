/**
 * @file derived.cpp
 * @brief Utility functions to extend the functionality of the CCMC
 * access and interpolation library.
 *
 * The purpose of this library is to provide easy access to derived variables that
 * can be calculated from the base variables provided by the native cdf files. This
 * includes interpolating derived variables, and units of derived variables.
 *
 * @author David Berrios
 **/
#include "Kameleon.h"
#include "FileReader.h"
#include "Kameleon_compatibility.h"
#include "KameleonInterpolator.h"
#include <boost/lexical_cast.hpp>
#include <boost/foreach.hpp>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <math.h>
#include <iostream>

//#define DEBUG_DERIVED
//#define DEPRECATED_WARNING
using namespace std;


//const Derived * derived = new Derived();

//Kameleon derived;
namespace ccmc
{
	extern "C" int cxform(const char *from,const char *to,const double et,double * v_in,double * v_out);
	extern "C" double gregorian_calendar_to_jd(int y, int m, int d, int h, int mi, int s);
	extern "C" long date2es(int yyyy, int mm, int dd, int hh, int mm2, int ss);
	extern "C" long cxRound(double doub);
	const float Kameleon::defaultMissingValue = 1.0995116278e12;

	/**
	 * Default constructor
	 */
	Kameleon::Kameleon()
	{

		model = NULL;
		modelName = "NA";

		missingValue = defaultMissingValue;
		//	cout << "Derived object created" << endl;


	}

	/**
	 * Destructor
	 */
	Kameleon::~Kameleon()
	{

		if (model != NULL)
		{
			model->close();
			delete model;
		}


	}

	/**
	 * @return
	 */
	float Kameleon::getMissingValue()
	{
		return missingValue;
	}

	/**
	 * @return
	 */
	void Kameleon::setMissingValue(float missingValue)
	{
		this->missingValue = missingValue;
	}

	/**
	 * Clears all maps used in this class.
	 */
	void Kameleon::clearMaps()
	{

		variableNativeUnits.clear();
		variableSIUnits.clear();
		variableVisUnits.clear();
		listOfRequiredVariablesForComponents.clear();
		listOfRequiredVariablesForVectors.clear();
		conversionFactorsToSI.clear();
		//conversionFactorsToVis.clear();

		variableAliases.clear();

		//variableData.clear(); //stores the original variable data, if loaded into memory.
		listOfRequiredVariablesForComponents.clear();
		listOfRequiredVariablesForVectors.clear();
		listOfRequiredVariablesForComponentsByID.clear();
		listOfRequiredVariablesForVectorsByID.clear();

	}

	/**
	 * Initializes the extra information required by this library.  Usually this is called whenever
	 * the open methods are called.
	 */
	void Kameleon::initializeExtraInformation()
	{

		//modelName = getGlobalAttributeString("model_name");
		clearMaps();
		initializeUnits();
		initializeListOfRequiredVariablesForComponentsAndVectors();
		//	initializeCalculationMethods();
		//	initializeConversionFactorsToSI();
		//	initializeConversionFactorsToVis();
		initializeVariableAliases();
		initializeConversionFactorsToSI();
		//initializeConversionFactorsToVis();
	}

	/**
	 * Returns the units of the variable specified.  The units may differ from the units in the original data.
	 * @param variable
	 * @return String representation of the units
	 */
	std::string Kameleon::getNativeUnit(const std::string& variable)
	{
		std::string units;
		std::string variable_str = variable;
		boost::unordered_map<std::string, std::string>::iterator iter = variableAliases.find(variable_str);
		if (iter != variableAliases.end())
			variable_str = variableAliases[variable_str];
		cout << "variable_str: " << variable_str << endl;

		//units were never fetched before
		//first, attempt fetch from Kameleon's map for derived variables.
		//then fall through to model specific variable units
		iter = variableNativeUnits.find(variable_str);
		if (iter == variableNativeUnits.end())
		{
			units = (model->getVariableAttribute(variable_str, "units")).getAttributeString();
			//variableUnits[variable] = units;
		} else
		{
			//cout << "found in variableUnits" << endl;
			units = "";
		}
		return units;
	}

	/**
	 * @param variable
	 * @return
	 */
	std::string Kameleon::getSIUnit(const std::string& variable)
	{
		std::string units;
		std::string variable_str = variable;
		boost::unordered_map<std::string, std::string>::iterator iter = variableAliases.find(variable_str);
		if (iter != variableAliases.end())
			variable_str = variableAliases[variable_str];
		cout << "variable_str: " << variable_str << endl;

		//units were never fetched before
		//first, attempt fetch from Kameleon's map for derived variables.
		//then fall through to model specific variable units
		iter = variableSIUnits.find(variable_str);
		if (iter != variableSIUnits.end())
		{
			units = (*iter).second;
		} else
		{
			units = model->getSIUnit(variable);
			//variableUnits[variable] = units;
		}
		return units;
	}

	/**
	 * @param variable
	 * @return
	 */
	std::string Kameleon::getVisUnit(const std::string& variable)
	{
		std::string units;
		std::string variable_str = variable;
		boost::unordered_map<std::string, std::string>::iterator iter = variableAliases.find(variable_str);
		if (iter != variableAliases.end())
			variable_str = variableAliases[variable_str];
		cout << "variable_str: " << variable_str << endl;

		//units were never fetched before
		//first, attempt fetch from Kameleon's map for derived variables.
		//then fall through to model specific variable units
		iter = variableVisUnits.find(variable_str);
		if (iter != variableVisUnits.end())
		{
			units = (*iter).second;
			//variableUnits[variable] = units;
		} else
		{
			units = model->getNativeUnit(variable_str);
		}
		return units;
	}

	/**
	 * Calculates the current time based on the start time and the elapsed time.
	 * @return Formatted string of the current time.  This is currently different for
	 * different models.  If the current time cannot be calculated, "TIME_UNAVAILABLE"
	 * is returned.
	 */
	Time Kameleon::getCurrentTime()
	{
		//selectCDF(current_cdf_id);
		std::string time_string;
		//string model_name = gattribute_char_get("model_name");
		Time time;
		std::string start_time_char = "";
		if (modelName != "enlil")
			start_time_char = (model->getGlobalAttribute("start_time")).getAttributeString();

		if (start_time_char == "")
		{
			time_string = "TIME UNAVAILABLE";
			if (modelName == "enlil")
			{
				// from some example in http://www.csgnetwork.com/julianmodifdateconv.html
				float mjd = (model->getGlobalAttribute("time_refdate_mjd")).getAttributeFloat();
				float time_physical_time = (model->getGlobalAttribute("time_physical_time")).getAttributeFloat();
				time_physical_time = time_physical_time / 60.0 / 60.0 / 24.0;
				mjd = mjd + time_physical_time;
				double J_d = mjd + 2400001.0;
				double J = (int) J_d;
				int l = (int) J + 68569;
				int n = (int) (4 * l / 146097);
				l = (int) (l - (146097 * n + 3) / 4);
				int year = (int) (4000 * (l + 1) / 1461001);
				l = (int) (l - 1461 * year / 4 + 31);
				int month = (int) (80 * l / 2447);
				int D = l - 2447 * month / 80;
				l = (int) (month / 11);
				int Y = 100 * (n - 49) + year + l;
				int M = month + 2 - 12 * l;
				///MessageBox.Show(D + "/" + M + "/" + Y);
				float remainder = J_d - J;
				if (remainder > 1.0)
				{
					D = D + 1;
					remainder = remainder - 1.0;

				}
				float hours = remainder * 24.0;
				float hours_int = (int) hours;
				float minutes = (hours - hours_int) * 60.0;
				float minutes_int = (int) minutes;
				float seconds = (minutes - minutes_int) * 60.0;
				//double seconds_int = (int)(seconds + .5);
				float seconds_int = (int) (seconds);

				time.year = Y;
				time.month = M;
				time.day = D;
				time.hour = hours;
				time.minute = minutes;
				time.second = seconds;


				string time_string_month = boost::lexical_cast<std::string>(M);
				string time_string_day = boost::lexical_cast<std::string>(D);
				string time_string_year = boost::lexical_cast<std::string>(Y);
				string time_string_hours = boost::lexical_cast<std::string>((int) hours);
				string time_string_minutes = boost::lexical_cast<std::string>((int) minutes);
				string time_string_seconds = boost::lexical_cast<std::string>((int) seconds_int);

				time_string = padString(time_string_year, 4) + "/" + padString(time_string_month, 2) + "/" + padString(
						time_string_day, 2) + " " + padString(time_string_hours, 2) + ":" + padString(
						time_string_minutes, 2) + ":" + padString(time_string_seconds, 2);
			}

		} else
		{
			string start_time = start_time_char;
			float elapsed_time = (model->getGlobalAttribute("elapsed_time_in_seconds")).getAttributeFloat();

			char buffer[50];
			char current_time[25];
			double cdf_epoch_time = parseEPOCH3((char *) start_time.c_str());
			encodeEPOCH3(cdf_epoch_time, buffer);
			//float temp = elapsed_time * 1000.0;
			cdf_epoch_time = (elapsed_time * 1000.0) + cdf_epoch_time;
			encodeEPOCH3(cdf_epoch_time, current_time);
			//parse the new string
			//"2007-05-20T20:30:00.000Z";
			cout << "current_time: " << current_time << endl;
			string current_time_str = current_time;
			time.year = boost::lexical_cast<int>(current_time_str.substr(0,4));
			cout << "time.year: " << time.year << endl;
			time.month = boost::lexical_cast<int>(current_time_str.substr(5,2));
			cout << "time.month: " << time.month << endl;
			time.day = boost::lexical_cast<int>(current_time_str.substr(8,2));
			cout << "time.day: " << time.day << endl;
			time.hour = boost::lexical_cast<int>(current_time_str.substr(11,2));
			cout << "time.hour: " << time.hour << endl;
			time.minute = boost::lexical_cast<int>(current_time_str.substr(14,2));
			cout << "time.minute: " << time.minute << endl;
			time.second = boost::lexical_cast<float>(current_time_str.substr(17,6));
			cout << "time.second: " << time.second << endl;
			time_string = current_time;
		}
		return time;
	}

	/**
	 * @param s
	 * @param minLength
	 * @return
	 */
	string Kameleon::padString(const string& s, int minLength)
	{
		string output = s;
		while ((int) (output.length()) < minLength)
		{
			output = "0" + output;
		}
		return output;
	}

	/**
	 * Helper function to create an apporpriate vector containing the list of required variables.
	 * This is used in conjunction with openWithMultipleVariables
	 * @return a vector<string> containing the variable names
	 */
	vector<string> Kameleon::createVectorOfStringFromList(int num, ...)
	{
		vector<string> neededVariables;
		va_list list_of_variables;
		va_start(list_of_variables, num);
		for (int i = 0; i < num; i++)
		{
			neededVariables.push_back(va_arg(list_of_variables, char *));
		}
		return neededVariables;
	}

	/**
	 * Helper function to create an apporpriate vector containing the list of required variables.
	 * This is used in conjunction with openWithMultipleVariables
	 * @return a vector<long> containing the variable names
	 */
	vector<long> Kameleon::createVectorOfLongFromList(int num, ...)
	{
		vector<long> neededVariables;
		va_list list_of_variables;
		va_start(list_of_variables, num);
		for (int i = 0; i < num; i++)
		{
			neededVariables.push_back(this->getVariableID(va_arg(list_of_variables, char *)));
		}
		return neededVariables;
	}


	/**
	 * Closes the currently opened file.
	 */
	long Kameleon::close()
	{
		model->close();
		delete model;
		model = NULL;


	}

	/**
	 * Returns a new interpolater that maintains state information independent of other interpolators. This can be used to
	 * parallelize the interpolations.
	 * @return A new interpolator.
	 */
	Interpolator * Kameleon::createNewInterpolator()
	{
		return new KameleonInterpolator(model);
	}

	std::vector<std::string> Kameleon::getLoadedVariables()
	{
		return model->getLoadedVariables();
	}

	/**
	 * @param variable
	 * @return
	 */
	bool Kameleon::loadVariable(const std::string& variable)
	{

		std::vector<std::string> requiredVariables = this->getListOfRequiredVariablesForComponents(variable);
		bool success = true;
		for (int i = 0; i < requiredVariables.size(); i++)
		{
			std::cout << "loading " << requiredVariables[i] << std::endl;
			if (!model->loadVariable(requiredVariables[i]))
				success = false;
		}
		return success;
	}

	bool Kameleon::unloadVariable(const std::string& variable)
	{
		std::vector<std::string> requiredVariables = this->getListOfRequiredVariablesForComponents(variable);
		bool success = true;
		for (int i = 0; i < requiredVariables.size(); i++)
		{
			std::cout << "unloading " << requiredVariables[i] << std::endl;
			if (!model->unloadVariable(requiredVariables[i]))
				success = false;
		}
		return success;
	}
	/**
	 * @param variable
	 * @return
	 */
	bool Kameleon::loadVectorVariable(const std::string& variable)
	{

		std::vector<std::string> requiredVariables = this->getListOfRequiredVariablesForVectors(variable);
		bool success = true;
		for (int i = 0; i < requiredVariables.size(); i++)
		{
			std::cout << "loading " << requiredVariables[i] << std::endl;
			if (!model->loadVariable(requiredVariables[i]))
				success = false;
		}
		return success;
	}

	bool Kameleon::unloadVectorVariable(const std::string& variable)
	{
		std::vector<std::string> requiredVariables = this->getListOfRequiredVariablesForVectors(variable);
		bool success = true;
		for (int i = 0; i < requiredVariables.size(); i++)
		{
			std::cout << "unloading " << requiredVariables[i] << std::endl;
			if (!model->unloadVariable(requiredVariables[i]))
				success = false;
		}
		return success;
	}

	/**
	 * @param varaible
	 * @return
	 */
	std::vector<std::string> Kameleon::getListOfRequiredVariablesForComponents(std::string variable)
	{
		boost::unordered_map<std::string, std::vector<std::string> >::iterator iter =
				this->listOfRequiredVariablesForComponents.find(variable);
		if (iter != listOfRequiredVariablesForComponents.end())
		{
			return (*iter).second;
		} else
		{
			if (model->doesVariableExist(variable))
			{
				std::vector<std::string> required;
				required.push_back(variable);
				return required;
			} else
			{
				std::vector<std::string> required;
				return required;
			}
		}
	}

	/**
	 * Returns a vector of strings of all the variables required to calculate the requested variable. For base variables,
	 * this will simply be an vector with one variable. Derived variables can have multiple variables.
	 * @param variable
	 * @return
	 */
	std::vector<std::string> Kameleon::getListOfRequiredVariablesForVectors(std::string variable)
	{
		boost::unordered_map<std::string, std::vector<std::string> >::iterator iter =
				this->listOfRequiredVariablesForVectors.find(variable);
		if (iter != listOfRequiredVariablesForVectors.end())
		{
			return (*iter).second;
		} else
		{
			if (model->doesVariableExist(variable))
			{
				std::vector<std::string> required;
				required.push_back(variable);
				return required;
			} else
			{
				std::vector<std::string> required;
				return required;
			}
		}
	}

	/**
	 * Currently not implemented.
	 * @param variable
	 * @return
	 */
	float Kameleon::getConversionFactorToSI(const std::string& variable)
	{
		boost::unordered_map<std::string, float>::iterator iter = conversionFactorsToSI.find(variable);

		if (iter != conversionFactorsToSI.end())
			return (*iter).second;
		else
		{
			std::cout << "Kameleon::getConversionFactorToSI(): " << std::endl;
			return model->getConversionFactorToSI(variable);
		}
	}



	/**
	 * Initializes the conversion factors required to convert the interpolated values to SI units. This is currently
	 * not implemented.
	 */
	void Kameleon::initializeConversionFactorsToSI()
	{

		conversionFactorsToSI["b"] = 1e-9f;

		/*    conversionFactorsToSI["pram"] = 1.0f;
		 conversionFactorsToSI["edotj"] = 1.0f;
		 conversionFactorsToSI["e"] = "mV/m";
		 conversionFactorsToSI["ex"] = "mV/m";
		 conversionFactorsToSI["ey"] = "mV/m";
		 conversionFactorsToSI["ez"] = "mV/m";
		 conversionFactorsToSI["er"] = "mV/m";
		 conversionFactorsToSI["etheta"] = "mV/m";
		 conversionFactorsToSI["ephi"] = "mV/m";
		 conversionFactorsToSI["br"] = "nT";
		 conversionFactorsToSI["b_r"] = "nT";
		 conversionFactorsToSI["b_lat"] = "nT";
		 conversionFactorsToSI["btheta"] = "nT";
		 conversionFactorsToSI["b_lon"] = "nT";
		 conversionFactorsToSI["bphi"] = "nT";
		 conversionFactorsToSI["j"] = "muA/m^2";
		 conversionFactorsToSI["jparx"] = "muA/m^2";
		 conversionFactorsToSI["jpary"] = "muA/m^2";
		 conversionFactorsToSI["jparz"] = "muA/m^2";
		 conversionFactorsToSI["jparr"] = "muA/m^2";
		 conversionFactorsToSI["jpartheta"] = "muA/m^2";
		 conversionFactorsToSI["jparphi"] = "muA/m^2";
		 conversionFactorsToSI["jpar"] = "muA/m^2";
		 conversionFactorsToSI["jxbx"] = "fN/m^3";
		 conversionFactorsToSI["jxby"] = "fN/m^3";
		 conversionFactorsToSI["jxbz"] = "fN/m^3";
		 conversionFactorsToSI["jxb"] = "fN/m^3";
		 conversionFactorsToSI["exbr"] = "muW/m^2";
		 conversionFactorsToSI["exbphi"] = "muW/m^2";
		 conversionFactorsToSI["exbtheta"] = "muW/m^2";
		 conversionFactorsToSI["exbx"] = "muW/m^2";
		 conversionFactorsToSI["exby"] = "muW/m^2";
		 conversionFactorsToSI["exbz"] = "muW/m^2";
		 conversionFactorsToSI["exb"] = "muW/m^2";
		 conversionFactorsToSI["s"] = "Km^2";
		 conversionFactorsToSI["en"] = "J/m^3";
		 conversionFactorsToSI["nv"] = "cm^-2s^-1";
		 conversionFactorsToSI["nvx"] = "cm^-2s^-1";
		 conversionFactorsToSI["nvy"] = "cm^-2s^-1";
		 conversionFactorsToSI["nvz"] = "cm^-2s^-1";
		 conversionFactorsToSI["u"] = "km/s";
		 conversionFactorsToSI["v"] = "km/s";
		 conversionFactorsToSI["v_r"] = "km/s";
		 conversionFactorsToSI["v_lat"] = "km/s";
		 conversionFactorsToSI["v_lon"] = "km/s";
		 conversionFactorsToSI["n"] = "amu/cm^3";
		 conversionFactorsToSI["n*r^2"] = "AU^2 cm^-3";
		 conversionFactorsToSI["p*r^2"] = "nPa AU^2";
		 conversionFactorsToSI["p"] = "nPa";
		 conversionFactorsToSI["polb"] = "";
		 conversionFactorsToSI["b1"] = "nT";
		 conversionFactorsToSI["eta*j"] = "mV/m";
		 conversionFactorsToSI["eta*jx"] = "mV/m";
		 conversionFactorsToSI["eta*jy"] = "mV/m";
		 conversionFactorsToSI["eta*jz"] = "mV/m";
		 conversionFactorsToSI["eta*j^2"] = "pW/m^3";


		 conversionFactorsToSI["beta"] = "";
		 if (modelName == "enlil")
		 {
		 conversionFactorsToSI["ux"] = "km/s";
		 conversionFactorsToSI["uy"] = "km/s";
		 conversionFactorsToSI["uz"] = "km/s";
		 conversionFactorsToSI["bx"] = "nT";
		 conversionFactorsToSI["by"] = "nT";
		 conversionFactorsToSI["bz"] = "nT";
		 conversionFactorsToSI["b1x"] = "nT";
		 conversionFactorsToSI["b1y"] = "nT";
		 conversionFactorsToSI["b1z"] = "nT";
		 }

		 */

	}

	/**
	 * Returns the model name of the opened file.
	 * @return The model name.
	 */
	const std::string& Kameleon::getModelName()
	{
		return modelName;
	}

	/**
	 * Wrapper for the CXFORM function cxform(). Performs coordinate transformation from the source
	 * system to the target system at the specified time.
	 * @param from
	 * @param to
	 * @param et
	 * @param v_in
	 * @param v_out
	 */
	int Kameleon::_cxform(const char *from,const char *to,const double et,Position* v_in,Position* v_out)
	{
		double * v_in_ = new double[3];
		v_in_[0] = v_in->c0;
		v_in_[1] = v_in->c1;
		v_in_[2] = v_in->c2;
		double * v_out_ = new double[3];
		int status = cxform(from, to, et, v_in_, v_out_);
		v_out->c0 = v_out_[0];
		v_out->c1 = v_out_[1];
		v_out->c2 = v_out_[2];
		delete v_in_;
		delete v_out_;
		return status;
	}

	/**
	 * @param y
	 * @param m
	 * @param d
	 * @param h
	 * @param mi
	 * @param s
	 */
	double Kameleon::_gregorian_calendar_to_jd(int y, int m, int d, int h, int mi, int s)
	{
		return gregorian_calendar_to_jd(y,m,d,h,mi,s);
	}

	/**
	 * Wrapper for the CXFORM function cxRound()
	 * @param doub
	 */
	long Kameleon::_cxRound(double doub)
	{
		return cxRound(doub);
	}

	/**
	 * Wrapper for the CXFORM function date2es()
	 * @param yyyy
	 * @param mm
	 * @param dd
	 * @param hh
	 * @param mm2
	 * @param ss
	 */
	long Kameleon::_date2es(int yyyy, int mm, int dd, int hh, int mm2, int ss)
	{
		return date2es(yyyy,mm,dd,hh,mm2,ss);
	}




	std::vector<float>* Kameleon::getVariable(const std::string& variable)
	{
		return model->getVariable(variable);
	}
	std::vector<int>* Kameleon::getVariableInt(const std::string& variable)
	{
		return model->getVariableInt(variable);
	}
	int Kameleon::getNumberOfGlobalAttributes()
	{
		return model->getNumberOfGlobalAttributes();
	}
	long Kameleon::getVariableID(const std::string& variable)
	{
		return model->getVariableID(variable);
	}
	std::string Kameleon::getVariableName(long variable_id)
	{
		return model->getVariableName(variable_id);
	}
	Attribute Kameleon::getGlobalAttribute(long i)
	{
		return model->getGlobalAttribute(i);
	}
	std::string Kameleon::getGlobalAttributeName(long attribute_id)
	{
		return model->getGlobalAttributeName(attribute_id);
	}
	Attribute Kameleon::getGlobalAttribute(const std::string& attribute)
	{
		return model->getGlobalAttribute(attribute);
	}
	Attribute Kameleon::getVariableAttribute(const std::string& variable, const std::string& attribute)
	{
		return model->getVariableAttribute(variable, attribute);
	}
	bool Kameleon::doesAttributeExist(const std::string& attribute)
	{
		return model->doesAttributeExist(attribute);
	}
	bool Kameleon::doesVariableExist(const std::string& variable)
	{
		return model->doesVariableExist(variable);
	}


	CDFid Kameleon::getCurrentFileID()
	{
		return model->getCurrentFileID();
	}

	const std::string& Kameleon::getCurrentFilename()
	{
		return model->getCurrentFilename();
	}

	int Kameleon::getNumberOfVariableAttributes()
	{
		return model->getNumberOfVariableAttributes();
	}
}