import cv2

img1 = cv2.imread('Images/compteur.jpg')

# Cas 1 : Binarisation avec la fonction prédéfinie de cv2
# Syntaxe :
# ret, image_binaire = cv2.threshold(image, seuil, valeur_max, type)

ret, imgb1 = cv2.threshold(img1, 80, 255, cv2.THRESH_BINARY)
cv2.imshow('cas1', imgb1)
cv2.waitKey(0)

#Cas2 : Binarisation manuelle

imgb2=img1.copy()
imgb2 = cv2.cvtColor(imgb2, cv2.COLOR_BGR2GRAY)
h,w =img1.shape[:2]
for i in range(h) : 
     for j in range(w): 
         if imgb2[i,j]<=80 : 
             imgb2[i,j]=0
         else: 
                 imgb2[i,j]=255
    
cv2.imshow('cas 2', imgb2)
cv2.waitKey(0)     