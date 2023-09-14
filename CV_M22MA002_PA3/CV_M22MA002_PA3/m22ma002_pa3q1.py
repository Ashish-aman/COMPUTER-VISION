# -*- coding: utf-8 -*-
"""M22MA002_PA3Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XcIhPg0FcpNoP7DbTM_od-6Mfm1pH4qb
"""

import cv2 as cv
import numpy as np
import os
from google.colab.patches import cv2_imshow
from sklearn.decomposition import PCA
from google.colab.patches import cv2_imshow
from skimage.metrics import structural_similarity as ssim

from google.colab import drive
drive.mount('/content/drive')

!unzip -qq /content/drive/MyDrive/face-lfw-train.zip

# import glob
# path = "/content/face-lfw-train"
# for file in glob.glob(path):
#    print(file)
#    a= cv.imread(file)
#    print(a)

import glob 
img_dir = "/content/face-lfw-train" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
train_data = [] 
for f1 in files: 
    img = cv.imread(f1) 
    train_data.append(img)

img1=cv.imread("/content/drive/MyDrive/msdhoni.jfif")
train_data.append(img1)
train_data=np.asarray(train_data)

train_data.shape

train_set=[]
for i in range(train_data.shape[0]):
  grayImage = cv.cvtColor(train_data[i], cv.COLOR_BGR2GRAY)
  grayImage= cv.resize(grayImage, (100, 100))
 
  train_set.append(grayImage)

train_set=np.asarray(train_set)

train_set=train_set.reshape(train_set.shape[0],-1)
# train_set = train_set.astype('float32') / 255.0
train_set.shape
# train_set[0].shape

# train_set=train_set.reshape(64*64,1)
mean=np.mean(train_set,axis=0)
# print(mean)
print(mean.shape)
reshape_mean=mean.reshape(100,100)
cv2_imshow(reshape_mean)

# phi=[]
# for i in range(train_set.shape[0]):
#     diff=np.subtract(train_set[i,:],mean)
#     phi.append(diff)
#     print(diff.shape)

diff=train_set-mean
print(diff.shape)

cv2_imshow(diff[0].reshape(100,100))

# for i in range(train_set.shape[0]):
# phi=np.asarray(phi)
# print(phi.shape)
# cov=(np.dot(diff.T,diff.T))
# print(cov.shape)
cov=(np.dot(diff.T,diff))/12

cov.shape

# Initialize a PCA object
pca = PCA(n_components=100)

# Fit the PCA object to the covariance matrix
pca.fit(cov)
num_eigenface=11
# Extract the top K Eigenfaces
eigenfaces = pca.components_[:11]
# cv2_imshow(eigenfaces)

# Reshape the Eigenfaces to their original size
eigenfaces1 = eigenfaces.reshape((11, 100,100))

import matplotlib.pyplot as plt
print(eigenfaces1.shape)
print(eigenfaces1[0].shape)
plt.imshow(eigenfaces1[5],cmap='gray')

#TOP 5 EIGEN FACES OF THE TRAINING SET
K = 5
fig, axes = plt.subplots(1, K, figsize=(10, 4))
for i in range(K):
    axes[i].imshow(eigenfaces1[i].reshape(100,100), cmap='gray')
    axes[i].axis('off')
plt.suptitle(f'Top {K} Eigenfaces')
plt.show()

test_image=cv.imread("/content/drive/MyDrive/msdhoni.jfif")
testimage1= cv.cvtColor(test_image, cv.COLOR_RGB2GRAY)
test_img1=cv.resize(testimage1,(100,100))
test_img=test_img1.reshape(1,-1)

mean_test=np.mean(test_img)

diff_test=test_img-mean

#here we have to take dot product of the obtained eigen faces and the diff_test of the tested image
# to take out the projection of the new image
dot_test=np.dot(diff_test,eigenfaces.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

#Considering the different value of k i.e. different eigen faces 
eigenfaces2=eigenfaces[:2]
print(eigenfaces2.shape)
dot_test=np.dot(diff_test,eigenfaces2.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces2)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

eigenfaces3=eigenfaces[:3]
print(eigenfaces3.shape)
dot_test=np.dot(diff_test,eigenfaces3.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces3)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

eigenfaces5=eigenfaces[:5]
print(eigenfaces5.shape)
dot_test=np.dot(diff_test,eigenfaces5.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces5)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

eigenfaces7=eigenfaces[:7]
print(eigenfaces7.shape)
dot_test=np.dot(diff_test,eigenfaces7.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces7)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

eigenfaces9=eigenfaces[:9]
print(eigenfaces5.shape)
dot_test=np.dot(diff_test,eigenfaces9.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces9)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

eigenfaces12=eigenfaces[:12]
print(eigenfaces12.shape)
dot_test=np.dot(diff_test,eigenfaces12.T)
print(dot_test.shape)
# print(dot_test.shape)
# distances = np.linalg.norm(cov - dot_test, axis=1)
reg_img=np.dot(dot_test,eigenfaces12)
reg_img.shape
reconstd_img=reg_img.reshape(100,100)
plt.imshow(reconstd_img,cmap='gray')

cv2_imshow(test_image)
test_image.shape

colour_testimg = cv.cvtColor(testimage1, cv.COLOR_GRAY2RGB)

cv2_imshow(reconstd_img)

for i in range(1,12):
  eigenface_k=eigenfaces[:i]
  dot_test=np.dot(diff_test,eigenface_k.T)
  print(dot_test.shape)
  # print(dot_test.shape)
  # distances = np.linalg.norm(cov - dot_test, axis=1)
  reg_img=np.dot(dot_test,eigenface_k)
  reg_img.shape
  reconstd_img=reg_img.reshape(100,100)
  # Calculate MSE
  mse = np.mean((reconstd_img - test_img1)**2)

  print(f"Mean Squared Error (MSE):{mse:.4f} for the output image using the eigen faces k={i}")
  # print(f"Confusion matrix for the reconst image using k ={i} eigen faces")
  print("-----------------------------")
  # Calculate SSIM
  ssim_score = ssim(test_img1, reconstd_img, data_range=reconstd_img.max() - reconstd_img.min())

  print("Structural Similarity Index (SSIM):", ssim_score)
  # print(confmat)
  print(f"Value of k (eigen faces) ={i}")
  cv2_imshow(reconstd_img)

