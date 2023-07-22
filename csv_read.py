from unicodedata import name
import cv2 as cv
import csv
mat= '921 05 37756'
find = False
## Ecrire
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        if exist(file_name,list_of_elem) == False:
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
        else:
            print("existe deja")
## EXISTE
def exist(filename, matricule):
    find = False
    with open(filename,"r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if matricule[2] == line[2]:
                find = True
                break
   
    return find
####lire
def lire(filename):
    with open(filename,"r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)
new_list = ["KOULAL","Yihdir Aghiles","156 263 987 123","queris"]
"""def modifier(filename,mat,new):
    if exist(filename, new) == True:
        ## Le cas ou la ligne a  modifier existe
        if mat == new[2]:
            
        pass
    pass
"""
import pandas as pd
i = 0
l = pd.read_csv('bd.csv',header=None)
with open("bd.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if mat == line[2]:
            find = True
            break
        else:
            i=i+1
#print(l)
#l.iloc[i][0] = "KOULAL"
# = "Yidhir Aghiles"
l = l[l.iloc[:][2] != "921 05 37846"]
print(l)
#l.to_csv("bd.csv",index=False,index_label=False,header=False)