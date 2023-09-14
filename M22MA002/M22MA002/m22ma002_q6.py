# -*- coding: utf-8 -*-
"""M22MA002_Q6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Co9e0IT47CNsevuww3wLuZYlVzgODTiC
"""

import numpy as np
import cv2 as cv
import pandas as pd
import os
import zipfile
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# zip_ref = zipfile.ZipFile('/content/Train.zip', 'r') #Opens the zip file in read mode
with zipfile.ZipFile('/content/TRAIN.zip' , 'r') as zip_ref:
    zip_ref.extractall()
with zipfile.ZipFile('/content/TEST.zip' , 'r') as zip_ref:
    zip_ref.extractall()

file_train=["/content/TRAIN/0","/content/TRAIN/1"]
file_test=["/content/TEST/0","/content/TEST/1"]
imglist=[]
imgtest=[]
xtrain=[]
ytrain=[]
xtest=[]
ytest=[]

for i,fol in enumerate(file_train):
  for k in range (5):
    k=0
    # print(i,fol)
  for file in os.listdir(fol):
    if file.endswith(".png"):
      path_img=os.path.join(fol,file)
      img=cv.imread(path_img,0)
      imglist.append((img,i))

for i,fol in enumerate(file_test):
  for k in range (5):
    k=0
    # print(i,fol)
  for file in os.listdir(fol):
    if file.endswith(".png"):
      path_img=os.path.join(fol,file)
      img=cv.imread(path_img,0)
      imgtest.append((img,i))

for x,y in imglist:
  projection=np.sum(x,axis=1)
  print(projection)
  xtrain.append(projection)
  ytrain.append(y)
print("-------------")
print(xtrain[0])
print(len(xtrain))

for x,y in imgtest:
  projection=np.sum(x,axis=1)
  # print(projection)
  xtest.append(projection)
  ytest.append(y)
print("-------------")
print(xtrain[0])
print(len(xtrain))
print(ytrain[0])

# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
KNneigh = KNeighborsClassifier(n_neighbors=7)
KNneigh.fit(xtrain, ytrain)
# Predict on dataset which model has not seen before
print(KNneigh.predict(xtest))

# accuracy of the model 
accuracy=KNneigh.score(xtest, ytest)
print(accuracy)
print(f"KNN MODEL accuracy for the test data set is {100*accuracy} %")


#prediction of the model using a sample
img=cv.imread("/content/TEST/1/107.png")
cv2_imshow(img)
y=KNneigh.predict([xtest[100]])
print(f"predicted value of the image is {y}")

neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))
  
# Loop over K values
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(xtrain, ytrain)
      
    # Compute training and test data accuracy
    train_accuracy[i] = knn.score(xtrain, ytrain)
    test_accuracy[i] = knn.score(xtest, ytest)
# Generate plot
plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy')
  
plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()

"""SVM MODEL FOR THE TRAINING DATASET"""

# import support vector classifier 
# "Support Vector Classifier"
from sklearn.svm import SVC  
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(xtrain, ytrain)


#prediction 
print(svm_classifier.predict(xtest))
# svm_classifier.predict(xtest)
print(ytest)

accuracy=svm_classifier.score(xtest, ytest)
print(accuracy)
print(f"SVM MODEL accuracy for the test data set is {100*accuracy} %")

img=cv.imread("/content/TEST/0/10.png")
cv2_imshow(img)
y=svm_classifier.predict([xtest[0]])
print(f"predicted value of the image is {y}")

