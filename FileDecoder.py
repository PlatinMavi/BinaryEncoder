import os
import EncoderDecoder

class FileDecoder():

    def GetFile(self):
        path = "C:/Users/PC/Desktop/BinaryEncoder/input/"
        file = os.listdir(path)[0]
        newpath = os.path.join(path, file)
        output = "C:/Users/PC/Desktop/BinaryEncoder/output/output."
        return newpath, output
    
    def DecodeFiletxt(self,file, outfilepath):
        binary_str = ""

        with open (file,"rt") as f:
            encoded_string = f.read().split(".")
            extension = encoded_string[-1]
            encoded_str = encoded_string[0]
            n = 2
            encoded_list = [encoded_str[i * n:(i + 1) * n] for i in range((len(encoded_str) + n - 1) // n )]
            for x in encoded_list:
                binary_str = binary_str+EncoderDecoder.GetBinary(x)

        return binary_str, outfilepath+extension
    
    def DecodeFile(self,file):
        binary_str = ""
        encoded_string = file.split(".")
        extension = encoded_string[-1]
        encoded_str = encoded_string[0]
        n = 2
        encoded_list = [encoded_str[i * n:(i + 1) * n] for i in range((len(encoded_str) + n - 1) // n )]
        for x in encoded_list:
            try:
                binary_str = binary_str+EncoderDecoder.GetBinary(x)
            except:
                pass
        return binary_str
    
    def SaveFile(self,file, filepath):
        binary_string = self.DecodeFile(file)

        bytes_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        int_list = [int(byte, 2) for byte in bytes_list]
        binary_data = bytes(int_list)

        with open(filepath, 'wb') as file:
            file.write(binary_data)
