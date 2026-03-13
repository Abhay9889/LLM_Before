import numpy as np
img = np.array([
[0,0,0,0,0],
[0,255,255,255,0],
[0,255,255,255,0],
[0,255,255,255,0],
[0,0,0,0,0]
], dtype=np.uint8)
print(img)
print(img.ndim)
print(img.shape)

# RGB img's have three prop. in shape fun (height,width,channels) 
#  ex- (5,5,3)
"""
Pixel = [R,G,B]
[255,0,0] → red
[0,255,0] → green
[0,0,255] → blue

"""

img1=np.zeros((5,5,3),dtype=np.uint8)
img1[2,2]=[255,0,0] # red pixels
print(img1)

#   total=5X5X3=75  --> R=255,G=0,B=0  
# now remaining 74 values are 0 and 1 value is 255
# mean=255/75=3.4

