from tkinter import *
from tkinter import messagebox
from tkinter import font
import time
import os
import sys
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from collections import defaultdict
from collections import deque



root = Tk()
root.title("house points program")
photo = PhotoImage(file = "gui icon.png")
root.iconphoto(False, photo)

#to check for internet connection
try:
    sender = "publicbetaprogram@gmail.com"
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.starttls()
    mailserver.login(sender, "publicbeta")

except socket.gaierror:
    message.showwarning("Warning!", "you are not connected to the internet!")
    message.showinfo("Error Information", "The program can't connect to the mail server")
    root.destroy()
    sys.exit()
    

def addpts(): #func to add pts (if not first time)
    global houses
    global addedpoints
    houses = ["Asgard", "Xandar", "Valhalla", "Wakanda"]
    readpoints = []
    addedpoints = []
    file = open("house points data.txt", "r")
    for line in file:
        m = line.strip()
        readpoints.append(m)
    file.close()
        
    asgard = float(entry1.get()) + float(readpoints[1])
    xandar = float(entry2.get()) + float(readpoints[3])
    valhalla = float(entry3.get()) + float(readpoints[5])
    wakanda = float(entry4.get()) + float(readpoints[7])

    addedpoints.append(asgard)
    addedpoints.append(xandar)
    addedpoints.append(valhalla)
    addedpoints.append(wakanda)

    file = open("house points data.txt", "w")
    for i in range (len(houses)):
        file.write(f"{houses[i]}:")
        file.write("\n")
        file.write(str(addedpoints[i]))
        file.write("\n")

    now = datetime.datetime.now()
    Date = now.strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"\n\n\nlast updated on {Date}")
    file.close()
    
    d = defaultdict(deque)
    for i, x in enumerate(sorted(addedpoints, reverse=True), start=1):
        d[x].append(i)

    result = [d[x].popleft() for x in addedpoints]

    rank = (f"\n\n The rank of Asgard: {result[0]} \n The rank of Valhalla: {result[1]} \n The rank of Wakanda: {result[2]} \n The rank of Xandar: {result[3]}")



    messagebox.showinfo("Information", "house points are already updated!")
    root2 = Tk()
    root2.title("house points data")
    labelres1 = Label(root2, text=f"points of {houses[0]}: {addedpoints[0]}")
    labelres2 = Label(root2, text=f"points of {houses[1]}: {addedpoints[1]}")
    labelres3 = Label(root2, text=f"points of {houses[2]}: {addedpoints[2]}")
    labelres4 = Label(root2, text=f"points of {houses[3]}: {addedpoints[3]}")
    labelres5 = Label(root2, text = rank)
    #labelwarn = Label(root2, text="this window will close in 5 seconds")

    labelres1.grid(row=0, column=0)
    labelres2.grid(row=1, column=0)
    labelres3.grid(row=2, column=0)
    labelres4.grid(row=3, column=0)
    labelres5.grid(row=4, column=0)
    #labelwarn.grid(row=5, column=0)


    messagebox.showwarning("Warning", "points will now be shared to students")

    contacts = ["tan.michael@sis-semarang.org"]
    file = open("house points data.txt", "r")
    data = file.read()
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ",".join(contacts)
    msg["Subject"] = "House Points Info"
    msg.attach(MIMEText(data, 'plain'))
    msg.attach(MIMEText(rank, 'plain'))
    mailserver.sendmail(sender, contacts, msg.as_string())
    messagebox.showinfo("Information", "points are shared to students via email")
    root.destroy()
    root2.destroy()
    sys.exit


def reset():
    res = messagebox.askquestion("Warning", "Are you sure to reset all the house points?")
    if res == 'yes':
        os.remove("house points data.txt")
        messagebox.showinfo("Information", "Points has been reset!")
        root.destroy()
        sys.exit()
    


    

label1 = Label(root, text ="Asgard", fg ="green")
label2 = Label(root, text = "Xandar", fg ="red")
label3 = Label(root, text = "Valhalla", fg = "orange")
label4 = Label(root, text = "Wakanda", fg = "blue")

entry1= Entry(root, width=15, borderwidth = 10) #asgard
entry2= Entry(root, width=15, borderwidth = 10) #xandar
entry3= Entry(root, width=15, borderwidth = 10) #valhalla
entry4= Entry(root, width=15, borderwidth = 10) #wakanda

button1 = Button(root, text = "update points", padx=60, pady=10, command = addpts)
button2 = Button(root, text = "reset points", padx = 60, pady=10, command=reset)


label1.grid(column=0, row=0, columnspan=1)
label2.grid(column=1, row=0,columnspan=1)
label3.grid(column=2, row=0, columnspan=1)
label4.grid(column=3, row=0, columnspan=1)

entry1.grid(row=1, column=0, columnspan=1, padx=20)
entry2.grid(row=1, column=1, columnspan=1, padx=20)
entry3.grid(row=1, column=2, columnspan=1, padx=20)
entry4.grid(row=1, column=3, columnspan=1, padx=20)

button1.grid(row=2, column=0, columnspan= 2)
button2.grid(row=2, column=2, columnspan =2)



            

def writefirst(): #inputting points for the first time
    points = []
    houses = ["Asgard", "Xandar", "Valhalla", "Wakanda"]
    points.append(entry1.get())
    points.append(entry2.get())
    points.append(entry3.get())
    points.append(entry4.get())
    file = open("house points data.txt", "w")
    for i in range(len(points)):
        file.write(f"{houses[i]}:")
        file.write("\n")
        file.write(points[i])
        file.write("\n")
    
    now = datetime.datetime.now()
    Date = now.strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"\n\n\nlast updated on {Date}")
    file.close()
    messagebox.showinfo("information", "current points are already saved!")
    messagebox.showinfo("information", "re-run the program to update the current points of each houses")
    root.destroy()
    sys.exit()


file = open("house points data.txt", "a")
file.close()
size = os.stat("house points data.txt").st_size

if size == 0: #to check wether it is the first time
    
    button2 = Button(root, text = "reset points", padx = 60, pady=10, state= DISABLED)
    button1 = Button(root, text = "update points", padx=60, pady=10, command=writefirst)

    tell = Label(root, text="this is your first time running the program, reset points will be de-activated")
        
    button1.grid(row=2, column=0, columnspan= 2)
    button2.grid(row=2, column=2, columnspan =2)
    tell.grid(row=3, column=0, columnspan=4)
    
else:
    pass


    
    
    

    

root.mainloop()



