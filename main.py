import ImageTools

__name__ == "__main__"

option = input("1: Encode\n2: Decode\nPlease select the option to procces for input: ")

if option == "1":
    print("Proccesing...")
    ImageTools.ImageTools().GenerateImage()
elif option == "2":
    print("Proccesing...")
    ImageTools.ImageTools().DecodeImage()
else:
    print("Please put the right input")