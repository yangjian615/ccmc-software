/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.0
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package gov.nasa.gsfc.ccmc;

public class FileReader {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  public FileReader(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  public static long getCPtr(FileReader obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        CCMCJNI.delete_FileReader(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public FileReader() {
    this(CCMCJNI.new_FileReader(), true);
  }

  public int open(String filename) {
    return CCMCJNI.FileReader_open(swigCPtr, this, filename);
  }

  public vector_float getVariable(String variable) {
    long cPtr = CCMCJNI.FileReader_getVariable__SWIG_0(swigCPtr, this, variable);
    return (cPtr == 0) ? null : new vector_float(cPtr, false);
  }

  public vector_float getVariableByID(int variableID) {
    long cPtr = CCMCJNI.FileReader_getVariableByID__SWIG_0(swigCPtr, this, variableID);
    return (cPtr == 0) ? null : new vector_float(cPtr, false);
  }

  public vector_float getVariable(String variable, int startIndex, int count) {
    long cPtr = CCMCJNI.FileReader_getVariable__SWIG_1(swigCPtr, this, variable, startIndex, count);
    return (cPtr == 0) ? null : new vector_float(cPtr, false);
  }

  public vector_float getVariableByID(int variableID, int startIndex, int count) {
    long cPtr = CCMCJNI.FileReader_getVariableByID__SWIG_1(swigCPtr, this, variableID, startIndex, count);
    return (cPtr == 0) ? null : new vector_float(cPtr, false);
  }

  public float getVariableAtIndex(String variable, int index) {
    return CCMCJNI.FileReader_getVariableAtIndex(swigCPtr, this, variable, index);
  }

  public float getVariableAtIndexByID(int variable_id, int index) {
    return CCMCJNI.FileReader_getVariableAtIndexByID(swigCPtr, this, variable_id, index);
  }

  public vector_int getVariableInt(String variable) {
    long cPtr = CCMCJNI.FileReader_getVariableInt(swigCPtr, this, variable);
    return (cPtr == 0) ? null : new vector_int(cPtr, false);
  }

  public int getVariableIntAtIndex(String variable, int index) {
    return CCMCJNI.FileReader_getVariableIntAtIndex(swigCPtr, this, variable, index);
  }

  public int getNumberOfGlobalAttributes() {
    return CCMCJNI.FileReader_getNumberOfGlobalAttributes(swigCPtr, this);
  }

  public int getNumberOfVariables() {
    return CCMCJNI.FileReader_getNumberOfVariables(swigCPtr, this);
  }

  public int getNumberOfVariableAttributes() {
    return CCMCJNI.FileReader_getNumberOfVariableAttributes(swigCPtr, this);
  }

  public int getNumberOfRecords(String variable) {
    return CCMCJNI.FileReader_getNumberOfRecords__SWIG_0(swigCPtr, this, variable);
  }

  public int getNumberOfRecords(int variable_id) {
    return CCMCJNI.FileReader_getNumberOfRecords__SWIG_1(swigCPtr, this, variable_id);
  }

  public int getVariableID(String variable) {
    return CCMCJNI.FileReader_getVariableID(swigCPtr, this, variable);
  }

  public String getVariableName(int variable_id) {
    return CCMCJNI.FileReader_getVariableName(swigCPtr, this, variable_id);
  }

  public Attribute getGlobalAttribute(int i) {
    return new Attribute(CCMCJNI.FileReader_getGlobalAttribute__SWIG_0(swigCPtr, this, i), true);
  }

  public String getGlobalAttributeName(int attribute_id) {
    return CCMCJNI.FileReader_getGlobalAttributeName(swigCPtr, this, attribute_id);
  }

  public String getVariableAttributeName(int attribute_id) {
    return CCMCJNI.FileReader_getVariableAttributeName(swigCPtr, this, attribute_id);
  }

  public Attribute getGlobalAttribute(String attribute) {
    return new Attribute(CCMCJNI.FileReader_getGlobalAttribute__SWIG_1(swigCPtr, this, attribute), true);
  }

  public Attribute getVariableAttribute(String variable, String attribute) {
    return new Attribute(CCMCJNI.FileReader_getVariableAttribute(swigCPtr, this, variable, attribute), true);
  }

  public vector_string getVariableAttributeNames() {
    return new vector_string(CCMCJNI.FileReader_getVariableAttributeNames(swigCPtr, this), true);
  }

  public boolean doesAttributeExist(String attribute) {
    return CCMCJNI.FileReader_doesAttributeExist(swigCPtr, this, attribute);
  }

  public boolean doesVariableExist(String variable) {
    return CCMCJNI.FileReader_doesVariableExist(swigCPtr, this, variable);
  }

  public int close() {
    return CCMCJNI.FileReader_close(swigCPtr, this);
  }

  public SWIGTYPE_p_void getCurrentFileID() {
    long cPtr = CCMCJNI.FileReader_getCurrentFileID(swigCPtr, this);
    return (cPtr == 0) ? null : new SWIGTYPE_p_void(cPtr, false);
  }

  public String getCurrentFilename() {
    return CCMCJNI.FileReader_getCurrentFilename(swigCPtr, this);
  }

  public final static int OK = CCMCJNI.FileReader_OK_get();
  public final static int OPEN_ERROR = CCMCJNI.FileReader_OPEN_ERROR_get();
  public final static int FILE_DOES_NOT_EXIST = CCMCJNI.FileReader_FILE_DOES_NOT_EXIST_get();
  public final static int VARIABLE_DOES_NOT_EXIST = CCMCJNI.FileReader_VARIABLE_DOES_NOT_EXIST_get();
  public final static int ATTRIBUTE_DOES_NOT_EXIST = CCMCJNI.FileReader_ATTRIBUTE_DOES_NOT_EXIST_get();
  public final static int LOAD_FAILED = CCMCJNI.FileReader_LOAD_FAILED_get();
  public final static int UNABLE_TO_ALLOCATE_MEMORY = CCMCJNI.FileReader_UNABLE_TO_ALLOCATE_MEMORY_get();
  public final static int VARIABLE_NOT_IN_MEMORY = CCMCJNI.FileReader_VARIABLE_NOT_IN_MEMORY_get();
  public final static int MODEL_NOT_SUPPORTED = CCMCJNI.FileReader_MODEL_NOT_SUPPORTED_get();
  public final static int NOT_A_VALID_KAMELEON_FILE = CCMCJNI.FileReader_NOT_A_VALID_KAMELEON_FILE_get();
}
