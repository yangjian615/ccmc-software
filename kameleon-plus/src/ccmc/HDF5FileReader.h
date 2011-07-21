/*
 * HDFFileReader.h
 *
 *  Created on: July 12, 2011
 *      Author: David Berrios
 */

#ifndef HDFFILEREADER_H_
#define HDFFILEREADER_H_
#include <string>
#include <vector>
#include <iostream>
#include "Attribute.h"
#include <boost/unordered_map.hpp>
#include "H5Cpp.h"
#include "FileReader.h"





namespace ccmc
{


	/**
	 * @class FileReader FileReader.h ccmc/FileReader.h
	 * @brief TODO: Brief description of FileReader class
	 *
	 * TODO: Full description of FileReader class
	 */

	class HDF5FileReader : public FileReader
	{

		public:

			HDF5FileReader();
			std::vector<float>* getVariable(const std::string& variable);
			std::vector<float>* getVariable(long variableID);
			std::vector<float>* getVariable(const std::string& variable, long startIndex, long count);
			std::vector<float>* getVariable(long variableID, long startIndex, long count);
			float getVariableAtIndex(const std::string& variable, long index);
			float getVariableAtIndex(long variable_id, long index);
			std::vector<int>* getVariableInt(const std::string& variable);
			int getVariableIntAtIndex(const std::string& variable, long index);
			int getNumberOfGlobalAttributes();
			int getNumberOfVariables();
			int getNumberOfVariableAttributes();
			long getNumberOfRecords(const std::string& variable);
			long getNumberOfRecords(long variable_id);
			long getVariableID(const std::string& variable);
			std::string getVariableName(long variable_id);
			Attribute getGlobalAttribute(long i);
			std::string getGlobalAttributeName(long attribute_id);
			std::string getVariableAttributeName(long attribute_id);
			Attribute getGlobalAttribute(const std::string& attribute);
			Attribute getVariableAttribute(const std::string& variable, const std::string& attribute);
			std::vector<std::string> getVariableAttributeNames();
			bool doesAttributeExist(const std::string& attribute);
			bool doesVariableExist(const std::string& variable);
			const std::string& getCurrentFilename();
			virtual ~HDF5FileReader();


		protected:
			std::string current_filename;
			H5::H5File * current_file;
			long closeFile();
			long openFile(const std::string& filename);
			void initializeGlobalAttributes();
			void initializeVariableAttributes();
			void initializeVariableIDs();
			void initializeVariableNames();

	};
}

#endif /* HDFFILEREADER_H_ */
