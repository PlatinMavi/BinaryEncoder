import FileDecoder
import FileEncoder
import ImageTools

__name__ == "__main__"

option = input("1: Encode\n2:Decode\nPlease select the option to procces for input: ")

if option == "1":
    FileEncoder.FileEncoder().SaveEncode(r"C:\Users\PC\Desktop\BinaryEncoder\input\test.png")
elif option == "2":
    FileDecoder.FileDecoder().SaveFile()
else:
    print("Please put the right input")