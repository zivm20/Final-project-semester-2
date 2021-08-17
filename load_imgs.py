import cv2
import numpy as np
def load_imgs(file,size=100):
    pic = cv2.imread(file)
    pic = cv2.resize(pic,(size,size))
    flg = file.split(r"\\")[-1] 
    if flg.startswith("cat"):
        label = 0
    else:
        label = 1
    
    return [pic,label]
def process_frame(f, size=100):
    return f, load_imgs(f[0],f[1])
