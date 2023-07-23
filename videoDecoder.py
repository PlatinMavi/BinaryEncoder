import os
import cv2
import pixelColor
import FileDecoder

class VideoDecoder():
    def GetFile(self):
        path = "C:/Users/PC/Desktop/BinaryEncoder/input/"
        file = os.listdir(path)[0]
        newpath = os.path.join(path, file)
        output = "C:/Users/PC/Desktop/BinaryEncoder/videooutput/"
        return newpath, output
    
    def extract_frames_from_video(self):
        video_path, output_directory = self.GetFile()
        video_capture = cv2.VideoCapture(video_path)
        if not video_capture.isOpened():
            print("Error: Unable to open the video file.")
            return
        os.makedirs(output_directory, exist_ok=True)
        frame_count = 0
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            frame_filename = os.path.join(output_directory, f"{frame_count:04d}.png")
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite(frame_filename, frame_rgb)
            frame_count += 1
        video_capture.release()
        print(f"{frame_count} frames extracted and saved to {output_directory}.")

class ImageDecoder():
    def GetFile(self):
        path = "C:/Users/PC/Desktop/BinaryEncoder/input/"
        file = os.listdir(path)[0]
        newpath = os.path.join(path, file)
        output = file.split(".")[-1]
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

        FileDecoder.FileDecoder().SaveFile()


id = ImageDecoder()
print(id.DecodeImage())
    
# vd = VideoDecoder()
# print(vd.extract_frames_from_video())