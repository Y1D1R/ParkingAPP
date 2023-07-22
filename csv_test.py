import csv
import cv2 as cv
from matplotlib.pyplot import close
##le file
img = cv.imread('img.jpg')
bd = "bd.csv"
cv.imwrite(filename="queries/img.jpg",img=img)
field_names = ['Nom','Prenom','Matricule','Image']
row_dict = {'Nom': 'LABCHRI','Prenom':'Amayas','Matricule':'256 98 453 12','Image':"queries\img.jpg"}


row_list = ["LABCHRI","Amayas","256 98 453 12","queries\img.jpg"]
"""def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)"""
        
def exist(filename, matricule):
    find = False
    with open(filename,"r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if matricule[2] == line[2]:
                find = True
                break
   
    return find
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

        
append_list_as_row(bd,row_list)