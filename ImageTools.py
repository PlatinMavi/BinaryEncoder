import FileEncoder, FileDecoder
from PIL import Image
import pixelColor
import os
import re
import cv2

class ImageTools():

    def GenerateImage(self):
        encoded_string, out = FileEncoder.FileEncoder().EncodeFile()
        encoded_string = encoded_string.split(".")
        encoded_str = encoded_string[0]
        extension = encoded_string[-1]
        n = 1
        encoded_list = [encoded_str[i * n:(i + 1) * n] for i in range((len(encoded_str) + n - 1) // n )]

        image = Image.new("RGB", (8, len(encoded_list)//8), color="white")
        width, height = image.size
        chunkindex = 0

        for x in range(width):
            for y in range(height):
                image.putpixel((x, y), pixelColor.GetRGB(encoded_list[chunkindex]))
                chunkindex = chunkindex+1
        image.save("C:/Users/PC/Desktop/BinaryEncoder/outputpng/"+extension+".png")

    def GetFile(self):
        path = "C:/Users/PC/Desktop/BinaryEncoder/input/"
        file = os.listdir(path)[0]
        newpath = os.path.join(path, file)
        output = file.split(".")[0]
        return newpath, output

    def DecodeImage(self):
        file, out = self.GetFile()
        image = cv2.imread(file)
        height, width, _ = image.shape

        full = ""

        for y in range(width):  # Swap loop order to fix width and height
            for x in range(height):
                pixel_value = image[x, y]  # Swap x and y to fix pixel_value retrieval
                rgb = tuple(pixel_value)[::-1]
                encoded = pixelColor.GetKey(rgb)

                full = full + encoded

        FileDecoder.FileDecoder().SaveFile(full, "C:/Users/PC/Desktop/BinaryEncoder/output/output."+out)

vg = ImageTools()
vg.DecodeImage()