import numpy as np
from PIL import Image


def display_image(array, title):
    """Displays a transformed image using the default image viewer."""
    try:
        Image.fromarray(array).show(title=title)
    except Exception:
        return


def ft_invert(array):
    """Inverts the colors of the image received."""
    if array is None:
        return None
    inverted = 255 - array
    display_image(inverted, "Invert")
    return inverted

def ft_red(array):
    """Keeps only the red channel of the image."""
    if array is None:
        return None
    red_filter = np.array([1, 0, 0], dtype=array.dtype)
    red = array * red_filter
    display_image(red, "Red")
    return red

def ft_green(array):
    """Keeps only the green channel of the image."""
    if array is None:
        return None
    green_img = array.copy()
    green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
    green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]
    display_image(green_img, "Green")
    return green_img

def ft_blue(array):
    """Keeps only the blue channel of the image."""
    if array is None:
        return None
    blue_img = array.copy()
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    display_image(blue_img, "Blue")
    return blue_img

def ft_grey(array):
    """Converts the image to grey while preserving a 3-channel shape."""
    if array is None:
        return None
    grey = np.mean(array, axis=2, keepdims=True).astype(array.dtype)
    grey_img = np.repeat(grey, 3, axis=2)
    display_image(grey_img, "Grey")
    return grey_img