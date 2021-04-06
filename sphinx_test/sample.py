def sample(val):
    """A sample function.

    Args:
        val (str): A text string
    """
    return val


class RpictOptions():
    """rpict command options."""
    def __init__(self, vt=None, vp=None):
        self._vt = vt
        self._vp = vp
        
    @property
    def vt(self):
        """view type perspective - default: vtv

        *   'v' sets a perspective view.
        *   'l' sets parallel view.
        *   c' sets a cylindrical panaroma. This view is like a standard perspective
            vertically, but projected on a cylinder horizontally, like a soupcan's
            eye-view.
        *   'h' sets a hemispherical fisheye view. This is a projection of the hemisphere
            onto a circle. The maximum view angle for this type is 180 degrees.
        *   'a' sets an angular fisheye view. An angular fisheye view is defined such
            that distance from the center of the image is proportional to the angle
            from the central view direction. An angular fisheye can display a full 360
            degrees.
        *   's' sets a planisphere (stereographic) view. A planisphere fisheye view
            maintains angular relationships between lines, and is commonly used for
            sun path analysis. This is more commonly known as a stereographic projection.
        """
        return self._vt

    @vt.setter
    def vt(self, value):
        self._vt.value = value

    @property
    def vp(self):
        """view point - default value is 0.000000 0.000000 0.000000

        Set the view point to x y z . This is the focal point of a perspective
        view or the center of a parallel projection.
        """
        return self._vp

    @vp.setter
    def vp(self, value):
        self._vp.value = value
    