import cv2
import os
import numpy as np
from scipy.stats import skew
import pandas as pd
path1 = "./input/test/"
images = []
image_name = []

def stats_moment(image):
        noise = image - cv2.fastNlMeansDenoising(image)
        b,g,r = cv2.split(noise)
        sb = cv2.meanStdDev(b)
        sg = cv2.meanStdDev(g)
        sr = cv2.meanStdDev(r)
        return np.ndarray.flatten(np.matrix.transpose(np.asarray([sr[0][0],sr[1][0],[skew(np.ravel(r))],sg[0][0],sg[1][0],[skew(np.ravel(g))],sb[0][0],sb[1][0],[skew(np.ravel(b))]])))




def load_images_from_folder(folder):
    c = 0
    print(folder)
    for filename in os.listdir(folder):

        images.append(stats_moment(cv2.imread(os.path.join(folder,filename))))
        image_name.append(filename)
        print(filename)
        c = c + 1
        print(c)





load_images_from_folder(path1)
my_df = pd.DataFrame(images)
df = pd.DataFrame(image_name)
my_df.to_csv('test_noise.csv', index=False, header=False)
df.to_csv('test_name.csv', index=False, header=False)

