# BinaryEncoder

This Projects main goal was to create my own binary encoding system, and then encode pixels into a png file.<br />
There is 32 encoding characters that seperates as 16 lowercase, 16 uppercase. <br />
Files encode as 8 bit, 01010101 = aA, then every character is being painted in its own rgb representation<br />

# Executing
Please delete placeholder.txt before running.<br />
Put your input in input folder, then run main.py, remember to put only 1 file in input. <br />

# For inspection
pixelColor.py and EncoderDecoder.py is a mapping that holds encoding pattern.<br />
FileDecoder.py and FileEncoder.py is responsible for encoding and decoding.<br />
ImageTools.py encodes images, and decodes images<br />
main.py For executing Program<br />