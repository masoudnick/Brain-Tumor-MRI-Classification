import h5py as h5
import numpy as np
from PIL import Image
import os
import random

matfiles = os.listdir("brainTumorDataPublic")
size = 512, 512
index = 0

for file in matfiles:

	f = h5.File(os.path.join("brainTumorDataPublic",file),"r")

	image = np.array(f['/cjdata/image'])
	label = int(np.array(f['/cjdata/label'])[0][0])

	print(int(label),image.shape)
	rescaled = (255.0 / image.max() * (image - image.min())).astype(np.uint8)
	im = Image.fromarray(rescaled)
	
	if image.shape[0] != 512 or image.shape[1] != 512:
		im.thumbnail(size, Image.ANTIALIAS)
		
	folder = ""
	if label == 1:
		folder = "meningioma"
	elif label == 2:
		folder = "glioma"
	elif label == 3:
		folder = "pituitary"
		
	rotated = im.rotate(-90)

	filename = folder+'-'+str(index)+".jpg"
	
	rotated.save(os.path.join(folder,filename))
	index+=1
