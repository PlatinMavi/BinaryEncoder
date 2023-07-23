import os
import EncoderDecoder

class FileEncoder():
    
    def GetFile(self):
        path = "C:/Users/PC/Desktop/BinaryEncoder/input/"
        file = os.listdir(path)[0]
        newpath = os.path.join(path, file)
        output = "C:/Users/PC/Desktop/BinaryEncoder/output/output.txt"
        return newpath, output
    
    def EncodeFile(self):
        filepath, output = self.GetFile()
        extension = "."+filepath.split(".")[-1]
        
        with open(filepath, 'rb') as file:
            binary_data = file.read()
            binary_string = ''.join(format(byte, '08b') for byte in binary_data)
            n = 8
            binary_list = [binary_string[i * n:(i + 1) * n] for i in range((len(binary_string) + n - 1) // n )]

            key_str = ""
            for x in binary_list:
                key = EncoderDecoder.GetKey(x)
                key_str = key_str+key
                
        return key_str+extension, output
    
    def SaveEncode(self):
        encodedData, output = self.EncodeFile()

        with open(output,"wt") as file:
            file.write(encodedData)