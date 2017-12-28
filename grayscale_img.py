import numpy as np
from PIL import Image
image_test = Image.open('images/rick_morty.jpg')
# image_test.show()


# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


# converts an image to grayscale
def convert_grayscale(image):
    width, height = image.size

    # new image to store our converted image
    newPic  = create_image(width, height)
    pixels  = newPic.load()

    # convert to grayscale
    # Get Pixel
    for i in range(width):
        for j in range(height):
            pixel = get_pixel(image, i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # Transform to grayscale
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    # Return new image
    return newPic


image_test  = convert_grayscale(image_test)

image_test.show()

# print(pixel)

# numbers = np.arange(10)
# print(numbers)

# filetest    = open('number_one_test.txt', 'a')
# for num in numbers:
#     filetest.write()
#     filetest.write('\n')
# filetest.close()
# print(filetest)