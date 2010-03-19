/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.40
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package ccmc.wrappers;

public class CCMC {
  public static double parseEPOCH3(String epString) {
    return CCMCJNI.parseEPOCH3(epString);
  }

  public static void encodeEPOCH3(double epoch, String epString) {
    CCMCJNI.encodeEPOCH3(epoch, epString);
  }

  public static void setKameleonObjects(SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Kameleon_p_t value) {
    CCMCJNI.kameleonObjects_set(SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Kameleon_p_t.getCPtr(value));
  }

  public static SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Kameleon_p_t getKameleonObjects() {
    return new SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Kameleon_p_t(CCMCJNI.kameleonObjects_get(), true);
  }

  public static void setInterpolatorObjects(SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Interpolator_p_t value) {
    CCMCJNI.interpolatorObjects_set(SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Interpolator_p_t.getCPtr(value));
  }

  public static SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Interpolator_p_t getInterpolatorObjects() {
    return new SWIGTYPE_p_boost__unordered_mapT_int_ccmc__Interpolator_p_t(CCMCJNI.interpolatorObjects_get(), true);
  }

  public static void setFileReaderObjects(SWIGTYPE_p_boost__unordered_mapT_int_ccmc__FileReader_p_t value) {
    CCMCJNI.fileReaderObjects_set(SWIGTYPE_p_boost__unordered_mapT_int_ccmc__FileReader_p_t.getCPtr(value));
  }

  public static SWIGTYPE_p_boost__unordered_mapT_int_ccmc__FileReader_p_t getFileReaderObjects() {
    return new SWIGTYPE_p_boost__unordered_mapT_int_ccmc__FileReader_p_t(CCMCJNI.fileReaderObjects_get(), true);
  }

}
