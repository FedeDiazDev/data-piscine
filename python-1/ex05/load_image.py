from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Loads an image, displays its format and shape, and returns its RGB pixel array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image data as a NumPy array, or None if an error occurs.
    """
    try:
        img = Image.open(path)
        if img.format not in ["JPEG", "MPO"]:
            raise ValueError("Unsupported image format. Only JPG and JPEG are allowed.")
        img_rgb = img.convert("RGB")
        img_array = np.array(img_rgb)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        return img_array
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
        return None
    except Exception as error:
        print(f"Error: {error}")
        return None
    