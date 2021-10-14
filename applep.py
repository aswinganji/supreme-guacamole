import hashlib

file = "Denoisedcar_Image.png"

with open(file,'rb') as f:
	file_data = f.read()


	imagehash = hashlib.sha256(file_data).hexdigest()

	print(imagehash)