

### trim and remove the noises. 


import csv
import os
path_dir="C:/khp_data/other/"
path_dir2="C:/khp_data/tst2/"
file_list=os.listdir(path_dir)



for file in file_list:
    with open(path_dir+file,'r') as infile, open(path_dir2+file,'w',newline='') as outfile:
        reader=csv.reader(infile,delimiter=',')
        writer=csv.writer(outfile,delimiter=',')
        for row in reader:
            row=[x.replace('"','') if x=='"' else x for x in row]
            row=[x.replace(' ','') if x==' ' else x for x in row]
            row=[x.replace('NA','') if x=='NA' else x for x in row]
            row=[x.lower() for x in row]
            writer.writerows([row,])
            
            
