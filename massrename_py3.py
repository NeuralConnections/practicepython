# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import os, re

def rename_files():

    #1 get file names from a folder
    file_list=os.listdir(r"C:\Users\gloverlu\Desktop\sample")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\gloverlu\Desktop\sample")

    #2 for each file, rename filename
    for file_name in file_list:
        
        print("Old name "+file_name)
        print("New name "+re.sub("[0-9]","", file_name))
        os.rename(file_name, re.sub("[0-9]","", file_name))
        
    os.chdir(saved_path)
                  
                  

rename_files()