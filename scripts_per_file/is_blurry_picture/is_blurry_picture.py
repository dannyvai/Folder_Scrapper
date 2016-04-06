#Picture face reco
import file_ext_util
import cv2
import numpy as np
debug = False



def foreach_file_do(filepath,filename,file_ext,private_data):
    global debug
    if file_ext_util.is_picture(file_ext):
        image = cv2.imread(filepath)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image_laplacian_variance = cv2.Laplacian(image, cv2.CV_64F).var()

        if gray.mean() > 90 and  image_laplacian_variance < 100:
            print filepath,image_laplacian_variance, "Detected a blurry photo"

    return private_data