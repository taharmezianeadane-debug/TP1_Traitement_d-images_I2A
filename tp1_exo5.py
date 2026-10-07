import cv2
import matplotlib.pyplot as plt
#Question 1: 
im1=cv2.imread('Images/cameraman.bmp',0)
im2=cv2.imread('Images/pepper.bmp')
#Question 2 : 
hist1 = cv2.calcHist([im1], [0], None, [256], [0, 256])
hist2_B = cv2.calcHist([im2], [0], None, [256], [0, 256])
hist2_G = cv2.calcHist([im2], [1], None, [256], [0, 256])
hist2_R = cv2.calcHist([im2], [2], None, [256], [0, 256])
#Question 3: 
#### Image a niveau de gris : 
plt.plot(hist1)
plt.title("Histogramme de im1")
plt.xlabel("Niveau de gris")
plt.ylabel("Nombre de pixels")
plt.show()
#### Image en Couleurs : 
hist2_B = cv2.calcHist([im2], [0], None, [256], [0, 256])
hist2_G = cv2.calcHist([im2], [1], None, [256], [0, 256])
hist2_R = cv2.calcHist([im2], [2], None, [256], [0, 256])
plt.figure()
plt.plot(hist2_B, label="Bleu")
plt.plot(hist2_G, label="Vert")
plt.plot(hist2_R, label="Rouge")
plt.title("Histogramme de im2")
plt.xlabel("Niveau de pixel")
plt.ylabel("Nombre de pixels")
plt.legend()
plt.show()
#Question 5 : 
##pour le premier hist : 
hist_1 = [0] * 256
h,w=im1.shape[:2]
for i in range(h):
    for j in range(w):
        pixel=im1[i,j]
        hist_1[pixel]+=1

for i in range(len(hist_1)):
    print(hist_1[i])

plt.plot(hist_1)
plt.title("Histogramme de im1 de Question 05")
plt.show()
##pour le deuxieme hist : 
histp2_B = [0] * 256
histp2_G = [0] * 256
histp2_R = [0] * 256

for i in range(h):
    for j in range(w):

        pixel_B=im2[i,j,0]
        hist2_B[pixel_B]+=1

        pixel_v=im2[i,j,1]
        histp2_G[pixel_v]+=1

        pixel_R=im2[i,j,2]
        histp2_R[pixel_R]+=1



plt.figure()

plt.plot(hist2_B, label="Bleu")
plt.plot(hist2_G, label="Vert")
plt.plot(hist2_R, label="Rouge")

plt.title("Histogramme de im2")
plt.xlabel("Valeur du pixel")
plt.ylabel("Nombre de pixels")

plt.legend()
plt.show()