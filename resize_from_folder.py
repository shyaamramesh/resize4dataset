import skimage
from skimage import io, transform
import os

print("Resize images to specified size from folder")

folder = input("Images Folder? ")
read = skimage.io.ImageCollection(folder + '/*.jpg')

prevFiles = os.listdir(folder)

height = int(input("Height? "))
width = int(input("Width? "))
print("Output File Name ?")
print("Example > 'dog'")
print("Output files will be > dog1.jpg,dog2.jpg...dog32.jpg,dog33.jpg")
fname = input(" ")

exists = os.path.isdir("Resized_Images")
if not exists:
	os.mkdir("Resized_Images")
		

for i in range(len(read)):
	resize = skimage.transform.resize(read[i], [height,width])
	skimage.io.imsave("Resized_Images/" + str(fname) + str(i)+'.jpg', resize)

print("Resized The Following Files: ")
print(prevFiles)
print("To Resized_Images Directory")
print("Done")
