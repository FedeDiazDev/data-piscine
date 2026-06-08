import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def zoom_image():
    """Loads animal.jpeg, applies a zoom slice, prints specs and displays it with scales."""
    try:
        path = "animal.jpeg"
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file '{path}' does not exist.")

        img = Image.open(path)
        img_rgb = img.convert("RGB")
        img_array = np.array(img_rgb)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
       
        zoomed_array = img_array[100:500, 400:800, 0:1]
        print(f"New shape after slicing: {zoomed_array.shape}")
        print(zoomed_array)

       
        if len(zoomed_array.shape) == 3 and zoomed_array.shape[2] == 1:
            plt.imshow(zoomed_array[:, :, 0], cmap="gray")
        else:
            plt.imshow(zoomed_array)
        plt.axis("on")
        plt.title("Zoomed Image")
        plt.savefig("animal_zoom.jpeg", bbox_inches='tight')
        print("Success: Image saved as 'animal_zoom.jpeg'")
        
        plt.close()

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    zoom_image()