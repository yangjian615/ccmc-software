/*
 * Adapt3D.cpp
 *
 *  Created on: Oct 29, 2010
 *      Author: David Berrios
 */

#include "Adapt3D.h"
#include "Point.h"
#include "Cell3D.h"
#include "Vector.h"
#include "Adapt3DInterpolator.h"
#include "StringConstants.h"


namespace ccmc
{
	/**
	 * Default constructor
	 */
	Adapt3D::Adapt3D()
	{
		ndimn=NDIMN_ADAPT3D;
		nnode=NNODE_ADAPT3D;
		nvars=NVARS_ADAPT3D;

	}

	/**
	 * @copydoc Model::open()
	 */
	long Adapt3D::open(const std::string& filename)
	{

		long status;
		status = openFile(filename);

		if (status != FileReader::OK)
		   return status;

		//counts[0] = 1; 									/* set values */
		//intervals[0] = 1;

		   /* get all of the cdf attribute/variable numbers that will be needed *******/

		if (this->doesVariableExist(ccmc::strings::variables::coord_) == FileReader::OK)
		{
			status = this->loadVariable(ccmc::strings::variables::coord_);
			if (status != FileReader::OK)
				return FileReader::LOAD_FAILED;
		} else
			return FileReader::VARIABLE_DOES_NOT_EXIST;

		if (this->doesVariableExist(ccmc::strings::variables::unkno_) != FileReader::OK)
		{
			status = this->loadVariable(ccmc::strings::variables::unkno_);
			if (status != FileReader::OK)
				return FileReader::LOAD_FAILED;
		} else
			return FileReader::VARIABLE_DOES_NOT_EXIST;

		if (this->doesVariableExist(ccmc::strings::variables::intmat_) == FileReader::OK)
		{
			status = this->loadVariableInt(ccmc::strings::variables::intmat_);
			if (status != FileReader::OK)
				return FileReader::LOAD_FAILED;
		} else
			return FileReader::VARIABLE_DOES_NOT_EXIST;

		/***  Check the existence of necessary attributes.  Fail if any don't exist ***/
		if (doesAttributeExist(ccmc::strings::variables::grid_reg_no_) == FileReader::OK)
		{
			this->grid_reg_no = (this->getGlobalAttribute(ccmc::strings::variables::grid_reg_no_)).getAttributeInt();
		} else
			return FileReader::ATTRIBUTE_DOES_NOT_EXIST;
		if (doesAttributeExist(ccmc::strings::variables::ndimn_) == FileReader::OK)
		{
			this->ndimn = (this->getGlobalAttribute(ccmc::strings::variables::ndimn_)).getAttributeInt();
		} else
			return FileReader::ATTRIBUTE_DOES_NOT_EXIST;

		if (doesAttributeExist(ccmc::strings::variables::npoin_) == FileReader::OK)
		{
			this->npoin = (this->getGlobalAttribute(ccmc::strings::variables::npoin_)).getAttributeInt();
		} else
			return FileReader::ATTRIBUTE_DOES_NOT_EXIST;

		if (doesAttributeExist(ccmc::strings::variables::nelem_) == FileReader::OK)
		{
			this->nelem = (this->getGlobalAttribute(ccmc::strings::variables::nelem_)).getAttributeInt();
		} else
			return FileReader::ATTRIBUTE_DOES_NOT_EXIST;

		if (doesAttributeExist(ccmc::strings::variables::nboun_) == FileReader::OK)
		{
			this->nboun = (this->getGlobalAttribute(ccmc::strings::variables::nboun_)).getAttributeInt();
		} else
			return FileReader::ATTRIBUTE_DOES_NOT_EXIST;

		if (doesAttributeExist(ccmc::strings::variables::nconi_) == FileReader::OK)
		{
			this->nconi = (this->getGlobalAttribute(ccmc::strings::variables::nconi_)).getAttributeInt();
		} else
			return FileReader::ATTRIBUTE_DOES_NOT_EXIST;




	}







	/**
	 *
	 * @copydoc Model::initializeSIUnits()
	 *
	 */
	void Adapt3D::initializeSIUnits()
	{
		variableSIUnits[ccmc::strings::variables::bx_] = "T";
		variableSIUnits[ccmc::strings::variables::by_] = "T";
		variableSIUnits[ccmc::strings::variables::bz_] = "T";
		variableSIUnits[ccmc::strings::variables::ux_] = "m/s";
		variableSIUnits[ccmc::strings::variables::uy_] = "m/s";
		variableSIUnits[ccmc::strings::variables::uz_] = "m/s";
		variableSIUnits[ccmc::strings::variables::jx_] = "A/m^2";
		variableSIUnits[ccmc::strings::variables::jy_] = "A/m^2";
		variableSIUnits[ccmc::strings::variables::jz_] = "A/m^2";
		variableSIUnits[ccmc::strings::variables::b1x_] = "T";
		variableSIUnits[ccmc::strings::variables::b1y_] = "T";
		variableSIUnits[ccmc::strings::variables::b1z_] = "T";
		variableSIUnits[ccmc::strings::variables::rho_] = "m^-3";
		variableSIUnits[ccmc::strings::variables::p_] = "Pa";
		variableSIUnits[ccmc::strings::variables::e_] = "J/m^3";
	}


	/**
	 * @copydoc Model::initializeConversionFactorsToSI()
	 */
	void Adapt3D::initializeConversionFactorsToSI()
	{

		/**
		 * TODO: fix these conversion factors
		 */
		conversionFactorsToSI[ccmc::strings::variables::bx_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::by_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::bz_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::ux_] = 1e3f;
		conversionFactorsToSI[ccmc::strings::variables::uy_] = 1e3f;
		conversionFactorsToSI[ccmc::strings::variables::uz_] = 1e3f;
		conversionFactorsToSI[ccmc::strings::variables::jx_] = 1e-6f;
		conversionFactorsToSI[ccmc::strings::variables::jy_] = 1e-6f;
		conversionFactorsToSI[ccmc::strings::variables::jz_] = 1e-6f;
		conversionFactorsToSI[ccmc::strings::variables::b1x_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::b1y_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::b1z_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::rho_] = 1e6;
		conversionFactorsToSI[ccmc::strings::variables::p_] = 1e-9f;
		conversionFactorsToSI[ccmc::strings::variables::e_] = 1e-15f;

	}


	/**
	 * @copydoc Model::createNewInterpolator()
	 */
	Interpolator * Adapt3D::createNewInterpolator()
	{
		Interpolator * interpolator = new Adapt3DInterpolator(this);
		return interpolator;
	}

	/**
	 * Destructor
	 */
	Adapt3D::~Adapt3D()
	{
		// TODO Auto-generated destructor stub
//		std::cout << "deleting Adapt3D object" << std::endl;
	}
}