import requests
import numpy as np
import imutils
import cv2 as cv
import matplotlib.pyplot as plt
import glob


#On donne l'image de la voiture et la fonction va nous dire si elle est autorisée à entrer au Parking ou pas
def Sift_detector(queries,licence):
  #Affichage de la voiture
  img2 = licence
  

  #Creation de l'objet SIFT
  sift = cv.SIFT_create()

  #RGB To Gray scale
  gray_voiture = cv.cvtColor(licence, cv.COLOR_BGR2GRAY)

  #La detection des point d'interets et les descripteurs
  kp2, des2 = sift.detectAndCompute(gray_voiture, None)
  #print("Nombre de point Sift dans la voiture (len kp2) = ", len(kp2))
  #print("===========================================================")

  img3=img2
  #parcourir tout l'ensemble des images des matricules et faire une comparaison a chaque fois
  #maxgood=0


  meilleur_good=[]
  maxKp=0
  maxgood=0

  #Parcourir le dossier des plaques d'immatriculation
  for i in range(queries.shape[0]):
      #print("TEST avec la ",i+1,"éme matricule:\n")
      #recuperer l'image de la matricule
      img1 = queries[i]
      gray_matricule = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

      kp1, des1 = sift.detectAndCompute(gray_matricule, None)
     # print("Nombre de point Sift dans la matricule (len kp1) = ",len(kp1))

      bf = cv.BFMatcher()
      matches = bf.knnMatch(des1, des2, k=2)

      # Apply ratio test pour obtenir les bon matching
      good = []
      for m, n in matches:
          if m.distance < 0.6 * n.distance:
              good.append([m])

      #print("Nombre de bon matching (Taille de good) = ", len(good))



      #Si on a obtenu un nombre de bon matching plus grand
      if(len(good) > maxgood):
          #mettre a jour maxgood(plus grand nb de bon matching)
          maxgood=len(good)
          #mettre a jour maxKp(plus grand nb de point sift détécté)
          maxKp=len(kp1)
          #Dessiner les appariements
          img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

          #print("Plus grand nb de point sift détécté(max kp) = ",len(kp1))
          #print("Plus grand nb de bon matching(max good) = ", maxgood)
          #print("=================================================================")

          #sauvegarder les bon matching dans meilleur good
          meilleur_good = good
      #print("===========================================================")
  #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  #print("=================================================================")
  #print("Taille meilleur good ",len(meilleur_good))
  #print("Max kp = ", maxKp)

  nb_kifkif=0
  for j in range(len(meilleur_good) - 1):
      x, y = kp2[meilleur_good[j][0].trainIdx].pt
      x1, y1 = kp2[meilleur_good[j + 1][0].trainIdx].pt

      #Si un meme point d'interet dans la voiture est matché a plusieur autre point d'interet dans la matricule
      if(x==x1 and y==y1):
          nb_kifkif=nb_kifkif+1
      #print("(x, y ) = ", x, y)
      #print("(x1,y1) = ", x1, y1)

 # print("nb kifkif = ",nb_kifkif)

  if((nb_kifkif > len(meilleur_good)/3) or len(meilleur_good)==0):
      return False
  else:
      if(maxgood >= int(maxKp*0.05)):
          print(" bon matching ! ")
          print("goodmax = ",maxgood," kp = ",maxKp," pourcentage = ", maxKp*0.05)
          return True
      else:
          print(" faux matching ! ")
          print("goodmax = ", maxgood, " kp = ", maxKp, " pourcentage = ", int(maxKp * 0.05))
          return False


#licence = [cv.imread(file) for file in glob.glob("Voitures\*.jpg")]
#Sift_detector(queries,cv.imread("output.jpg"))