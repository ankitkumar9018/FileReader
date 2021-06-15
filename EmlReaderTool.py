# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 00:40:08 2020

@author: ankit kumar
"""


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def open_file_button():
    master.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("eml files","*.eml")))

    
def extract_file_button():
    master.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("encrypted files","*.enc"),("all files","*.*")))



master = tk.Tk()

master.title('EML File extractor')


tk.Button(master, 
          text='Open Folder', 
          command=open_file_button).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Extract Attachments', command=extract_file_button).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(master, 
          text='Quit', command=master.quit).grid(row=3, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()



#pyinstaller --onefile --noconsole encrptionTool.py



