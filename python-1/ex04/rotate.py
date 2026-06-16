import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def rotate_image() -> None:
    """Loads an image, crops it, transposes it manually, and saves the result."""
    try:
        path = "animal.jpeg"
        img_array = ft_load(path)
        if img_array is None:
            return

        zoomed_array = img_array[100:500, 450:850, 0:1]
        height, width, channels = zoomed_array.shape

        print(f"The shape of image is: {zoomed_array.shape}")
        print(zoomed_array)

        transpose_matrix = np.zeros(
            (width, height, channels), dtype=zoomed_array.dtype
        )

        for h in range(height):
            for w in range(width):
                transpose_matrix[w][h] = zoomed_array[h][w]

        rotated_image_2d = transpose_matrix[:, :, 0]

        print(f"The shape after Transpose: {rotated_image_2d.shape}")
        print(rotated_image_2d)

        plt.imshow(rotated_image_2d, cmap="gray")
        plt.axis("on")
        plt.savefig("animal_rotated.jpeg", bbox_inches="tight")
        plt.close()
        print("Success: Image saved as 'animal_rotated.jpeg'")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    rotate_image()