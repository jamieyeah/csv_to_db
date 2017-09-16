
#Change the csv files name in some order 


import os
import glob


path="C:/khp_data/mt/"

for filename in os.listdir(path):
    if filename[2:4] == "08":
        os.rename(path+filename,path+"khphh_"+filename[:2]+filename[5:6]+""+filename[-4:-5]+"_2008.csv")
    if filename[2:4] == "09":
        os.rename(path+filename,path+"khphh_"+filename[:2]+filename[5:6]+""+filename[-4:-5]+"_2009.csv")
    if filename[2:4] == "10":
        os.rename(path+filename,path+"khphh_"+filename[:2]+filename[5:6]+""+filename[-4:-5]+"_2010.csv")
    if filename[2:4] == "11":
        os.rename(path+filename,path+"khphh_"+filename[:2]+filename[5:6]+""+filename[-4:-5]+"_2011.csv")
    if filename[2:4] == "12":
        os.rename(path+filename,path+"khphh_"+filename[:2]+filename[5:6]+""+filename[-4:-5]+"_2012.csv")
    if filename[2:4] == "13":
        os.rename(path+filename,path+"khphh_"+filename[:2]+filename[5:6]+""+filename[-4:-5]+"_2013.csv")


import os
path="C:/khp_data/other/"

for filename in os.listdir(path):
    if len(filename) == 9:
        os.rename(path+filename,path+"khphh_t"+filename[3:5]+"_20"+filename[1:3]+".csv")
    if len(filename) == 10:
        os.rename(path+filename,path+"khphh_t"+filename[3:6]+"_20"+filename[1:3]+".csv")
    if len(filename) == 11:
        os.rename(path+filename,path+"khphh_t"+filename[3:7]+"_20"+filename[1:3]+".csv")
    if len(filename) == 12:
        os.rename(path+filename,path+"khphh_t"+filename[3:8]+"_20"+filename[1:3]+".csv")
    if len(filename) == 13:
        os.rename(path+filename,path+"khphh_t"+filename[3:9]+"_20"+filename[1:3]+".csv")
    if len(filename) == 14:
        os.rename(path+filename,path+"khphh_t"+filename[3:10]+"_20"+filename[1:3]+".csv")
    if len(filename) == 17:
        os.rename(path+filename,path+"khphh_t"+filename[3:13]+"_20"+filename[1:3]+".csv")



import os
path="C:/khp_data/panel_ind_hh/"

for filename in os.listdir(path):
    if len(filename) == 15:
        os.rename(path+filename,path+"khphh_"+filename[:5]+filename[6:8]+"_20"+filename[9:11]+".csv")
    if len(filename) == 16:
        os.rename(path + filename, path + "khphh_" + filename[:5] + filename[6:9] + "_20" + filename[10:12] + ".csv")


import os
import glob
fpath="C:/khp_data/khpind/*.csv"
for fpath in glob.glob(fpath):
    print(fpath)
    fpath_r=fpath.replace('khpind','khphh')
    os.rename(fpath,fpath_r)



