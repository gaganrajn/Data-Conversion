import tkinter as tk
from tkinter import filedialog
import pandas as pd
from timeit import default_timer as timer
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 310, height = 380, bg = 'white', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'white')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    begin = timer()
    read_file = pd.read_csv (import_file_path)
    end1 = timer()
    global final1
    final1 = end1-begin
   
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

def convertToJSON ():
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.json')
    start = timer()
    read_file.to_json(export_file_path, indent = 4)
    end = timer()
    final=end-start
    total = final+final1
    print("The time taken to convert from CSV to JSON format is around ", str(total)+"s")
saveAsButton_JSON = tk.Button(text='Convert CSV to JSON', command=convertToJSON, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JSON)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()