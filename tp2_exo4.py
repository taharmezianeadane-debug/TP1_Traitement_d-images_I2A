import cv2
##Question 1: 
im1 = cv2.imread('Images/pepper.bmp ')
##Question 2: 
h,w = im1.shape[:2]
print(f"la valeur de h : {h} ")
print(f"la valeur de h : {w} ")
##Question 3 : 
im2=cv2.resize(im1,(h//2,w//2))
cv2.imshow('image1_input',im1)
cv2.imshow('image2_input',im2)
cv2.waitKey(0)
##Question 4 : 
im3 = im1[30:150, 200:400] #comme si est une matrice et je veux une certaine partie indexé
cv2.imshow('image Croper',im3)
cv2.waitKey(0)
##Question 5 : image.copy() et cv2.putText(image,"txt",(x,y),cv2.Police, taille,Couleur,épaisseur)
im4=im1.copy()
for i in range(30,151): 
     for j in range(200,401): 
         im4[i,j]=[255,0,0]
cv2.putText(im4, "Mon rectangle", (200,20),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0) , 2)
cv2.imshow('image coloré',im4) 
cv2.waitKey(0)
##Question 6: cv2.rotate(image,degree)
im5=cv2.rotate(im1,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('image_rotat_90',im5)
cv2.waitKey(0)
#Question 7 : cv2.GaussianBlur(image,(deg,deg),sigma) deg <- positive et non null et sigma ce calcule auto selon (deg,deg)
im6=cv2.GaussianBlur(im1,(25,25),0)
cv2.imshow('felou_gaussien',im6)
cv2.waitKey(0)
#Question8 : déja repondus !
