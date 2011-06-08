# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.3
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_CCMC', [dirname(__file__)])
        except ImportError:
            import _CCMC
            return _CCMC
        if fp is not None:
            try:
                _mod = imp.load_module('_CCMC', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _CCMC = swig_import_helper()
    del swig_import_helper
else:
    import _CCMC
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _CCMC.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _CCMC.SwigPyIterator_value(self)
    def incr(self, n = 1): return _CCMC.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _CCMC.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _CCMC.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _CCMC.SwigPyIterator_equal(self, *args)
    def copy(self): return _CCMC.SwigPyIterator_copy(self)
    def next(self): return _CCMC.SwigPyIterator_next(self)
    def __next__(self): return _CCMC.SwigPyIterator___next__(self)
    def previous(self): return _CCMC.SwigPyIterator_previous(self)
    def advance(self, *args): return _CCMC.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _CCMC.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _CCMC.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _CCMC.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _CCMC.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _CCMC.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _CCMC.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _CCMC.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class FileReader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileReader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileReader, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CCMC.new_FileReader()
        try: self.this.append(this)
        except: self.this = this
    def open(self, *args): return _CCMC.FileReader_open(self, *args)
    def getVariable(self, *args): return _CCMC.FileReader_getVariable(self, *args)
    def getVariableByID(self, *args): return _CCMC.FileReader_getVariableByID(self, *args)
    def getVariableAtIndex(self, *args): return _CCMC.FileReader_getVariableAtIndex(self, *args)
    def getVariableAtIndexByID(self, *args): return _CCMC.FileReader_getVariableAtIndexByID(self, *args)
    def getVariableInt(self, *args): return _CCMC.FileReader_getVariableInt(self, *args)
    def getVariableIntAtIndex(self, *args): return _CCMC.FileReader_getVariableIntAtIndex(self, *args)
    def getNumberOfGlobalAttributes(self): return _CCMC.FileReader_getNumberOfGlobalAttributes(self)
    def getNumberOfVariables(self): return _CCMC.FileReader_getNumberOfVariables(self)
    def getNumberOfVariableAttributes(self): return _CCMC.FileReader_getNumberOfVariableAttributes(self)
    def getNumberOfRecords(self, *args): return _CCMC.FileReader_getNumberOfRecords(self, *args)
    def getVariableID(self, *args): return _CCMC.FileReader_getVariableID(self, *args)
    def getVariableName(self, *args): return _CCMC.FileReader_getVariableName(self, *args)
    def getGlobalAttributeName(self, *args): return _CCMC.FileReader_getGlobalAttributeName(self, *args)
    def getVariableAttributeName(self, *args): return _CCMC.FileReader_getVariableAttributeName(self, *args)
    def getGlobalAttribute(self, *args): return _CCMC.FileReader_getGlobalAttribute(self, *args)
    def getVariableAttribute(self, *args): return _CCMC.FileReader_getVariableAttribute(self, *args)
    def getVariableAttributeNames(self): return _CCMC.FileReader_getVariableAttributeNames(self)
    def doesAttributeExist(self, *args): return _CCMC.FileReader_doesAttributeExist(self, *args)
    def doesVariableExist(self, *args): return _CCMC.FileReader_doesVariableExist(self, *args)
    def close(self): return _CCMC.FileReader_close(self)
    def getCurrentFileID(self): return _CCMC.FileReader_getCurrentFileID(self)
    def getCurrentFilename(self): return _CCMC.FileReader_getCurrentFilename(self)
    __swig_destroy__ = _CCMC.delete_FileReader
    __del__ = lambda self : None;
    OK = _CCMC.FileReader_OK
    OPEN_ERROR = _CCMC.FileReader_OPEN_ERROR
    FILE_DOES_NOT_EXIST = _CCMC.FileReader_FILE_DOES_NOT_EXIST
    VARIABLE_DOES_NOT_EXIST = _CCMC.FileReader_VARIABLE_DOES_NOT_EXIST
    ATTRIBUTE_DOES_NOT_EXIST = _CCMC.FileReader_ATTRIBUTE_DOES_NOT_EXIST
    LOAD_FAILED = _CCMC.FileReader_LOAD_FAILED
    UNABLE_TO_ALLOCATE_MEMORY = _CCMC.FileReader_UNABLE_TO_ALLOCATE_MEMORY
    VARIABLE_NOT_IN_MEMORY = _CCMC.FileReader_VARIABLE_NOT_IN_MEMORY
    MODEL_NOT_SUPPORTED = _CCMC.FileReader_MODEL_NOT_SUPPORTED
    NOT_A_VALID_KAMELEON_FILE = _CCMC.FileReader_NOT_A_VALID_KAMELEON_FILE
FileReader_swigregister = _CCMC.FileReader_swigregister
FileReader_swigregister(FileReader)


def parseEPOCH3(*args):
  return _CCMC.parseEPOCH3(*args)
parseEPOCH3 = _CCMC.parseEPOCH3

def encodeEPOCH3(*args):
  return _CCMC.encodeEPOCH3(*args)
encodeEPOCH3 = _CCMC.encodeEPOCH3
class Position(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Position, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Position, name)
    __repr__ = _swig_repr
    __swig_setmethods__["c0"] = _CCMC.Position_c0_set
    __swig_getmethods__["c0"] = _CCMC.Position_c0_get
    if _newclass:c0 = _swig_property(_CCMC.Position_c0_get, _CCMC.Position_c0_set)
    __swig_setmethods__["c1"] = _CCMC.Position_c1_set
    __swig_getmethods__["c1"] = _CCMC.Position_c1_get
    if _newclass:c1 = _swig_property(_CCMC.Position_c1_get, _CCMC.Position_c1_set)
    __swig_setmethods__["c2"] = _CCMC.Position_c2_set
    __swig_getmethods__["c2"] = _CCMC.Position_c2_get
    if _newclass:c2 = _swig_property(_CCMC.Position_c2_get, _CCMC.Position_c2_set)
    def __init__(self): 
        this = _CCMC.new_Position()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _CCMC.delete_Position
    __del__ = lambda self : None;
Position_swigregister = _CCMC.Position_swigregister
Position_swigregister(Position)

class Time(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Time, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Time, name)
    __repr__ = _swig_repr
    __swig_setmethods__["year"] = _CCMC.Time_year_set
    __swig_getmethods__["year"] = _CCMC.Time_year_get
    if _newclass:year = _swig_property(_CCMC.Time_year_get, _CCMC.Time_year_set)
    __swig_setmethods__["month"] = _CCMC.Time_month_set
    __swig_getmethods__["month"] = _CCMC.Time_month_get
    if _newclass:month = _swig_property(_CCMC.Time_month_get, _CCMC.Time_month_set)
    __swig_setmethods__["day"] = _CCMC.Time_day_set
    __swig_getmethods__["day"] = _CCMC.Time_day_get
    if _newclass:day = _swig_property(_CCMC.Time_day_get, _CCMC.Time_day_set)
    __swig_setmethods__["hour"] = _CCMC.Time_hour_set
    __swig_getmethods__["hour"] = _CCMC.Time_hour_get
    if _newclass:hour = _swig_property(_CCMC.Time_hour_get, _CCMC.Time_hour_set)
    __swig_setmethods__["minute"] = _CCMC.Time_minute_set
    __swig_getmethods__["minute"] = _CCMC.Time_minute_get
    if _newclass:minute = _swig_property(_CCMC.Time_minute_get, _CCMC.Time_minute_set)
    __swig_setmethods__["second"] = _CCMC.Time_second_set
    __swig_getmethods__["second"] = _CCMC.Time_second_get
    if _newclass:second = _swig_property(_CCMC.Time_second_get, _CCMC.Time_second_set)
    def __init__(self): 
        this = _CCMC.new_Time()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _CCMC.delete_Time
    __del__ = lambda self : None;
Time_swigregister = _CCMC.Time_swigregister
Time_swigregister(Time)

class Kameleon(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Kameleon, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Kameleon, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CCMC.new_Kameleon()
        try: self.this.append(this)
        except: self.this = this
    def open(self, *args): return _CCMC.Kameleon_open(self, *args)
    def getModelName(self): return _CCMC.Kameleon_getModelName(self)
    def setMissingValue(self, *args): return _CCMC.Kameleon_setMissingValue(self, *args)
    def getMissingValue(self): return _CCMC.Kameleon_getMissingValue(self)
    def createNewInterpolator(self): return _CCMC.Kameleon_createNewInterpolator(self)
    def loadVariable(self, *args): return _CCMC.Kameleon_loadVariable(self, *args)
    def unloadVariable(self, *args): return _CCMC.Kameleon_unloadVariable(self, *args)
    def loadVectorVariable(self, *args): return _CCMC.Kameleon_loadVectorVariable(self, *args)
    def unloadVectorVariable(self, *args): return _CCMC.Kameleon_unloadVectorVariable(self, *args)
    def getNativeUnit(self, *args): return _CCMC.Kameleon_getNativeUnit(self, *args)
    def getSIUnit(self, *args): return _CCMC.Kameleon_getSIUnit(self, *args)
    def getVisUnit(self, *args): return _CCMC.Kameleon_getVisUnit(self, *args)
    def getConversionFactorToSI(self, *args): return _CCMC.Kameleon_getConversionFactorToSI(self, *args)
    def getVariable(self, *args): return _CCMC.Kameleon_getVariable(self, *args)
    def getVariableInt(self, *args): return _CCMC.Kameleon_getVariableInt(self, *args)
    def getNumberOfGlobalAttributes(self): return _CCMC.Kameleon_getNumberOfGlobalAttributes(self)
    def getNumberOfVariableAttributes(self): return _CCMC.Kameleon_getNumberOfVariableAttributes(self)
    def getVariableID(self, *args): return _CCMC.Kameleon_getVariableID(self, *args)
    def getVariableName(self, *args): return _CCMC.Kameleon_getVariableName(self, *args)
    def getGlobalAttributeName(self, *args): return _CCMC.Kameleon_getGlobalAttributeName(self, *args)
    def getGlobalAttribute(self, *args): return _CCMC.Kameleon_getGlobalAttribute(self, *args)
    def getVariableAttribute(self, *args): return _CCMC.Kameleon_getVariableAttribute(self, *args)
    def getVariableAttributeName(self, *args): return _CCMC.Kameleon_getVariableAttributeName(self, *args)
    def getLoadedVariables(self): return _CCMC.Kameleon_getLoadedVariables(self)
    def getNumberOfVariables(self): return _CCMC.Kameleon_getNumberOfVariables(self)
    def doesAttributeExist(self, *args): return _CCMC.Kameleon_doesAttributeExist(self, *args)
    def doesVariableExist(self, *args): return _CCMC.Kameleon_doesVariableExist(self, *args)
    def getCurrentFileID(self): return _CCMC.Kameleon_getCurrentFileID(self)
    def getCurrentFilename(self): return _CCMC.Kameleon_getCurrentFilename(self)
    __swig_getmethods__["_cxform"] = lambda x: _CCMC.Kameleon__cxform
    if _newclass:_cxform = staticmethod(_CCMC.Kameleon__cxform)
    __swig_getmethods__["_gregorian_calendar_to_jd"] = lambda x: _CCMC.Kameleon__gregorian_calendar_to_jd
    if _newclass:_gregorian_calendar_to_jd = staticmethod(_CCMC.Kameleon__gregorian_calendar_to_jd)
    __swig_getmethods__["_cxRound"] = lambda x: _CCMC.Kameleon__cxRound
    if _newclass:_cxRound = staticmethod(_CCMC.Kameleon__cxRound)
    __swig_getmethods__["_date2es"] = lambda x: _CCMC.Kameleon__date2es
    if _newclass:_date2es = staticmethod(_CCMC.Kameleon__date2es)
    def close(self): return _CCMC.Kameleon_close(self)
    def getCurrentTime(self): return _CCMC.Kameleon_getCurrentTime(self)
    __swig_destroy__ = _CCMC.delete_Kameleon
    __del__ = lambda self : None;
Kameleon_swigregister = _CCMC.Kameleon_swigregister
Kameleon_swigregister(Kameleon)

def Kameleon__cxform(*args):
  return _CCMC.Kameleon__cxform(*args)
Kameleon__cxform = _CCMC.Kameleon__cxform

def Kameleon__gregorian_calendar_to_jd(*args):
  return _CCMC.Kameleon__gregorian_calendar_to_jd(*args)
Kameleon__gregorian_calendar_to_jd = _CCMC.Kameleon__gregorian_calendar_to_jd

def Kameleon__cxRound(*args):
  return _CCMC.Kameleon__cxRound(*args)
Kameleon__cxRound = _CCMC.Kameleon__cxRound

def Kameleon__date2es(*args):
  return _CCMC.Kameleon__date2es(*args)
Kameleon__date2es = _CCMC.Kameleon__date2es

class Interpolator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Interpolator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Interpolator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def interpolate(self, *args): return _CCMC.Interpolator_interpolate(self, *args)
    def getConversionFactor(self, *args): return _CCMC.Interpolator_getConversionFactor(self, *args)
    def setMissingValue(self, *args): return _CCMC.Interpolator_setMissingValue(self, *args)
    def getModelName(self): return _CCMC.Interpolator_getModelName(self)
    __swig_destroy__ = _CCMC.delete_Interpolator
    __del__ = lambda self : None;
Interpolator_swigregister = _CCMC.Interpolator_swigregister
Interpolator_swigregister(Interpolator)
cvar = _CCMC.cvar

class Tracer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tracer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tracer, name)
    __repr__ = _swig_repr
    FOWARD = _CCMC.Tracer_FOWARD
    REVERSE = _CCMC.Tracer_REVERSE
    def __init__(self, *args): 
        this = _CCMC.new_Tracer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _CCMC.delete_Tracer
    __del__ = lambda self : None;
    def setInnerBoundary(self, *args): return _CCMC.Tracer_setInnerBoundary(self, *args)
    def setMaxIterations(self, *args): return _CCMC.Tracer_setMaxIterations(self, *args)
    def setDn(self, *args): return _CCMC.Tracer_setDn(self, *args)
    def setTilt(self, *args): return _CCMC.Tracer_setTilt(self, *args)
    def setMissing(self, *args): return _CCMC.Tracer_setMissing(self, *args)
    def setMaxArcLength(self, *args): return _CCMC.Tracer_setMaxArcLength(self, *args)
    def bidirectionalTrace(self, *args): return _CCMC.Tracer_bidirectionalTrace(self, *args)
    def bidirectionalTraceWithDipole(self, *args): return _CCMC.Tracer_bidirectionalTraceWithDipole(self, *args)
    def unidirectionalTrace(self, *args): return _CCMC.Tracer_unidirectionalTrace(self, *args)
    def unidirectionalTraceWithDipole(self, *args): return _CCMC.Tracer_unidirectionalTraceWithDipole(self, *args)
    def findLastClosed(self, *args): return _CCMC.Tracer_findLastClosed(self, *args)
    def getLastClosedFieldlines(self, *args): return _CCMC.Tracer_getLastClosedFieldlines(self, *args)
    def isClosed(self, *args): return _CCMC.Tracer_isClosed(self, *args)
    def setUseMaxArcLength(self, *args): return _CCMC.Tracer_setUseMaxArcLength(self, *args)
    def getVector(self, *args): return _CCMC.Tracer_getVector(self, *args)
    def setRegionOfInterest(self, *args): return _CCMC.Tracer_setRegionOfInterest(self, *args)
    def setUseRegionOfInterest(self, *args): return _CCMC.Tracer_setUseRegionOfInterest(self, *args)
Tracer_swigregister = _CCMC.Tracer_swigregister
Tracer_swigregister(Tracer)

class Fieldline(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Fieldline, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Fieldline, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CCMC.new_Fieldline(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _CCMC.delete_Fieldline
    __del__ = lambda self : None;
    def insertPointData(self, *args): return _CCMC.Fieldline_insertPointData(self, *args)
    def removePoint(self, *args): return _CCMC.Fieldline_removePoint(self, *args)
    def reverseOrder(self): return _CCMC.Fieldline_reverseOrder(self)
    def reverseOrderInPlace(self): return _CCMC.Fieldline_reverseOrderInPlace(self)
    def getPositions(self): return _CCMC.Fieldline_getPositions(self)
    def size(self): return _CCMC.Fieldline_size(self)
    def getPosition(self, *args): return _CCMC.Fieldline_getPosition(self, *args)
    def getData(self, *args): return _CCMC.Fieldline_getData(self, *args)
    def getStartPoint(self): return _CCMC.Fieldline_getStartPoint(self)
    def reserve(self, *args): return _CCMC.Fieldline_reserve(self, *args)
    def setStartPoint(self, *args): return _CCMC.Fieldline_setStartPoint(self, *args)
    def setVariable(self, *args): return _CCMC.Fieldline_setVariable(self, *args)
    def getVariable(self): return _CCMC.Fieldline_getVariable(self)
    def getDs(self): return _CCMC.Fieldline_getDs(self)
    def getElements(self): return _CCMC.Fieldline_getElements(self)
    def getElement(self, *args): return _CCMC.Fieldline_getElement(self, *args)
    def integrate(self): return _CCMC.Fieldline_integrate(self)
    def measure(self): return _CCMC.Fieldline_measure(self)
    def getLength(self, *args): return _CCMC.Fieldline_getLength(self, *args)
    def getIntegral(self, *args): return _CCMC.Fieldline_getIntegral(self, *args)
    def interpolate(self, *args): return _CCMC.Fieldline_interpolate(self, *args)
    def getNearest(self): return _CCMC.Fieldline_getNearest(self)
Fieldline_swigregister = _CCMC.Fieldline_swigregister
Fieldline_swigregister(Fieldline)

class Point3f(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point3f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point3f, name)
    __repr__ = _swig_repr
    SPHERICAL = _CCMC.Point3f_SPHERICAL
    CARTESIAN = _CCMC.Point3f_CARTESIAN
    def __init__(self, *args): 
        this = _CCMC.new_Point3f(*args)
        try: self.this.append(this)
        except: self.this = this
    def normalize(self): return _CCMC.Point3f_normalize(self)
    def toString(self): return _CCMC.Point3f_toString(self)
    def magnitude(self): return _CCMC.Point3f_magnitude(self)
    def distance(self, *args): return _CCMC.Point3f_distance(self, *args)
    __swig_setmethods__["component1"] = _CCMC.Point3f_component1_set
    __swig_getmethods__["component1"] = _CCMC.Point3f_component1_get
    if _newclass:component1 = _swig_property(_CCMC.Point3f_component1_get, _CCMC.Point3f_component1_set)
    __swig_setmethods__["component2"] = _CCMC.Point3f_component2_set
    __swig_getmethods__["component2"] = _CCMC.Point3f_component2_get
    if _newclass:component2 = _swig_property(_CCMC.Point3f_component2_get, _CCMC.Point3f_component2_set)
    __swig_setmethods__["component3"] = _CCMC.Point3f_component3_set
    __swig_getmethods__["component3"] = _CCMC.Point3f_component3_get
    if _newclass:component3 = _swig_property(_CCMC.Point3f_component3_get, _CCMC.Point3f_component3_set)
    def __add__(self, *args): return _CCMC.Point3f___add__(self, *args)
    def __sub__(self, *args): return _CCMC.Point3f___sub__(self, *args)
    def __mul__(self, *args): return _CCMC.Point3f___mul__(self, *args)
    def setCoordinates(self, *args): return _CCMC.Point3f_setCoordinates(self, *args)
    def getCoordinates(self): return _CCMC.Point3f_getCoordinates(self)
    def getCartesian(self): return _CCMC.Point3f_getCartesian(self)
    __swig_destroy__ = _CCMC.delete_Point3f
    __del__ = lambda self : None;
Point3f_swigregister = _CCMC.Point3f_swigregister
Point3f_swigregister(Point3f)

class Attribute(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Attribute, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Attribute, name)
    __repr__ = _swig_repr
    FLOAT = _CCMC.Attribute_FLOAT
    INT = _CCMC.Attribute_INT
    STRING = _CCMC.Attribute_STRING
    def getAttributeName(self): return _CCMC.Attribute_getAttributeName(self)
    def setAttributeName(self, *args): return _CCMC.Attribute_setAttributeName(self, *args)
    def setAttributeValue(self, *args): return _CCMC.Attribute_setAttributeValue(self, *args)
    def getAttributeType(self): return _CCMC.Attribute_getAttributeType(self)
    def getAttributeFloat(self): return _CCMC.Attribute_getAttributeFloat(self)
    def getAttributeString(self): return _CCMC.Attribute_getAttributeString(self)
    def getAttributeInt(self): return _CCMC.Attribute_getAttributeInt(self)
    def __init__(self): 
        this = _CCMC.new_Attribute()
        try: self.this.append(this)
        except: self.this = this
    def toString(self): return _CCMC.Attribute_toString(self)
    __swig_destroy__ = _CCMC.delete_Attribute
    __del__ = lambda self : None;
Attribute_swigregister = _CCMC.Attribute_swigregister
Attribute_swigregister(Attribute)

class vector_point3f(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_point3f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_point3f, name)
    __repr__ = _swig_repr
    def iterator(self): return _CCMC.vector_point3f_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _CCMC.vector_point3f___nonzero__(self)
    def __bool__(self): return _CCMC.vector_point3f___bool__(self)
    def __len__(self): return _CCMC.vector_point3f___len__(self)
    def pop(self): return _CCMC.vector_point3f_pop(self)
    def __getslice__(self, *args): return _CCMC.vector_point3f___getslice__(self, *args)
    def __setslice__(self, *args): return _CCMC.vector_point3f___setslice__(self, *args)
    def __delslice__(self, *args): return _CCMC.vector_point3f___delslice__(self, *args)
    def __delitem__(self, *args): return _CCMC.vector_point3f___delitem__(self, *args)
    def __getitem__(self, *args): return _CCMC.vector_point3f___getitem__(self, *args)
    def __setitem__(self, *args): return _CCMC.vector_point3f___setitem__(self, *args)
    def append(self, *args): return _CCMC.vector_point3f_append(self, *args)
    def empty(self): return _CCMC.vector_point3f_empty(self)
    def size(self): return _CCMC.vector_point3f_size(self)
    def clear(self): return _CCMC.vector_point3f_clear(self)
    def swap(self, *args): return _CCMC.vector_point3f_swap(self, *args)
    def get_allocator(self): return _CCMC.vector_point3f_get_allocator(self)
    def begin(self): return _CCMC.vector_point3f_begin(self)
    def end(self): return _CCMC.vector_point3f_end(self)
    def rbegin(self): return _CCMC.vector_point3f_rbegin(self)
    def rend(self): return _CCMC.vector_point3f_rend(self)
    def pop_back(self): return _CCMC.vector_point3f_pop_back(self)
    def erase(self, *args): return _CCMC.vector_point3f_erase(self, *args)
    def __init__(self, *args): 
        this = _CCMC.new_vector_point3f(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _CCMC.vector_point3f_push_back(self, *args)
    def front(self): return _CCMC.vector_point3f_front(self)
    def back(self): return _CCMC.vector_point3f_back(self)
    def assign(self, *args): return _CCMC.vector_point3f_assign(self, *args)
    def resize(self, *args): return _CCMC.vector_point3f_resize(self, *args)
    def insert(self, *args): return _CCMC.vector_point3f_insert(self, *args)
    def reserve(self, *args): return _CCMC.vector_point3f_reserve(self, *args)
    def capacity(self): return _CCMC.vector_point3f_capacity(self)
    __swig_destroy__ = _CCMC.delete_vector_point3f
    __del__ = lambda self : None;
vector_point3f_swigregister = _CCMC.vector_point3f_swigregister
vector_point3f_swigregister(vector_point3f)

class vector_string(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_string, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_string, name)
    __repr__ = _swig_repr
    def iterator(self): return _CCMC.vector_string_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _CCMC.vector_string___nonzero__(self)
    def __bool__(self): return _CCMC.vector_string___bool__(self)
    def __len__(self): return _CCMC.vector_string___len__(self)
    def pop(self): return _CCMC.vector_string_pop(self)
    def __getslice__(self, *args): return _CCMC.vector_string___getslice__(self, *args)
    def __setslice__(self, *args): return _CCMC.vector_string___setslice__(self, *args)
    def __delslice__(self, *args): return _CCMC.vector_string___delslice__(self, *args)
    def __delitem__(self, *args): return _CCMC.vector_string___delitem__(self, *args)
    def __getitem__(self, *args): return _CCMC.vector_string___getitem__(self, *args)
    def __setitem__(self, *args): return _CCMC.vector_string___setitem__(self, *args)
    def append(self, *args): return _CCMC.vector_string_append(self, *args)
    def empty(self): return _CCMC.vector_string_empty(self)
    def size(self): return _CCMC.vector_string_size(self)
    def clear(self): return _CCMC.vector_string_clear(self)
    def swap(self, *args): return _CCMC.vector_string_swap(self, *args)
    def get_allocator(self): return _CCMC.vector_string_get_allocator(self)
    def begin(self): return _CCMC.vector_string_begin(self)
    def end(self): return _CCMC.vector_string_end(self)
    def rbegin(self): return _CCMC.vector_string_rbegin(self)
    def rend(self): return _CCMC.vector_string_rend(self)
    def pop_back(self): return _CCMC.vector_string_pop_back(self)
    def erase(self, *args): return _CCMC.vector_string_erase(self, *args)
    def __init__(self, *args): 
        this = _CCMC.new_vector_string(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _CCMC.vector_string_push_back(self, *args)
    def front(self): return _CCMC.vector_string_front(self)
    def back(self): return _CCMC.vector_string_back(self)
    def assign(self, *args): return _CCMC.vector_string_assign(self, *args)
    def resize(self, *args): return _CCMC.vector_string_resize(self, *args)
    def insert(self, *args): return _CCMC.vector_string_insert(self, *args)
    def reserve(self, *args): return _CCMC.vector_string_reserve(self, *args)
    def capacity(self): return _CCMC.vector_string_capacity(self)
    __swig_destroy__ = _CCMC.delete_vector_string
    __del__ = lambda self : None;
vector_string_swigregister = _CCMC.vector_string_swigregister
vector_string_swigregister(vector_string)

class vector_float(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_float, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_float, name)
    __repr__ = _swig_repr
    def iterator(self): return _CCMC.vector_float_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _CCMC.vector_float___nonzero__(self)
    def __bool__(self): return _CCMC.vector_float___bool__(self)
    def __len__(self): return _CCMC.vector_float___len__(self)
    def pop(self): return _CCMC.vector_float_pop(self)
    def __getslice__(self, *args): return _CCMC.vector_float___getslice__(self, *args)
    def __setslice__(self, *args): return _CCMC.vector_float___setslice__(self, *args)
    def __delslice__(self, *args): return _CCMC.vector_float___delslice__(self, *args)
    def __delitem__(self, *args): return _CCMC.vector_float___delitem__(self, *args)
    def __getitem__(self, *args): return _CCMC.vector_float___getitem__(self, *args)
    def __setitem__(self, *args): return _CCMC.vector_float___setitem__(self, *args)
    def append(self, *args): return _CCMC.vector_float_append(self, *args)
    def empty(self): return _CCMC.vector_float_empty(self)
    def size(self): return _CCMC.vector_float_size(self)
    def clear(self): return _CCMC.vector_float_clear(self)
    def swap(self, *args): return _CCMC.vector_float_swap(self, *args)
    def get_allocator(self): return _CCMC.vector_float_get_allocator(self)
    def begin(self): return _CCMC.vector_float_begin(self)
    def end(self): return _CCMC.vector_float_end(self)
    def rbegin(self): return _CCMC.vector_float_rbegin(self)
    def rend(self): return _CCMC.vector_float_rend(self)
    def pop_back(self): return _CCMC.vector_float_pop_back(self)
    def erase(self, *args): return _CCMC.vector_float_erase(self, *args)
    def __init__(self, *args): 
        this = _CCMC.new_vector_float(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _CCMC.vector_float_push_back(self, *args)
    def front(self): return _CCMC.vector_float_front(self)
    def back(self): return _CCMC.vector_float_back(self)
    def assign(self, *args): return _CCMC.vector_float_assign(self, *args)
    def resize(self, *args): return _CCMC.vector_float_resize(self, *args)
    def insert(self, *args): return _CCMC.vector_float_insert(self, *args)
    def reserve(self, *args): return _CCMC.vector_float_reserve(self, *args)
    def capacity(self): return _CCMC.vector_float_capacity(self)
    __swig_destroy__ = _CCMC.delete_vector_float
    __del__ = lambda self : None;
vector_float_swigregister = _CCMC.vector_float_swigregister
vector_float_swigregister(vector_float)

class vector_fieldline(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_fieldline, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_fieldline, name)
    __repr__ = _swig_repr
    def iterator(self): return _CCMC.vector_fieldline_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _CCMC.vector_fieldline___nonzero__(self)
    def __bool__(self): return _CCMC.vector_fieldline___bool__(self)
    def __len__(self): return _CCMC.vector_fieldline___len__(self)
    def pop(self): return _CCMC.vector_fieldline_pop(self)
    def __getslice__(self, *args): return _CCMC.vector_fieldline___getslice__(self, *args)
    def __setslice__(self, *args): return _CCMC.vector_fieldline___setslice__(self, *args)
    def __delslice__(self, *args): return _CCMC.vector_fieldline___delslice__(self, *args)
    def __delitem__(self, *args): return _CCMC.vector_fieldline___delitem__(self, *args)
    def __getitem__(self, *args): return _CCMC.vector_fieldline___getitem__(self, *args)
    def __setitem__(self, *args): return _CCMC.vector_fieldline___setitem__(self, *args)
    def append(self, *args): return _CCMC.vector_fieldline_append(self, *args)
    def empty(self): return _CCMC.vector_fieldline_empty(self)
    def size(self): return _CCMC.vector_fieldline_size(self)
    def clear(self): return _CCMC.vector_fieldline_clear(self)
    def swap(self, *args): return _CCMC.vector_fieldline_swap(self, *args)
    def get_allocator(self): return _CCMC.vector_fieldline_get_allocator(self)
    def begin(self): return _CCMC.vector_fieldline_begin(self)
    def end(self): return _CCMC.vector_fieldline_end(self)
    def rbegin(self): return _CCMC.vector_fieldline_rbegin(self)
    def rend(self): return _CCMC.vector_fieldline_rend(self)
    def pop_back(self): return _CCMC.vector_fieldline_pop_back(self)
    def erase(self, *args): return _CCMC.vector_fieldline_erase(self, *args)
    def __init__(self, *args): 
        this = _CCMC.new_vector_fieldline(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _CCMC.vector_fieldline_push_back(self, *args)
    def front(self): return _CCMC.vector_fieldline_front(self)
    def back(self): return _CCMC.vector_fieldline_back(self)
    def assign(self, *args): return _CCMC.vector_fieldline_assign(self, *args)
    def resize(self, *args): return _CCMC.vector_fieldline_resize(self, *args)
    def insert(self, *args): return _CCMC.vector_fieldline_insert(self, *args)
    def reserve(self, *args): return _CCMC.vector_fieldline_reserve(self, *args)
    def capacity(self): return _CCMC.vector_fieldline_capacity(self)
    __swig_destroy__ = _CCMC.delete_vector_fieldline
    __del__ = lambda self : None;
vector_fieldline_swigregister = _CCMC.vector_fieldline_swigregister
vector_fieldline_swigregister(vector_fieldline)

class vector_int(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_int, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_int, name)
    __repr__ = _swig_repr
    def iterator(self): return _CCMC.vector_int_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _CCMC.vector_int___nonzero__(self)
    def __bool__(self): return _CCMC.vector_int___bool__(self)
    def __len__(self): return _CCMC.vector_int___len__(self)
    def pop(self): return _CCMC.vector_int_pop(self)
    def __getslice__(self, *args): return _CCMC.vector_int___getslice__(self, *args)
    def __setslice__(self, *args): return _CCMC.vector_int___setslice__(self, *args)
    def __delslice__(self, *args): return _CCMC.vector_int___delslice__(self, *args)
    def __delitem__(self, *args): return _CCMC.vector_int___delitem__(self, *args)
    def __getitem__(self, *args): return _CCMC.vector_int___getitem__(self, *args)
    def __setitem__(self, *args): return _CCMC.vector_int___setitem__(self, *args)
    def append(self, *args): return _CCMC.vector_int_append(self, *args)
    def empty(self): return _CCMC.vector_int_empty(self)
    def size(self): return _CCMC.vector_int_size(self)
    def clear(self): return _CCMC.vector_int_clear(self)
    def swap(self, *args): return _CCMC.vector_int_swap(self, *args)
    def get_allocator(self): return _CCMC.vector_int_get_allocator(self)
    def begin(self): return _CCMC.vector_int_begin(self)
    def end(self): return _CCMC.vector_int_end(self)
    def rbegin(self): return _CCMC.vector_int_rbegin(self)
    def rend(self): return _CCMC.vector_int_rend(self)
    def pop_back(self): return _CCMC.vector_int_pop_back(self)
    def erase(self, *args): return _CCMC.vector_int_erase(self, *args)
    def __init__(self, *args): 
        this = _CCMC.new_vector_int(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _CCMC.vector_int_push_back(self, *args)
    def front(self): return _CCMC.vector_int_front(self)
    def back(self): return _CCMC.vector_int_back(self)
    def assign(self, *args): return _CCMC.vector_int_assign(self, *args)
    def resize(self, *args): return _CCMC.vector_int_resize(self, *args)
    def insert(self, *args): return _CCMC.vector_int_insert(self, *args)
    def reserve(self, *args): return _CCMC.vector_int_reserve(self, *args)
    def capacity(self): return _CCMC.vector_int_capacity(self)
    __swig_destroy__ = _CCMC.delete_vector_int
    __del__ = lambda self : None;
vector_int_swigregister = _CCMC.vector_int_swigregister
vector_int_swigregister(vector_int)



