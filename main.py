import FileDecoder
import FileEncoder

option = input("1: Encode\n2:Decode\nPlease select the option to procces for input: ")

if option == "1":
    FileEncoder.FileEncoder().SaveEncode()
elif option == "2":
    FileDecoder.FileDecoder().SaveFile()
else:
    print("Please put the right input")