# -*- coding: utf-8 -*-
"""logoMatch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/105E-nhYnWHrF65NK8UQSfXLLNcmTCRJa
"""

#@title Importing the libraries

import cv2
import numpy as np
import glob
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
!pip install easyocr
import easyocr
reader = easyocr.Reader(['en'])

#@title Using SIFT Method Example 1

def calling_sift(image,logo):
  obj_sift = cv2.SIFT_create()
  kp_logo, logo_descript = obj_sift.detectAndCompute(logo, None)
  kp_scene, image_descript = obj_sift.detectAndCompute(image, None)
  fbmatcher = cv2.FlannBasedMatcher()
  matches = fbmatcher.knnMatch(logo_descript, image_descript, k=2)
  points = []
  for m,n in matches:
    if m.distance < 0.6*n.distance:
      points.append(m)
  print(f"Points matched are {len(points)}")
  return len(points)

#@title Example 1 Using SIFT
directory = "/content/sample_data/Example1/logos/*.*"
image1 = cv2.imread('/content/sample_data/levis_shop.jpg')
answer=None
count=0
matc=0
for file in glob.glob(directory):
   print(file)
   logo= cv2.imread(file)
   count=calling_sift(image1,logo)
   if count>matc:
     answer = logo
     matc=count

obj_sift = cv2.SIFT_create()

kp_logo, logo_descript = obj_sift.detectAndCompute(answer, None)
kp_scene, image_descript = obj_sift.detectAndCompute(image1, None)
fbmatcher = cv2.FlannBasedMatcher()

matches = fbmatcher.knnMatch(logo_descript, image_descript, k=2)
good_matches = []
for m,n in matches:
  if m.distance < 0.6*n.distance:
    good_matches.append(m)
result = cv2.drawMatches(answer, kp_logo, image1, kp_scene, good_matches, None)
cv2_imshow(result)
cv2_imshow(answer)

#@title Using SIFT Method Example 2

def calling_sift(image,logo):
  obj_sift = cv2.SIFT_create()
  kp_logo, logo_descript = obj_sift.detectAndCompute(logo, None)
  kp_scene, image_descript = obj_sift.detectAndCompute(image, None)
  fbmatcher = cv2.FlannBasedMatcher()
  matches = fbmatcher.knnMatch(logo_descript, image_descript, k=2)
  points = []
  for m,n in matches:
    if m.distance < 0.6*n.distance:
      points.append(m)
  print(f"Points matched are {len(points)}")
  return len(points)

#@title Example 1 Using SIFT
directory = "/content/sample_data/Example2/logos/*.*"
image1 = cv2.imread('/content/sample_data/starbucks_shop.jpeg')
answer=None
count=0
matc=0
for file in glob.glob(directory):
   print(file)
   logo= cv2.imread(file)
   count=calling_sift(image1,logo)
   if count>matc:
     answer = logo
     matc=count

obj_sift = cv2.SIFT_create()

kp_logo, logo_descript = obj_sift.detectAndCompute(answer, None)
kp_scene, image_descript = obj_sift.detectAndCompute(image1, None)
fbmatcher = cv2.FlannBasedMatcher()

matches = fbmatcher.knnMatch(logo_descript, image_descript, k=2)
good_matches = []
for m,n in matches:
  if m.distance < 0.6*n.distance:
    good_matches.append(m)
result = cv2.drawMatches(answer, kp_logo, image1, kp_scene, good_matches, None)
cv2_imshow(result)
cv2_imshow(answer)

#@title Using ORB Method Example 1

def calling_ORB(image, logo):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    kp_logo, des1 = orb.detectAndCompute(image_gray, None)
    kp_scene, des2 = orb.detectAndCompute(logo_gray, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    match_count=0
    for i in range(len(matches)):
      match=matches[i]
      if match.distance > 70:
        match_count+=1
    print(f"Points matched are {match_count}")
    return match_count

directory = "/content/sample_data/Example1/logos/*.*"
image1 = cv2.imread('/content/sample_data/levis_shop.jpg')
answer=None
count=0
matc=0
for file in glob.glob(directory):
   print(file)
   logo= cv2.imread(file)
   count=calling_ORB(image1,logo)
   if count>matc:
     answer = logo
     matc=count

image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
kp_logo, des1 = orb.detectAndCompute(image_gray, None)
kp_scene, des2 = orb.detectAndCompute(logo_gray, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
img3 = cv2.drawMatches(image1, kp_logo, logo, kp_scene, matches[:5], None, flags=2)
cv2_imshow(img3)

#@title Using ORB Method Example 2

def calling_ORB(image, logo):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    kp_logo, des1 = orb.detectAndCompute(image_gray, None)
    kp_scene, des2 = orb.detectAndCompute(logo_gray, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    match_count=0
    for i in range(len(matches)):
      match=matches[i]
      if match.distance > 70:
        match_count+=1
    print(f"Points matched are {match_count}")
    return match_count

directory = "/content/sample_data/Example2/logos/*.*"
image1 = cv2.imread('/content/sample_data/starbucks_shop.jpeg')
answer=None
count=0
matc=0
for file in glob.glob(directory):
   print(file)
   logo= cv2.imread(file)
   count=calling_ORB(image1,logo)
   if count>matc:
     answer = logo
     matc=count

image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
kp_logo, des1 = orb.detectAndCompute(image_gray, None)
kp_scene, des2 = orb.detectAndCompute(logo_gray, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
img3 = cv2.drawMatches(image1, kp_logo, logo, kp_scene, matches[:5], None, flags=2)
cv2_imshow(img3)

#@title logo Matching using Template Matching

def logo_matching(image, logo):
  mark = 0.3
  g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  logo = cv2.imread(logo, 0)
  bread, height = logo.shape[::-1]
  res = cv2.matchTemplate(g_image, logo, cv2.TM_CCOEFF_NORMED)
  points=0
  loc = np.where(res >= mark)
  for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + bread, pt[1] + height), (0, 255, 255), 2)
    points+=1
  print(points)
  return points


directory = "/content/sample_data/Example1/logos/*.*"
image1 = cv2.imread('/content/sample_data/levis_shop.jpg')
answer=None
count=0
matc=0
for file in glob.glob(directory):
   print(file)
   logo= cv2.imread(file)
   count=logo_matching(image1,file)
   if count>matc:
     answer = logo
     matc=count
cv2_imshow(answer)

directory = "/content/sample_data/Example2/logos/*.*"
image1 = cv2.imread('/content/sample_data/starbucks_shop.jpeg')
answer=None
count=0
matc=0
for file in glob.glob(directory):
   print(file)
   logo= cv2.imread(file)
   count=logo_matching(image1,file)
   if count>matc:
     answer = logo
     matc=count
cv2_imshow(answer)

# import imutils
# #preprocessing the template logo image to get the desired result
# # define the alpha and beta
# alpha = 1 # Contrast control
# beta = 8 # Brightness control

# # call convertScaleAbs function
# adjusted_logo = cv.convertScaleAbs(template, alpha=alpha, beta=beta)
# cv2_imshow(adjusted_logo)
# # Cropping an image
# # cropped_image = adjusted_logo[7:70, 0:200]
# # cv2_imshow(cropped_image)
# #rotationn
# rotated_image = imutils.rotate(cropped_image, angle=-5)
# cv2_imshow(rotated_image)
# print(rotated_image.shape)
# resized = cv.resize(rotated_image, (300,150))
# cv2_imshow(resized)

"""ADDITIONAL METHOD USING EASEOCR"""

template = cv2.imread("/content/levis.jpg")
img2=cv2.imread("/content/levis_shop.jpg")
cv2_imshow(template)
cv2_imshow(img2)
# result_img=img2
# result_logo=template
result_img=reader.readtext(img2)
result_logo=reader.readtext(template)
print(result_img)
print(result_logo)
type(result_img)
print(len(result_img))
text_img=np.asarray(result_img)
text_logo=np.asarray(result_logo)
print(text_img[0,1])
l1=len(text_img)
t=0
for i in range(l1-1):
  if (text_img[i,1]==text_logo[0,1]):
    print(f"LOGO HAS BEEN FOUND MATCHING TO THE SCENE WITH BRAND NAMED AS:{text_img[i,1]}")
    break
  else:
    t=t+1

if t!=0:
      print(f"NOT ENOUGH MATCH POINT FOUND AS SCENE AS LOGO:{text_img[i,1]} AND SUPPLIED LOGO IMAGE IS:{text_logo[0,1]}")
