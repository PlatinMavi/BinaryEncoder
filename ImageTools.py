import FileEncoder, FileDecoder
from PIL import Image
import pixelColor
import os
import re
import cv2

class ImageTools():

    def GenerateImage(self):
        encoded_string = FileEncoder.FileEncoder().EncodeFile(FileEncoder.FileEncoder().GetFile())
        encoded_string = encoded_string.split(".")
        encoded_str = encoded_string[0]
        extension = encoded_string[-1]
        n = 1
        encoded_list = [encoded_str[i * n:(i + 1) * n] for i in range((len(encoded_str) + n - 1) // n )]

        image = Image.new("RGB", (4, len(encoded_list)//4), color="white")
        width, height = image.size
        chunkindex = 0

        for x in range(width):
            for y in range(height):
                image.putpixel((x, y), pixelColor.GetRGB(encoded_list[chunkindex]))
                chunkindex = chunkindex+1
        image.save("C:/Users/PC/Desktop/BinaryEncoder/output/"+extension+".png")


    def DecodeImage(self, file):
        image = cv2.imread(file)
        height, width, _ = image.shape
        extension = file.split("/")[-1].split(".")[0]

        full = ""

        for y in range(width):  # Swap loop order to fix width and height
            for x in range(height):
                pixel_value = image[x, y]  # Swap x and y to fix pixel_value retrieval
                rgb = tuple(pixel_value)[::-1]
                encoded = pixelColor.GetKey(rgb)

                full = full + encoded

        FileDecoder.FileDecoder().SaveFile(full+"."+extension, "C:/Users/PC/Desktop/BinaryEncoder/output/output."+extension)

vg = ImageTools()
vg.GenerateImage()
# vg.DecodeImage("C:/Users/PC/Desktop/BinaryEncoder/input/png.png")