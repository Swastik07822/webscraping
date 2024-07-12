import xlsxwriter
import csv


    
def writedict_csv(temp):
    with open('D:\Faltu\data.csv','a') as csvfile:
        csw = csv.writer(csvfile)
        csw.writerow(temp)
    csvfile.close()
    return True
 

