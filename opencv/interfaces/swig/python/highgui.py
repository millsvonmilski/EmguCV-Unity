# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
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
            fp, pathname, description = imp.find_module('_highgui', [dirname(__file__)])
        except ImportError:
            import _highgui
            return _highgui
        if fp is not None:
            try:
                _mod = imp.load_module('_highgui', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _highgui = swig_import_helper()
    del swig_import_helper
else:
    import _highgui
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


class CvRNG_Wrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvRNG_Wrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvRNG_Wrapper, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _highgui.new_CvRNG_Wrapper(*args)
        try: self.this.append(this)
        except: self.this = this
    def ptr(self): return _highgui.CvRNG_Wrapper_ptr(self)
    def ref(self): return _highgui.CvRNG_Wrapper_ref(self)
    def __eq__(self, *args): return _highgui.CvRNG_Wrapper___eq__(self, *args)
    def __ne__(self, *args): return _highgui.CvRNG_Wrapper___ne__(self, *args)
    __swig_destroy__ = _highgui.delete_CvRNG_Wrapper
    __del__ = lambda self : None;
CvRNG_Wrapper_swigregister = _highgui.CvRNG_Wrapper_swigregister
CvRNG_Wrapper_swigregister(CvRNG_Wrapper)

class CvSubdiv2DEdge_Wrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSubdiv2DEdge_Wrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSubdiv2DEdge_Wrapper, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _highgui.new_CvSubdiv2DEdge_Wrapper(*args)
        try: self.this.append(this)
        except: self.this = this
    def ptr(self): return _highgui.CvSubdiv2DEdge_Wrapper_ptr(self)
    def ref(self): return _highgui.CvSubdiv2DEdge_Wrapper_ref(self)
    def __eq__(self, *args): return _highgui.CvSubdiv2DEdge_Wrapper___eq__(self, *args)
    def __ne__(self, *args): return _highgui.CvSubdiv2DEdge_Wrapper___ne__(self, *args)
    __swig_destroy__ = _highgui.delete_CvSubdiv2DEdge_Wrapper
    __del__ = lambda self : None;
CvSubdiv2DEdge_Wrapper_swigregister = _highgui.CvSubdiv2DEdge_Wrapper_swigregister
CvSubdiv2DEdge_Wrapper_swigregister(CvSubdiv2DEdge_Wrapper)

cvReleaseCapture = _highgui.delete_CvCapture

cvReleaseVideoWriter = _highgui.delete_CvVideoWriter


def cvRetrieveFrame(*args):
  """cvRetrieveFrame(CvCapture capture) -> CvMat"""
  return _highgui.cvRetrieveFrame(*args)

def cvQueryFrame(*args):
  """cvQueryFrame(CvCapture capture) -> CvMat"""
  return _highgui.cvQueryFrame(*args)

def cvInitSystem(*args):
  """cvInitSystem(int argc, char argv) -> int"""
  return _highgui.cvInitSystem(*args)

def cvStartWindowThread():
  """cvStartWindowThread() -> int"""
  return _highgui.cvStartWindowThread()
CV_WINDOW_AUTOSIZE = _highgui.CV_WINDOW_AUTOSIZE

def cvNamedWindow(*args):
  """cvNamedWindow(char name, int flags = 1) -> int"""
  return _highgui.cvNamedWindow(*args)

def cvShowImage(*args):
  """cvShowImage(char name, CvArr image)"""
  return _highgui.cvShowImage(*args)

def cvResizeWindow(*args):
  """cvResizeWindow(char name, int width, int height)"""
  return _highgui.cvResizeWindow(*args)

def cvMoveWindow(*args):
  """cvMoveWindow(char name, int x, int y)"""
  return _highgui.cvMoveWindow(*args)

def cvDestroyWindow(*args):
  """cvDestroyWindow(char name)"""
  return _highgui.cvDestroyWindow(*args)

def cvDestroyAllWindows():
  """cvDestroyAllWindows()"""
  return _highgui.cvDestroyAllWindows()

def cvGetWindowHandle(*args):
  """cvGetWindowHandle(char name) -> void"""
  return _highgui.cvGetWindowHandle(*args)

def cvGetWindowName(*args):
  """cvGetWindowName(void window_handle) -> char"""
  return _highgui.cvGetWindowName(*args)

def cvCreateTrackbar(*args):
  """
    cvCreateTrackbar(char trackbar_name, char window_name, int value, int count, 
        CvTrackbarCallback on_change) -> int
    """
  return _highgui.cvCreateTrackbar(*args)

def cvCreateTrackbar2(*args):
  """
    cvCreateTrackbar2(char trackbar_name, char window_name, int value, int count, 
        CvTrackbarCallback2 on_change, void userdata = None) -> int
    """
  return _highgui.cvCreateTrackbar2(*args)

def cvGetTrackbarPos(*args):
  """cvGetTrackbarPos(char trackbar_name, char window_name) -> int"""
  return _highgui.cvGetTrackbarPos(*args)

def cvSetTrackbarPos(*args):
  """cvSetTrackbarPos(char trackbar_name, char window_name, int pos)"""
  return _highgui.cvSetTrackbarPos(*args)
CV_EVENT_MOUSEMOVE = _highgui.CV_EVENT_MOUSEMOVE
CV_EVENT_LBUTTONDOWN = _highgui.CV_EVENT_LBUTTONDOWN
CV_EVENT_RBUTTONDOWN = _highgui.CV_EVENT_RBUTTONDOWN
CV_EVENT_MBUTTONDOWN = _highgui.CV_EVENT_MBUTTONDOWN
CV_EVENT_LBUTTONUP = _highgui.CV_EVENT_LBUTTONUP
CV_EVENT_RBUTTONUP = _highgui.CV_EVENT_RBUTTONUP
CV_EVENT_MBUTTONUP = _highgui.CV_EVENT_MBUTTONUP
CV_EVENT_LBUTTONDBLCLK = _highgui.CV_EVENT_LBUTTONDBLCLK
CV_EVENT_RBUTTONDBLCLK = _highgui.CV_EVENT_RBUTTONDBLCLK
CV_EVENT_MBUTTONDBLCLK = _highgui.CV_EVENT_MBUTTONDBLCLK
CV_EVENT_FLAG_LBUTTON = _highgui.CV_EVENT_FLAG_LBUTTON
CV_EVENT_FLAG_RBUTTON = _highgui.CV_EVENT_FLAG_RBUTTON
CV_EVENT_FLAG_MBUTTON = _highgui.CV_EVENT_FLAG_MBUTTON
CV_EVENT_FLAG_CTRLKEY = _highgui.CV_EVENT_FLAG_CTRLKEY
CV_EVENT_FLAG_SHIFTKEY = _highgui.CV_EVENT_FLAG_SHIFTKEY
CV_EVENT_FLAG_ALTKEY = _highgui.CV_EVENT_FLAG_ALTKEY

def cvSetMouseCallbackOld(*args):
  """cvSetMouseCallbackOld(char window_name, CvMouseCallback on_mouse, void param = None)"""
  return _highgui.cvSetMouseCallbackOld(*args)
CV_LOAD_IMAGE_UNCHANGED = _highgui.CV_LOAD_IMAGE_UNCHANGED
CV_LOAD_IMAGE_GRAYSCALE = _highgui.CV_LOAD_IMAGE_GRAYSCALE
CV_LOAD_IMAGE_COLOR = _highgui.CV_LOAD_IMAGE_COLOR
CV_LOAD_IMAGE_ANYDEPTH = _highgui.CV_LOAD_IMAGE_ANYDEPTH
CV_LOAD_IMAGE_ANYCOLOR = _highgui.CV_LOAD_IMAGE_ANYCOLOR

def cvLoadImageM(*args):
  """cvLoadImageM(char filename, int iscolor = 1) -> CvMat"""
  return _highgui.cvLoadImageM(*args)
CV_IMWRITE_JPEG_QUALITY = _highgui.CV_IMWRITE_JPEG_QUALITY
CV_IMWRITE_PNG_COMPRESSION = _highgui.CV_IMWRITE_PNG_COMPRESSION
CV_IMWRITE_PXM_BINARY = _highgui.CV_IMWRITE_PXM_BINARY

def cvSaveImage(*args):
  """cvSaveImage(char filename, CvArr image, int params = None) -> int"""
  return _highgui.cvSaveImage(*args)

def cvDecodeImage(*args):
  """cvDecodeImage(CvMat buf, int iscolor = 1)"""
  return _highgui.cvDecodeImage(*args)

def cvDecodeImageM(*args):
  """cvDecodeImageM(CvMat buf, int iscolor = 1) -> CvMat"""
  return _highgui.cvDecodeImageM(*args)

def cvEncodeImage(*args):
  """cvEncodeImage(char ext, CvArr image, int params = None) -> CvMat"""
  return _highgui.cvEncodeImage(*args)
CV_CVTIMG_FLIP = _highgui.CV_CVTIMG_FLIP
CV_CVTIMG_SWAP_RB = _highgui.CV_CVTIMG_SWAP_RB

def cvConvertImage(*args):
  """cvConvertImage(CvArr src, CvArr dst, int flags = 0)"""
  return _highgui.cvConvertImage(*args)

def cvWaitKeyC(delay = 0):
  """cvWaitKeyC(int delay = 0) -> int"""
  return _highgui.cvWaitKeyC(delay)

def cvCreateFileCapture(*args):
  """cvCreateFileCapture(char filename) -> CvCapture"""
  return _highgui.cvCreateFileCapture(*args)
CV_CAP_ANY = _highgui.CV_CAP_ANY
CV_CAP_MIL = _highgui.CV_CAP_MIL
CV_CAP_VFW = _highgui.CV_CAP_VFW
CV_CAP_V4L = _highgui.CV_CAP_V4L
CV_CAP_V4L2 = _highgui.CV_CAP_V4L2
CV_CAP_FIREWARE = _highgui.CV_CAP_FIREWARE
CV_CAP_FIREWIRE = _highgui.CV_CAP_FIREWIRE
CV_CAP_IEEE1394 = _highgui.CV_CAP_IEEE1394
CV_CAP_DC1394 = _highgui.CV_CAP_DC1394
CV_CAP_CMU1394 = _highgui.CV_CAP_CMU1394
CV_CAP_STEREO = _highgui.CV_CAP_STEREO
CV_CAP_TYZX = _highgui.CV_CAP_TYZX
CV_TYZX_LEFT = _highgui.CV_TYZX_LEFT
CV_TYZX_RIGHT = _highgui.CV_TYZX_RIGHT
CV_TYZX_COLOR = _highgui.CV_TYZX_COLOR
CV_TYZX_Z = _highgui.CV_TYZX_Z
CV_CAP_QT = _highgui.CV_CAP_QT
CV_CAP_UNICAP = _highgui.CV_CAP_UNICAP
CV_CAP_DSHOW = _highgui.CV_CAP_DSHOW

def cvCreateCameraCapture(*args):
  """cvCreateCameraCapture(int index) -> CvCapture"""
  return _highgui.cvCreateCameraCapture(*args)

def cvGrabFrame(*args):
  """cvGrabFrame(CvCapture capture) -> int"""
  return _highgui.cvGrabFrame(*args)

def cvRetrieveFrame__Deprecated(*args):
  """cvRetrieveFrame__Deprecated(CvCapture capture, int streamIdx = 0)"""
  return _highgui.cvRetrieveFrame__Deprecated(*args)

def cvQueryFrame__Deprecated(*args):
  """cvQueryFrame__Deprecated(CvCapture capture)"""
  return _highgui.cvQueryFrame__Deprecated(*args)
CV_CAP_PROP_POS_MSEC = _highgui.CV_CAP_PROP_POS_MSEC
CV_CAP_PROP_POS_FRAMES = _highgui.CV_CAP_PROP_POS_FRAMES
CV_CAP_PROP_POS_AVI_RATIO = _highgui.CV_CAP_PROP_POS_AVI_RATIO
CV_CAP_PROP_FRAME_WIDTH = _highgui.CV_CAP_PROP_FRAME_WIDTH
CV_CAP_PROP_FRAME_HEIGHT = _highgui.CV_CAP_PROP_FRAME_HEIGHT
CV_CAP_PROP_FPS = _highgui.CV_CAP_PROP_FPS
CV_CAP_PROP_FOURCC = _highgui.CV_CAP_PROP_FOURCC
CV_CAP_PROP_FRAME_COUNT = _highgui.CV_CAP_PROP_FRAME_COUNT
CV_CAP_PROP_FORMAT = _highgui.CV_CAP_PROP_FORMAT
CV_CAP_PROP_MODE = _highgui.CV_CAP_PROP_MODE
CV_CAP_PROP_BRIGHTNESS = _highgui.CV_CAP_PROP_BRIGHTNESS
CV_CAP_PROP_CONTRAST = _highgui.CV_CAP_PROP_CONTRAST
CV_CAP_PROP_SATURATION = _highgui.CV_CAP_PROP_SATURATION
CV_CAP_PROP_HUE = _highgui.CV_CAP_PROP_HUE
CV_CAP_PROP_GAIN = _highgui.CV_CAP_PROP_GAIN
CV_CAP_PROP_EXPOSURE = _highgui.CV_CAP_PROP_EXPOSURE
CV_CAP_PROP_CONVERT_RGB = _highgui.CV_CAP_PROP_CONVERT_RGB
CV_CAP_PROP_WHITE_BALANCE = _highgui.CV_CAP_PROP_WHITE_BALANCE
CV_CAP_PROP_RECTIFICATION = _highgui.CV_CAP_PROP_RECTIFICATION

def cvGetCaptureProperty(*args):
  """cvGetCaptureProperty(CvCapture capture, int property_id) -> double"""
  return _highgui.cvGetCaptureProperty(*args)

def cvSetCaptureProperty(*args):
  """cvSetCaptureProperty(CvCapture capture, int property_id, double value) -> int"""
  return _highgui.cvSetCaptureProperty(*args)

def cvGetCaptureDomain(*args):
  """cvGetCaptureDomain(CvCapture capture) -> int"""
  return _highgui.cvGetCaptureDomain(*args)

def CV_FOURCC(*args):
  """CV_FOURCC(char c1, char c2, char c3, char c4) -> int"""
  return _highgui.CV_FOURCC(*args)
CV_FOURCC_PROMPT = _highgui.CV_FOURCC_PROMPT

def cvCreateVideoWriter(*args):
  """
    cvCreateVideoWriter(char filename, int fourcc, double fps, CvSize frame_size, 
        int is_color = 1) -> CvVideoWriter
    """
  return _highgui.cvCreateVideoWriter(*args)

def cvWriteFrame(*args):
  """cvWriteFrame(CvVideoWriter writer,  image) -> int"""
  return _highgui.cvWriteFrame(*args)
HG_AUTOSIZE = _highgui.HG_AUTOSIZE
class CvvImage(_object):
    """Proxy of C++ CvvImage class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvvImage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvvImage, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(self) -> CvvImage"""
        this = _highgui.new_CvvImage()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _highgui.delete_CvvImage
    __del__ = lambda self : None;
    def Create(self, *args):
        """
        Create(self, int width, int height, int bits_per_pixel, int image_origin = 0) -> bool
        Create(self, int width, int height, int bits_per_pixel) -> bool
        """
        return _highgui.CvvImage_Create(self, *args)

    def Load(self, *args):
        """
        Load(self, char filename, int desired_color = 1) -> bool
        Load(self, char filename) -> bool
        """
        return _highgui.CvvImage_Load(self, *args)

    def LoadRect(self, *args):
        """LoadRect(self, char filename, int desired_color, CvRect r) -> bool"""
        return _highgui.CvvImage_LoadRect(self, *args)

    def Save(self, *args):
        """Save(self, char filename) -> bool"""
        return _highgui.CvvImage_Save(self, *args)

    def CopyOf(self, *args):
        """
        CopyOf(self, CvvImage image, int desired_color = -1)
        CopyOf(self, CvvImage image)
        CopyOf(self,  img, int desired_color = -1)
        CopyOf(self,  img)
        """
        return _highgui.CvvImage_CopyOf(self, *args)

    def GetImage(self):
        """GetImage(self)"""
        return _highgui.CvvImage_GetImage(self)

    def Destroy(self):
        """Destroy(self)"""
        return _highgui.CvvImage_Destroy(self)

    def Width(self):
        """Width(self) -> int"""
        return _highgui.CvvImage_Width(self)

    def Height(self):
        """Height(self) -> int"""
        return _highgui.CvvImage_Height(self)

    def Bpp(self):
        """Bpp(self) -> int"""
        return _highgui.CvvImage_Bpp(self)

    def Fill(self, *args):
        """Fill(self, int color)"""
        return _highgui.CvvImage_Fill(self, *args)

    def Show(self, *args):
        """Show(self, char window)"""
        return _highgui.CvvImage_Show(self, *args)

CvvImage_swigregister = _highgui.CvvImage_swigregister
CvvImage_swigregister(CvvImage)

def cvSetMouseCallback(*args):
  return _highgui.cvSetMouseCallback(*args)
cvSetMouseCallback = _highgui.cvSetMouseCallback

def cvWaitKey(delay = 0):
  return _highgui.cvWaitKey(delay)
cvWaitKey = _highgui.cvWaitKey

def cvLoadImage(*args):
  """
    cvLoadImage(char filename, int iscolor = 1) -> CvMat
    cvLoadImage(char filename) -> CvMat
    """
  return _highgui.cvLoadImage(*args)

class CvCapture(_object):
    """Proxy of C++ CvCapture class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvCapture, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvCapture, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _highgui.delete_CvCapture
    __del__ = lambda self : None;
CvCapture_swigregister = _highgui.CvCapture_swigregister
CvCapture_swigregister(CvCapture)

class CvVideoWriter(_object):
    """Proxy of C++ CvVideoWriter class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvVideoWriter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvVideoWriter, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _highgui.delete_CvVideoWriter
    __del__ = lambda self : None;
CvVideoWriter_swigregister = _highgui.CvVideoWriter_swigregister
CvVideoWriter_swigregister(CvVideoWriter)

__doc__ = """HighGUI provides minimalistic user interface parts and video input/output.

Dependent on the platform it was compiled on, this library provides methods
to draw a window for image display, capture video from a camera or framegrabber
or read/write video streams from/to the file system.

This wrapper was semi-automatically created from the C/C++ headers and therefore
contains no Python documentation. Because all identifiers are identical to their
C/C++ counterparts, you can consult the standard manuals that come with OpenCV.
"""




