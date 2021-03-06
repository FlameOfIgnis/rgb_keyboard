
class LightingMode():
    """ Enum class for different lighting methods and their corresponding values
    """
    BREATHING       = b"\x02" 
    WAVE            = b"\x03"
    TOUCH           = b"\x04" 
    RAINBOW         = b"\x05"
    RIPPLE          = b"\x06"
    SNAKE           = b"\x09"
    RAINDROP        = b"\x0a"
    AURORA          = b"\x0e"
    FIRECRACKER     = b"\x11"
    FLAT_COLOR      = b"\x33"


class ExtendedModes():
    """ Custom coded effects, done with repeatedly setting flat colors
    """
    RAINBOW_FADE    = "rainbow_fade"
    MUSIC           = "audio_visualizer"
