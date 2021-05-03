from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time
import psycopg2
import numpy as np
import time
import cv2
import math
import PIL
from PIL import ImageTk,Image
import socket
import threading
import requests
import json
import webbrowser
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def menu():
    screen5.destroy()
    screen6.destroy()
    con = psycopg2.connect(
        host="localhost",
        database="Library",
        user="postgres",
        password="gautham"
    )
    # cursor
    cur = con.cursor()
    
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Social Distancing")
    screen1.resizable(0,0)
    screen1.geometry("1000x600")
    screen1.iconbitmap(r'socialdistancing.ico')
    Label(screen1, text="Welcome", fg="#00005A", font=("calibri", 18)).pack()
    #Label(screen1, text="Menu", fg="#00005A", font=("calibri", 18)).pack()
    img = PhotoImage(file="C:\\Users\\Home\\rsz_four.png")
    b1 = Button(screen1, width="150", height="150", text="Sign in", command=start, image=img)
    b1.place(x=225, y=120)
    l1 = Label(screen1, text="Video Monitoring")
    l1.place(x=240, y=290)
    img1 = PhotoImage(file="C:\\Users\\Home\\rsz_five.png")
    b2 = Button(screen1, width="150", height="150", text="Sign in", command=show_user, image=img1)
    b2.place(x=25, y=120)
    l1 = Label(screen1, text="Profile", font="bold")
    l1.place(x=70, y=290)
    img2 = PhotoImage(file="C:\\Users\\Home\\rsz_six.png")
    b3 = Button(screen1, width="150", height="150", text="Sign in", command=covid, image=img2)
    b3.place(x=425, y=120)
    l1 = Label(screen1, text="Real Time Covid 19")
    l1.place(x=440, y=290)
    img3 = PhotoImage(file="C:\\Users\\Home\\rsz_seven.png")
    b4 = Button(screen1, width="150", height="150", text="Sign in", command=mobile, image=img3)
    b4.place(x=625, y=120)
    l1 = Label(screen1, text="IP Monitoring")
    l1.place(x=650, y=290)
    img4 = PhotoImage(file="C:\\Users\\Home\\rsz_eight.png")
    b5 = Button(screen1, width="150", height="150", text="Sign in", command=developer, image=img4)
    b5.place(x=825, y=120)
    l1 = Label(screen1, text="Developers")
    l1.place(x=860, y=290)
    con.commit()
    cur.close()
    con.close()
    username1.delete(0, END)
    password1.delete(0, END)
    screen1.mainloop()
    
    
def developer():
    screen12= Toplevel(screen1)
    screen12.geometry("500x500")
    screen12.title("Social distancing")
    screen12.resizable(0,0)
    screen12.iconbitmap(r'socialdistancing.ico')
    
    Label(screen12,text="DEVELOPERS INFORMATION\n", fg="#00005A", font=("calibri", 20)).pack()
    Label(screen12,text="1.GAUTHAM SHEKAR\n shekargautham1@gmail.com\n", fg="#00002A", font=("calibri", 12)).pack()
    Label(screen12,text="2.NIBIN BIN RIYAS AK \n nibinbinriyas@gmail.com\n",fg="#00002A", font=("calibri", 12)).pack()
    Label(screen12,text="3.SHRADDHA K \nshraddhakbhat@gmail.com\n", fg="#00002A", font=("calibri", 12)).pack()

    btn = Button(screen12, text = "close", bg="#6C63FF", fg="white",command=screen12.destroy).pack()

    screen12.mainloop()

def destroy1():
    screen5.destroy()
    screen6.destroy()
    
def mobile():
    screen16 = Toplevel(screen)
    screen16.geometry("800x600")
    screen16.title("Social distancing")
    screen16.resizable(0,0)
    screen16.iconbitmap(r'socialdistancing.ico')
    middleframe=Frame(screen16)
    middleframe.pack(side="bottom")

    def link():
        messagebox.askokcancel("Redirect","Redirecting you to www.play.google.com") 
        webbrowser.open("https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US")
    def destroy():
        screen16.destroy()

    Label(screen16,text="INSTRUCTIONS TO BE FOLLOWED\n", fg="#00005A", font=("calibri", 24)).pack()
    Label(screen16, text="1.Open the webcam application installed in your phone.\n", fg="#00002A", font=("calibri", 15)).pack()
    Label(screen16, text="2.If not installed  click on download button for the link \n and install.\n", fg="#00002A", font=("calibri", 15)).pack()
    Label(screen16, text="3.Click on start server and know the IP address to connect \nit to the system example:120.120.123.0\n", fg="#00002A", font=("calibri", 15)).pack()
    Label(screen16, text="4.Enable the hotspot in your phone and connect to the system. \n", fg="#00002A", font=("calibri", 15)).pack()
    Label(screen16, text="5.Go to the browser and type the IP address and start. \n", fg="#00002A", font=("calibri", 15)).pack()

    btn = Button(middleframe, text = "Download",fg="white",bg="#6C63FF",command=link).pack(side="left",padx=10)
    btn = Button(middleframe, text = "close",fg="white",bg="#6C63FF",command=destroy).pack(side="left",padx=10)
    btn = Button(middleframe, text = "start",fg="white",bg="#6C63FF", command = ip)
    btn.pack(side="left",padx=10)
    

def covid():
    global screen13
    screen13 = Toplevel(screen)
    screen13.resizable(0,0)
    screen13.title("Social Distancing")
    screen13.geometry("400x400")
    screen13.iconbitmap(r'socialdistancing.ico')
    
    lbl = Label(screen13, text ="Total active cases:-......") 
    lbl1 = Label(screen13, text ="Total confirmed cases:-...") 
  
    lbl.grid(column = 1, row = 0) 
    lbl1.grid(column = 1, row = 1) 
    lbl2 = Label(screen13, text ="") 
    lbl2.grid(column = 1, row = 3)
    def clicked():   
        url = "https://api.covid19india.org/data.json"
        page = requests.get(url) 
        data = json.loads(page.text) 
        lbl.configure(text ="Total active cases:-"+ data["statewise"][0]["active"]) 
      
        lbl1.configure(text ="Total Confirmed cases:-"+ data["statewise"][0]["confirmed"])
      
        lbl2.configure(text ="Data refreshed")
    btn = Button(screen13, text ="Refresh", bg="#6C63FF", fg="white", command = clicked) 
    btn.grid(column = 2, row = 8)
    screen13.mainloop()
    
def ip():
    try:
        socket.create_connection(("https://192.168.43.1:8080/video", 80))
        labelsPath = "coco.names"
        LABELS = open(labelsPath).read().strip().split("\n")

        np.random.seed(42)
        COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

        weightsPath = "yolov3.weights"
        configPath = "yolov3.cfg"

        net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)


        cap = cv2.VideoCapture("https://192.168.43.1:8080/video")

        while(cap.isOpened()):
    
            ret,image=cap.read()
            (H, W) = image.shape[:2]
            ln = net.getLayerNames()
            ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),swapRB=True, crop=False)
            net.setInput(blob)
            start = time.time()
            layerOutputs = net.forward(ln)
            end = time.time()
            print("Frame Prediction Time : {:.6f} seconds".format(end - start))
            boxes = []
            confidences = []
            classIDs = []
            for output in layerOutputs:
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    if confidence > 0.1 and classID == 0:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
                
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.3)
            ind = []
            for i in range(0,len(classIDs)):
                if(classIDs[i]==0):
                    ind.append(i)
            a = []
            b = []

            if len(idxs) > 0:
                    for i in idxs.flatten():
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        a.append(x)
                        b.append(y)
                
            distance=[] 
            nsd = []
            for i in range(0,len(a)-1):
                for k in range(1,len(a)):
                    if(k==i):
                        break
                    else:
                        x_dist = (a[k] - a[i])
                        y_dist = (b[k] - b[i])
                        d = math.sqrt(x_dist * x_dist + y_dist * y_dist)
                        distance.append(d)
                        if(d <=100):
                            nsd.append(i)
                            nsd.append(k)
                        nsd = list(dict.fromkeys(nsd))
                        print(nsd)
            color = (0, 0, 255) 
            for i in nsd:
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                text = "Alert"
                cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
            color = (0, 255, 0) 
            if len(idxs) > 0:
                for i in idxs.flatten():
                    if (i in nsd):
                        break
                    else:
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                        text = 'OK'
                        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)   
    
            cv2.imshow("Social Distancing Detector", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except OSError:
        messagebox.showerror("Social Distancing","It seems you have not connected to the IP address. Please Check your connection with your mobile phone.")
def register():
    global screen2
    screen2 = Toplevel(screen)
    screen2.configure(bg="white")
    screen2.title("Social Distancing")
    screen2.resizable(0,0)
    screen2.geometry("1000x600")
    screen2.iconbitmap(r'socialdistancing.ico')
    Label(screen2, text="Registration",bg="white", fg="#00005A", font=("calibri", 18)).pack()

    global User_id
    global Name
    global Email
    global Mobile
    global Username
    global Password
    uid = StringVar()
    name = StringVar()
    uemail = StringVar()
    umobile = StringVar()
    uname = StringVar()
    upass = StringVar()
    # uname = username.get()
    # upass = password.get()
    canvas = Canvas(screen2, width = 550, height = 500,bg="white", highlightbackground="white")      
    canvas.place(x=30, y=80)
    img = PhotoImage(file="C:\\Users\\Home\\second.png")
    img = img.subsample(2)
    canvas.create_image(300,250, image=img)
    label1 = Label(screen2, text="User ID", bg="white")
    label1.place(x=725, y=120)
    User_id = Entry(screen2, textvariable="uid", bg="#E1E1E1")
    User_id.place(x=680, y=150)
    label2=Label(screen2, text="Name ", bg="white")
    label2.place(x=730, y=180)
    Name = Entry(screen2, textvariable="name", bg="#E1E1E1")
    Name.place(x=680, y=210)
    label3=Label(screen2, text="Email", bg="white")
    label3.place(x=730, y=240)
    Email = Entry(screen2, textvariable="uemail", bg="#E1E1E1")
    Email.place(x=680, y=270)
    label4=Label(screen2, text="Mobile", bg="white")
    label4.place(x=730, y=300)
    Mobile = Entry(screen2, textvariable="umobile", bg="#E1E1E1")
    Mobile.place(x=680, y=330)
    label5=Label(screen2, text="Username", bg="white")
    label5.place(x=720, y=360)
    Username = Entry(screen2, textvariable="uname", bg="#E1E1E1")
    Username.place(x=680, y=390)
    label6=Label(screen2, text="Password", bg="white")
    label6.place(x=720, y=420)
    Password = Entry(screen2, textvariable="upass", bg="#E1E1E1", show='*')
    Password.place(x=680, y=450)
    Label(text="").pack()
    Label(text="").pack()
    button1=Button(screen2, text="Submit", height="1", width="20", fg="white", bg="#6C63FF", command=success)
    button1.place(x=675, y=490)  
    button2 = Button(screen2, text="GoBack", height="1", width="10", command=screen2.destroy)
    button2.pack()
    screen2.mainloop()

def success():
    uid = User_id.get()
    name = Name.get()
    uemail = Email.get()
    umobile = Mobile.get()
    uname = Username.get()
    upass = Password.get()

    # connect to db
    con = psycopg2.connect(
        host="localhost",
        database="Library",
        user="postgres",
        password="gautham"
    )

    # cursor
    cur = con.cursor()

    cur.execute("select * from uniqueid")
    global rows
    rows = cur.fetchall()


    for r in rows:
        u=r[0]
        id = str(u)
        uid1 = id.strip()
        if uid1 == uid:
            cur.execute("insert into register (User_ID,Name,Email,Mobile,Username,Password) values(%s,%s,%s,%s,%s,%s)",
                        (uid, name, uemail, umobile, uname, upass))
            Label(screen2, text="Registration Successful", fg="green").pack()
            cur.execute("select * from register")
            rows = cur.fetchall()

            for r in rows:
                print(f"Name : {r[1]}\n Email : {r[2]}")
            con.commit()
            cur.close()
            con.close()
            User_id.delete(0, END)
            Name.delete(0, END)
            Email.delete(0, END)
            Mobile.delete(0, END)
            Username.delete(0, END)
            Password.delete(0, END)
            
def show_user():

    screen11 = Toplevel(screen)
    screen11.title("Social Distancing")
    screen11.geometry("400x400")
    screen11.resizable(0,0)
    screen11.iconbitmap(r'socialdistancing.ico')
    # connect to db
    con = psycopg2.connect(
        host="localhost",
        database="Library",
        user="postgres",
        password="gautham"
    )

    # cursor
    cur = con.cursor()

    cur.execute("select * from register")
    global rows
    rows = cur.fetchall()

    for r in rows:
        u = r[4]
        id1 = str(u)
        user = id1.strip()
        p = r[5]
        id2 = str(p)
        passw = id2.strip()
     
        if uname==user and upass==passw:
            
            u1 = r[0]
            id3 = str(u1)
            userid = id3.strip()
            u2 = r[1]
            id4 = str(u2)
            name = id4.strip()
            u3 = r[2]
            id5 = str(u3)
            email = id5.strip()
            u4 = r[3]
            id6 = str(u4)
            mob = id6.strip()
            Label(screen11, text="Profile", fg ="#00005A").pack()
            l1 = Label(screen11, text="User Id:", fg ="#00005A")
            l1.place(x=10, y=20)
            l2 = Label(screen11, text=userid)
            l2.place(x=60, y=20)
            l3 = Label(screen11, text="Name: ", fg ="#00005A")
            l3.place(x=10, y=50)
            l4 = Label(screen11, text=name)
            l4.place(x=70, y=50)
            l5 = Label(screen11, text="Email: ", fg ="#00005A")
            l5.place(x=10, y=80)
            l6 = Label(screen11, text=email)
            l6.place(x=70, y=80)
            l7 = Label(screen11, text="Mobile: ", fg ="#00005A")
            l7.place(x=10, y=110)
            l8 = Label(screen11, text=mob)
            l8.place(x=70, y=110)
            b1 = Button(screen11, text="Close", bg="#6C63FF", fg="white", command=screen11.destroy)
            b1.place(x=180, y=170)
        
    screen11.mainloop()
            
            

def is_connected():
    top = Tk()
    top.title("Social Distancing")
    top.configure(background="#006666")

    l=Label(top,text='Checking ...')
    l.pack()
    try:
        socket.create_connection(("www.google.com", 80)) # better to set timeout as well
        state = "Online"
    except OSError:
         state = "Offline"
    l.config(text=state)
    print(state)
    top.mainloop()
            
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("1000x600")
    screen.iconbitmap(r'socialdistancing.ico')
    screen.configure(bg="white")
    screen.title("Social Distancing")
    screen.resizable(0,0)
    Label(text="SOCIAL DISTANCING MONITORING SYSTEM", fg="#00005A", bg="white", font=("calibri", 25)).pack()
    Label(text="", bg="white").pack()

    global username1
    global password1
    global unm
    global upd
    
    username = StringVar()
    password = StringVar()
    label9 = Label(text="Login", fg="#00005A", bg="white", font=("calibri", 20))
    label9.place(x=720, y=155)
    label1 = Label(text="Username", bg="white")
    label1.place(x=725, y=220)
    
    username1 = Entry(textvariable=username, bg="#E1E1E1")
    username1.place(x=690, y=250)
    Label(text="", bg="white").pack()
    canvas = Canvas(screen, width = 550, height = 500, bg="white", highlightbackground="white")      
    canvas.place(x=30, y=80)
    img = PhotoImage(file="C:\\Users\\Home\\third.png")
    img = img.subsample(2)
    canvas.create_image(300,250, image=img)    
    label2=Label(text="Password", bg="white")
    label2.place(x=725, y=290)
    password1 = Entry(textvariable=password, bg="#E1E1E1",show='*')
    password1.place(x=690, y=320)
    Label(text="", bg="white").pack()
    button1=Button(text="Login", height="1", width="17", bg="#6C63FF", fg="white", command=instruction)
    button1.place(x=697, y=370)
    Label(text="", bg="white").pack()
    button2=Button(text="Sign in", command=register)
    button2.place(x=740, y=420)
 
    screen.mainloop()
def close():
    cv2.DestroyWindow("Output.avi")
def start():
    labelsPath = 'coco.names'
    LABELS = open(labelsPath).read().strip().split("\n")

    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
        dtype="uint8")

    weightsPath = 'yolov3.weights'
    configPath = 'yolov3.cfg'
    cap = cv2.VideoCapture('mall.mp4')
    hasFrame, frame = cap.read()
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    vid_writer = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))



    while cv2.waitKey(1) < 0:
    
        ret,image=cap.read()
        image=cv2.resize(image,(1366,768))
        (H, W) = image.shape[:2]
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        blob = cv2.dnn.blobFromImage(image, 1 / 300.0, (416, 416),swapRB=True, crop=False)
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        end = time.time()
        print("Frame Prediction Time : {:.6f} seconds".format(end - start))
        boxes = []
        confidences = []
        classIDs = []
        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > 0.1 and classID == 0:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
                
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.3)
        ind = []
        for i in range(0,len(classIDs)):
            if(classIDs[i]==0):
                ind.append(i)
        a = []
        b = []

        if len(idxs) > 0:
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    a.append(x)
                    b.append(y)
                
        distance=[] 
        nsd = []
        for i in range(0,len(a)-1):
            for k in range(1,len(a)):
                if(k==i):
                    break
                else:
                    x_dist = (a[k] - a[i])
                    y_dist = (b[k] - b[i])
                    d = math.sqrt(x_dist * x_dist + y_dist * y_dist)
                    distance.append(d)
                    if(d <=100):
                        nsd.append(i)
                        nsd.append(k)
                    nsd = list(dict.fromkeys(nsd))
                    print(nsd)
        color = (0, 0, 255) 
        for i in nsd:
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = "Alert"
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
        color = (0, 255, 0) 
        if len(idxs) > 0:
            for i in idxs.flatten():
                if (i in nsd):
                    break
                else:
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                    text = 'OK'
                    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)   
    
        cv2.imshow('Social distancing', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        vid_writer.write(image)

    vid_writer.release()
    cap.release()
    cv2.destroyAllWindows()
    
def progress():
    global screen6
    screen6 = Tk()
    screen6.resizable(0,0)
    screen6.title("Social Distancing")
    screen6.geometry('350x200')
    screen6.iconbitmap(r'socialdistancing.ico')
    Label(screen6, text="Loading")
    progress = Progressbar(screen6, orient = HORIZONTAL, length = 100, mode = 'determinate')
    progress['value'] = 20
    screen6.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 40
    screen6.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    screen6.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    screen6.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    screen6.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100
  
    progress.pack(pady = 10)
    Label(screen6, text="You are connected to Internet").pack()
    Button(screen6, text="start", command=menu).pack()
    screen6.mainloop()
    
def New_Entry():
    
    global screen15
    global uid2
    screen15 = Toplevel(screen14)
    screen15.geometry("800x600")
    screen15.resizable(0,0)
    screen15.title("Social distancing")
    screen15.iconbitmap(r'socialdistancing.ico')
    Label(screen15,text="").pack()
    Label(screen15,text="").pack()
    Label(screen15,text="").pack()
    Label(screen15,text="Add New User", fg="#00005A",font=("calibri", 20)).pack()
    Label(screen15,text="").pack()
    Label(screen15,text="").pack()
    Label(screen15,text="").pack()
    user_id = StringVar()
    uid1=Label(screen15,text="User ID")
    uid1.pack()
    Label(screen15,text="").pack()
    #uid1.place(x=725, y=290)
    uid2 = Entry(screen15,textvariable=user_id, bg="#E1E1E1")
    uid2.pack()
    Label(screen15,text="").pack()
    #uid2.place(x=300, y=270)
    Label(text="").pack()
    button1=Button(screen15,text="Add", height="1", width="17", bg="#6C63FF", fg="white",command=Add_uid)
    #button1.pack()
    button1.place(x=250, y=290)
    button2=Button(screen15,text="Back", height="1", width="17", bg="#6C63FF",fg="white", command=screen15.destroy)
    #button2.pack()
    button2.place(x=400, y=290)
    screen15.mainloop()


def Add_uid():
    
    user_id=uid2.get()
    uuid=str(user_id)
    # connect to db
    con = psycopg2.connect(
    host="localhost",
    database="Library",
    user="postgres",
    password="gautham"
    )

    # cursor
    cur = con.cursor()
    
    cur.execute("INSERT INTO uniqueid (unique_id) VALUES (%s)",(uuid,))
    
    con.commit()
    cur.close()
    con.close()
    uid2.delete(0, END)
    
def instruction():
    global uname
    global upass
    count = 0
    
    uname = username1.get()
    upass = password1.get()
    # connect to db
    
    con = psycopg2.connect(
        host="localhost",
        database="Library",
        user="postgres",
        password="gautham"
    )

    # cursor
    cur = con.cursor()

    cur.execute("select * from register")
    global rows
    rows = cur.fetchall()

    for r in rows:
        u = r[4]
        id1 = str(u)
        user = id1.strip()
        p = r[5]
        id2 = str(p)
        passw = id2.strip()
        u1 = r[0]
        id3 = str(u1)
        userid = id3.strip()
        u2 = r[1]
        id4 = str(u2)
        name = id4.strip()
        u3 = r[2]
        id5 = str(u3)
        email = id5.strip()
        u4 = r[3]
        id6 = str(u4)
        mob = id6.strip()
        if (user == uname and passw == upass):
            global screen5
            screen5 = Tk()
            screen5.geometry("2000x2000")
            screen5.title("Social distancing")
            screen5.iconbitmap(r'socialdistancing.ico')
            Label(screen5,text="INSTRUCTIONS TO BE FOLLOWED\n", fg="#00005A", font=("Times new roman", 24)).pack()
            Label(screen5,text="1.This application is concerned on maintaining the social distancing between the\n people in public areas.\n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="2.Make sure you have proper CCTV cameras for monitoring the social distancing .\n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="3.Turn off your device,and do not remove or install battery charges,AC adapters,or \nany other accesory or your device when you are in the area with potentiality \nexplosive atmospheres .\n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="4.Make sure your passwords are safe and do not share your passwords with anyone. \n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="5.This application shows the person who has greater temperature than the specified \ntemperature.Immedialtely admit the person to near by hospital for COVID-19 test\n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="6.Make sure the details given by you in the registration page is true as per your knowledge .\n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="7.Follow the precautions of covid-19 be responsible and  stay safe. \n", fg="#00002A", font=("Times new roman", 10)).pack()
            Label(screen5,text="8.Click on get started to proceed\n", fg="#00002A", font=("Times new roman", 10)).pack()
            radioButton = Radiobutton(screen5, text ="I accept the terms and conditions of this application",value=0,font=("Times new roman", 10))
            radioButton.pack()
            btn = Button(screen5, text = "Get started", bg="#6C63FF", fg="white",font=("Times new roman", 10), command=progress)
            btn.pack()
            btn1 = Button(screen5, text="Check Your Connection", command=is_connected)
            btn1.pack()
            cur.close()
            con.close()
            username1.delete(0, END)
            password1.delete(0, END) 
            screen5.mainloop()
        else:
            count = count + 1 
        if (uname == 'admin' and upass == 'admin'):
            global screen14
            screen14 = Toplevel(screen)
            screen14.resizable(0,0)
            screen14.geometry("800x600")
            screen14.title("Social distancing")
            screen14.iconbitmap(r'socialdistancing.ico')
            Label(screen14, text="").pack()
            Label(screen14,text="Valid User IDs", fg="#00005A").pack()
            # connect to db
            con = psycopg2.connect(
                host="localhost",
                database="Library",
                user="postgres",
                password="gautham"
            )

            # cursor
            cur = con.cursor()

            cur.execute("select * from uniqueid")
            global adminrows
            adminrows = cur.fetchall()
            Label(screen14, text="").pack()
            Label(screen14, text="").pack()
            b1 = Button(screen14, text="New Entry", bg="#6C63FF", fg="white", command=New_Entry)
            b1.place(x=650, y=40)
            b2 = Button(screen14, text="Logout", bg="#6C63FF", fg="white", command=screen14.destroy)
            b2.place(x=730, y=40)
            
            for r in adminrows:
                l1 = Label(screen14, text=r[0].strip())
                l1.pack()
                
            cur.close()
            con.close()
            username1.delete(0, END)
            password1.delete(0, END)
            screen14.mainloop()
    if count>0:
        messagebox.showerror("error","Login Failed") 
            

main_screen()
