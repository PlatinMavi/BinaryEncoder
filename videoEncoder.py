import FileEncoder
from PIL import Image
import pixelColor
import os
import re
import cv2

class VideoGenerator():
    def __init__(self) -> None:
        self.imagesize = 256
        self.fps = 24

    def BreakChunks(self):
        encoded_string, out = FileEncoder.FileEncoder().EncodeFile()
        encoded_string = encoded_string.split(".")
        encoded_str = encoded_string[0]
        extension = encoded_string[-1]
        n = 1
        encoded_list = [encoded_str[i * n:(i + 1) * n] for i in range((len(encoded_str) + n - 1) // n )]
        chunks = []
        
        for x in range(1,(len(encoded_list)//self.imagesize)+1):
            i = 0
            chunk = ""
            while i < self.imagesize:
                chunk = chunk+encoded_list[i*x]
                i = i+1
            chunks.append(chunk)

        leftovercount = len(encoded_list)-len(chunks)*256
        if leftovercount == 0:
            pass
        else:
            lastchunk=""
            for x in range(len(chunks)*self.imagesize,len(encoded_list)):
                lastchunk=lastchunk+encoded_list[x]
            chunks.append(lastchunk)

        
        print((len(chunks)-2)*self.imagesize,len(encoded_list),len(lastchunk))
        return chunks
    
    def GenerateImages(self):
        chunks = self.BreakChunks()
        i = 1
        for x in chunks:
            n = 1
            chunk = [x[i * n:(i + 1) * n] for i in range((len(x) + n - 1) // n )]
            image = Image.new("RGB", (16, 16), color="white")
            width, height = image.size

            mistakecount = 0
            chunkindex = 0
            try:
                for x in range(width):
                    for y in range(height):
                        image.putpixel((x, y), pixelColor.GetRGB(chunk[chunkindex]))
                        chunkindex = chunkindex+1
            except:
                if mistakecount == 1:
                    mistakecount = mistakecount+1
                    return None
                else:
                    pass
            image.save("C:/Users/PC/Desktop/BinaryEncoder/TempImages/"+str(i)+".png")
            i=i+1

    def natural_sort_key(self,s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

    def TurnIntoVideo(self):
        images_directory = "C:/Users/PC/Desktop/BinaryEncoder/TempImages"
        output_video_path = "C:/Users/PC/Desktop/BinaryEncoder/output/output.mp4"
        image_files = os.listdir(images_directory)
        image_files.sort(key=self.natural_sort_key)  # Sort the filenames in numerical order

        first_image_path = os.path.join(images_directory, image_files[0])
        first_image = cv2.imread(first_image_path)
        height, width, _ = first_image.shape

        # Initialize video writer with the same resolution as the images (16x16)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use mp4v codec
        video_writer = cv2.VideoWriter(output_video_path, fourcc, self.fps, (width, height), isColor=True)

        # Write images to video
        for image_file in image_files:
            image_path = os.path.join(images_directory, image_file)
            image = cv2.imread(image_path)
            video_writer.write(image)

        # Release video writer and close the video file
        video_writer.release()



    
vg = VideoGenerator()
print(vg.TurnIntoVideo())