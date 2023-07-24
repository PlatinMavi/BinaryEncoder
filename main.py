import ImageTools

__name__ == "__main__"

option = input("1: Encode\n2:Decode\nPlease select the option to procces for input: ")

if option == "1":
    ImageTools.ImageTools().GenerateImage()
elif option == "2":
    ImageTools.ImageTools().DecodeImage()
else:
    print("Please put the right input")