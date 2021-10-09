import time 
from tkinter import messagebox 
import tkinter as tk 
import requests 
import os 
 
def checkIfPrgmExists(): 
    print("File status:", end=' ') 
    time.sleep(1) 
    try: 
        fle = open("mainfile.py","r") 
        print("Exists on system") 
        time.sleep(1) 
        print("Program ran successfully") 
    except: 
        print("File not find, creating new file...") 
        fle = open("mainfile.py","a") 
        fle.write(r"""import pyautogui as p 
import time 
import webbrowser as w 
import re 
  
opn = open(r"C:\Users\pc\Desktop\cond.txt",'r').read() 
s1 = re.search('s =(.+)',opn).group(1) 
s2 = re.search('c =(.+)',opn).group(1) 
s3 = re.search('x =(.+)',opn).group(1) 
s4 = re.search('y =(.+)',opn).group(1) 
s = int(s1) 
c = int(s2) 
x = s3 
y = s4 
msg = "The message '%s' will be sent to '%s' at %s:%s" %(y,x,s,c) 
print(msg) 
q = s 
  
if (s == 00): 
    q = 24 
  
if (c == 00): 
    c = 60 
    s = q-1 
  
while True: 
    l = time.localtime(time.time()) 
    if(l.tm_hour == s)&(l.tm_min == c-1): 
        w.open('https://web.whatsapp.com/send?phone='+x+'&text='+y) 
        time.sleep(60) 
        p.press('enter') 
        break; 
    else: 
        opn = open(r"C:\Users\pc\Desktop\cond.txt",'r') 
        cond = opn.read() 
        if (cond == "break"): 
            break""") 
        fle.close() 
        time.sleep(1) 
        print("File created successfully") 
        time.sleep(1) 
        print("Program ran successfully") 
 
def check_internet(): 
    print("Internet status:", end=' ') 
    start = time.time() 
    try: 
        req = requests.get('https://web.whatsapp.com/') 
        end = time.time() 
        tyme = end - start 
        if (tyme >= 3): 
            print("Slow") 
        else: 
            print("Good") 
      
    except : 
        errmsg = "PLEASE CHECK INTERNET CONNECTION!" 
        print("Not available.") 
        print(errmsg) 
        messagebox.showerror("ERROR",errmsg) 
        exit()       
  
def break_it(): 
    f = open(r"C:\Users\pc\Desktop\cond.txt",'w') 
    f.write("break") 
    f.close() 
    exit() 
  
def send_message(): 
    s = e3.get() 
    c = e4.get() 
    x = e1.get() 
    y = e2.get() 
    msg = "The message '%s' will be sent to '%s' at %s:%s" %(y,x,s,c) 
    msg2 = "Cond =do\nx =%s\ny =%s\ns =%s\nc =%s"%(x,y,s,c) 
    print(msg) 
    open(r"C:\Users\pc\Desktop\cond.txt",'w').write(msg2) 
    messagebox.showinfo("SeWaMe", msg) 
    time.sleep(3) 
    os.startfile("mainfile.py") 
    master.mainloop() 
 
check_internet() 
checkIfPrgmExists() 
    
master = tk.Tk() 
master.title("SeWaMe") 
master.geometry("290x150") 
tk.Label(master, text="Receiver's name : ").grid(row=0) 
tk.Label(master, text="Message : ").grid(row=1) 
tk.Label(master, text="Hour : ").grid(row=2,column=0) 
tk.Label(master, text="Minutes : ").grid(row=3,column=0) 
  
e1 = tk.Entry(master) 
e2 = tk.Entry(master,width=30) 
e3 = tk.Spinbox(master, from_=00, to=23, width=5) 
e4 = tk.Spinbox(master, from_=00, to=59, width=5) 
  
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1) 
e4.grid(row=3, column=1) 
  
tk.Button(master,text='Cancel',command=break_it).grid(row=4, column=0)#,sticky=tk.W,pady=4) 
tk.Button(master,text='SEND MESSAGE', command=send_message).grid(row=4,column=1)#,sticky=tk.W,pady=1) 
master.mainloop() 