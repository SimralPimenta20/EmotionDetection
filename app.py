from tkinter import *
from tkinter import ttk
import webbrowser as wb
from pygame import *
import cv2
import random as rd
import os
import pandas as pd
from text import happy_text,anger_text,pickup_text,fear_text,neutral_text,sad_text

data1 = pd.read_csv('youtube urls1.csv')
urls = data1.iloc[0:29,0]
button_names = data1.iloc[0:29,1]



def callback(url):
    mixer.music.stop()
    wb.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)

def quit_window(r):
    r.destroy()
    mixer.music.stop()

def happy():
    path1 = "songs/happy"
    music = os.listdir(path1)
    mixer.init()
    a = rd.randrange(len(music))
    mixer.music.load(path1 + '//'+ music[a])
    mixer.music.play()
    root = Tk()
    rd_array = rd.sample(range(64),8)
    path = "ppm_resized"
    pics = os.listdir(path)
    while True:
        root.title("MOOD UP !")
        root.resizable(False,False)
        root.configure(background = "#ffffd0")
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',background = "#fee03b",foreground = "#ffffff",
                        font = ("Kristen ITC", 18),wraplength = 225,
                        justify = CENTER)
        style.configure('1.TButton',background = "#ff3367",foreground = "#ffffff",
                        font = ("Kristen ITC", 18),wraplength = 225,
                        justify = CENTER)
        style.configure('Quit.TButton',background = "#ff0000",foreground = "#ffffff",
                        font = ("Impact", 15),wraplength = 300,
                        justify = CENTER)
        style.configure('TFrame',background = "#ffffd0")
        style.configure('TLabel',foreground = "#ffffff",background = "#13254b")
        logo = PhotoImage(file = path + '//' +pics[rd_array[0]])
        label = ttk.Label(root,image = logo)
        label.grid(row = 0,column = 0)
        logo1 = PhotoImage(file = path + '//' +pics[rd_array[1]])
        label1 = ttk.Label(root,image = logo1)
        label1.grid(row = 0,column =1)
        logo2 = PhotoImage(file = path + '//' +pics[rd_array[2]])
        label2 = ttk.Label(root,image = logo2)
        label2.grid(row = 0,column = 2)
        logo3 = PhotoImage(file = path + '//' +pics[rd_array[3]])
        label3 = ttk.Label(root,image = logo3)
        label3.grid(row = 1,column = 0)
        logo4 = PhotoImage(file = path + '//' +pics[rd_array[4]])
        label4 = ttk.Label(root,image = logo4)
        label4.grid(row = 1,column = 2)
        logo5 = PhotoImage(file = path + '//' +pics[rd_array[5]])
        label5 = ttk.Label(root,image = logo5)
        label5.grid(row = 2,column = 0)
        logo6 = PhotoImage(file = path + '//' +pics[rd_array[6]])
        label6 = ttk.Label(root,image = logo6)
        label6.grid(row = 2,column = 1)
        logo7 = PhotoImage(file = path + '//' +pics[rd_array[7]])
        label7 = ttk.Label(root,image = logo7)
        label7.grid(row = 2,column = 2)
        text1 = rd.randrange(len(happy_text))
        label8 = ttk.Label(root, text = happy_text[text1],justify = CENTER,font = ("Kristen ITC", 18),wraplength = 225)
        label8.grid(row = 1, column =1)
        frame = ttk.Frame(root)
        frame.grid(row = 0,column = 3,rowspan = 3)
        frame.config(height = 675,width = 225)
        l = ttk.Label(frame,text = pickup_text[0],justify = CENTER,font = ("Kristen ITC", 18),wraplength = 500)
        l.grid(row = 0,column=0)
        #label_quit = ttk.Label (frame,text = "WARNING: YOU ARE FOREVER STUCK IN THIS APPLICATION.....JK! CLICK HERE TO QUIT!"
         #                       ,font = ("Kristen ITC",18),wraplength = 500,background = "red")

        #label_quit.grid(row = 6,column = 0)
        button1 = ttk.Button(frame,text = button_names[0]
                             ,command = lambda: callback(urls[0]),width = 25)
        button1.grid(row = 1,column = 0)
        
        button2 = ttk.Button(frame,text = button_names[1]
                             ,command = lambda: callback(urls[1]),width = 25,style = '1.TButton')
        button2.grid(row = 2,column = 0)
        
        button3 = ttk.Button(frame,text = button_names[2]
                             ,command = lambda: callback(urls[2]),width = 25)
        button3.grid(row = 3,column = 0)
        
        button4 = ttk.Button(frame,text = button_names[3]
                             ,command = lambda: callback(urls[3]),width = 25,style = '1.TButton')
        button4.grid(row = 4,column = 0)
        
        button5 = ttk.Button(frame,text = button_names[4]
                             ,command = lambda: callback(urls[4]),width = 25)
        button5.grid(row = 5,column = 0)
        button5 = ttk.Button(frame,text = "WARNING: YOU ARE FOREVER STUCK IN THIS APPLICATION.....JK! CLICK HERE TO QUIT!"
                             ,command = lambda: quit_window(root),width = 35,style = 'Quit.TButton')
        button5.grid(row = 7,column = 0)
        root.mainloop()
  
def anger():
    path1 = "songs/anger"
    music = os.listdir(path1)
    mixer.init()
    a = rd.randrange(len(music))
    mixer.music.load(path1 + '//'+ music[a])
    mixer.music.play()
    root = Tk()
    rd_array = rd.sample(range(64),8)
    path = "ppm_resized"
    pics = os.listdir(path)
    while True:
        root.title("MOOD UP !")
        root.resizable(False,False)
        root.configure(background = "#fff3f3")
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',background = "#f03967",foreground = "#ffffff",
                        font = ("Pristina", 20),wraplength = 225,
                        justify = CENTER)
        style.configure('1.TButton',background = "#bfaa99",foreground = "#ffffff",
                        font = ("Pristina", 20),wraplength = 225,
                        justify = CENTER)
        style.configure('Quit.TButton',background = "#ff0000",foreground = "#ffffff",
                        font = ("Impact", 15),wraplength = 300,
                        justify = CENTER)
        style.configure('TFrame',background = "#fff3f3")
        style.configure('TLabel',foreground = "#ffffff",background = "#7a56b4")
        logo = PhotoImage(file = path + '//' +pics[rd_array[0]])
        label = ttk.Label(root,image = logo)
        label.grid(row = 0,column = 0)
        logo1 = PhotoImage(file = path + '//' +pics[rd_array[1]])
        label1 = ttk.Label(root,image = logo1)
        label1.grid(row = 0,column =1)
        logo2 = PhotoImage(file = path + '//' +pics[rd_array[2]])
        label2 = ttk.Label(root,image = logo2)
        label2.grid(row = 0,column = 2)
        logo3 = PhotoImage(file = path + '//' +pics[rd_array[3]])
        label3 = ttk.Label(root,image = logo3)
        label3.grid(row = 1,column = 0)
        logo4 = PhotoImage(file = path + '//' +pics[rd_array[4]])
        label4 = ttk.Label(root,image = logo4)
        label4.grid(row = 1,column = 2)
        logo5 = PhotoImage(file = path + '//' +pics[rd_array[5]])
        label5 = ttk.Label(root,image = logo5)
        label5.grid(row = 2,column = 0)
        logo6 = PhotoImage(file = path + '//' +pics[rd_array[6]])
        label6 = ttk.Label(root,image = logo6)
        label6.grid(row = 2,column = 1)
        logo7 = PhotoImage(file = path + '//' +pics[rd_array[7]])
        label7 = ttk.Label(root,image = logo7)
        label7.grid(row = 2,column = 2)
        text1 = rd.randrange(len(anger_text))
        label8 = ttk.Label(root, text = anger_text[text1],justify = CENTER,font = ("Pristina", 20),wraplength = 225)
        label8.grid(row = 1, column =1)
        frame = ttk.Frame(root)
        frame.grid(row = 0,column = 3,rowspan = 3)
        frame.config(height = 675,width = 225)
        l = ttk.Label(frame,text = pickup_text[1],justify = CENTER,font = ("Pristina", 20),wraplength = 500)
        l.grid(row = 0,column=0)
        
 
        button1 = ttk.Button(frame,text = button_names[6]
                             ,command = lambda: callback(urls[6]),width = 25,style = '1.TButton')
        button1.grid(row = 1,column = 0)
        
        button2 = ttk.Button(frame,text = button_names[7]
                             ,command = lambda: callback(urls[7]),width = 25)
        button2.grid(row = 2,column = 0)
        
        button3 = ttk.Button(frame,text = button_names[8]
                             ,command = lambda: callback(urls[8]),width = 25,style = '1.TButton')
        button3.grid(row = 3,column = 0)
        
        button4 = ttk.Button(frame,text = button_names[9]
                             ,command = lambda: callback(urls[9]),width = 25)
        button4.grid(row = 4,column = 0)
        
        button5 = ttk.Button(frame,text = button_names[10]
                             ,command = lambda: callback(urls[10]),width = 25,style = '1.TButton')
        button5.grid(row = 5,column = 0)
        button5 = ttk.Button(frame,text = "WARNING: YOU ARE FOREVER STUCK IN THIS APPLICATION.....JK! CLICK HERE TO QUIT!"
                             ,command = lambda: quit_window(root),width = 35,style = 'Quit.TButton')
        button5.grid(row = 6,column = 0)
        root.mainloop()
def sad():
    path1 = "songs/sad"
    music = os.listdir(path1)
    mixer.init()
    a = rd.randrange(len(music))
    mixer.music.load(path1 + '//'+ music[a])
    mixer.music.play()
    root = Tk()
    rd_array = rd.sample(range(64),8)
    path = "ppm_resized"
    pics = os.listdir(path)
    while True:
        root.title("MOOD UP !")
        root.resizable(False,False)
        root.configure(background = "#f5fcf8")
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',background = "#fff73f",foreground = "#17113e",
                        font = ("Maiandra GD", 18,"bold"),wraplength = 225,
                        justify = CENTER)
        style.configure('1.TButton',background = "#84d4f6",foreground = "#f2e4b8",
                        font = ("Maiandra GD", 18,"bold"),wraplength = 225,
                        justify = CENTER)
        style.configure('Quit.TButton',background = "#ff0000",foreground = "#ffffff",
                        font = ("Impact", 15),wraplength = 300,
                        justify = CENTER)
        style.configure('TFrame',background = "#f5fcf8")
        style.configure('TLabel',foreground = "#ffffff",background = "#0d074d")
        logo = PhotoImage(file = path + '//' +pics[rd_array[0]])
        label = ttk.Label(root,image = logo)
        label.grid(row = 0,column = 0)
        logo1 = PhotoImage(file = path + '//' +pics[rd_array[1]])
        label1 = ttk.Label(root,image = logo1)
        label1.grid(row = 0,column =1)
        logo2 = PhotoImage(file = path + '//' +pics[rd_array[2]])
        label2 = ttk.Label(root,image = logo2)
        label2.grid(row = 0,column = 2)
        logo3 = PhotoImage(file = path + '//' +pics[rd_array[3]])
        label3 = ttk.Label(root,image = logo3)
        label3.grid(row = 1,column = 0)
        logo4 = PhotoImage(file = path + '//' +pics[rd_array[4]])
        label4 = ttk.Label(root,image = logo4)
        label4.grid(row = 1,column = 2)
        logo5 = PhotoImage(file = path + '//' +pics[rd_array[5]])
        label5 = ttk.Label(root,image = logo5)
        label5.grid(row = 2,column = 0)
        logo6 = PhotoImage(file = path + '//' +pics[rd_array[6]])
        label6 = ttk.Label(root,image = logo6)
        label6.grid(row = 2,column = 1)
        logo7 = PhotoImage(file = path + '//' +pics[rd_array[7]])
        label7 = ttk.Label(root,image = logo7)
        label7.grid(row = 2,column = 2)
        text1 = rd.randrange(len(sad_text))
        label8 = ttk.Label(root, text = sad_text[text1],justify = CENTER,font = ("Maiandra GD",18,"bold"),wraplength = 225)
        label8.grid(row = 1, column =1)
        frame = ttk.Frame(root)
        frame.grid(row = 0,column = 3,rowspan = 3)
        frame.config(height = 675,width = 225)
        l = ttk.Label(frame,text = pickup_text[2],justify = CENTER,font = ("Maiandra GD",18,"bold"),wraplength = 500)
        l.grid(row = 0,column=0)
        
        button1 = ttk.Button(frame,text = button_names[12]
                             ,command = lambda: callback(urls[12]),width = 25,style = '1.TButton')
        button1.grid(row = 1,column = 0)
        
        button2 = ttk.Button(frame,text = button_names[13]
                             ,command = lambda: callback(urls[13]),width = 25)
        button2.grid(row = 2,column = 0)
        
        button3 = ttk.Button(frame,text = button_names[14]
                             ,command = lambda: callback(urls[14]),width = 25,style = '1.TButton')
        button3.grid(row = 3,column = 0)
        
        button4 = ttk.Button(frame,text = button_names[15]
                             ,command = lambda: callback(urls[15]),width = 25)
        button4.grid(row = 4,column = 0)
        
        button5 = ttk.Button(frame,text = button_names[16]
                             ,command = lambda: callback(urls[16]),width = 25,style = '1.TButton')
        button5.grid(row = 5,column = 0)
        button5 = ttk.Button(frame,text = "WARNING: YOU ARE FOREVER STUCK IN THIS APPLICATION.....JK! CLICK HERE TO QUIT!"
                             ,command = lambda: quit_window(root),width = 35,style = 'Quit.TButton')
        button5.grid(row = 6,column = 0)
        root.mainloop()
def fear():
    path1 = "songs/fear"
    music = os.listdir(path1)
    mixer.init()
    a = rd.randrange(len(music))
    mixer.music.load(path1 + '//'+ music[a])
    mixer.music.play()
    root = Tk()
    rd_array = rd.sample(range(64),8)
    path = "ppm_resized"
    pics = os.listdir(path)
    while True:
        root.title("MOOD UP !")
        root.resizable(False,False)
        root.configure(background = "#fff3f3")
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',background = "#deafe1",foreground = "#5c599c",
                        font = ("Comic Sans MS", 18),wraplength = 225,
                        justify = CENTER)
        style.configure('1.TButton',background = "#ff1b50",foreground = "#2c0d21",
                        font = ("Comic Sans MS", 18),wraplength = 225,
                        justify = CENTER)
        style.configure('Quit.TButton',background = "#ff0000",foreground = "#ffffff",
                        font = ("Impact", 15),wraplength = 300,
                        justify = CENTER)
        style.configure('TFrame',background = "#fff3f3")
        style.configure('TLabel',foreground = "#ffffff",background = "#0d1246")
        logo = PhotoImage(file = path + '//' +pics[rd_array[0]])
        label = ttk.Label(root,image = logo)
        label.grid(row = 0,column = 0)
        logo1 = PhotoImage(file = path + '//' +pics[rd_array[1]])
        label1 = ttk.Label(root,image = logo1)
        label1.grid(row = 0,column =1)
        logo2 = PhotoImage(file = path + '//' +pics[rd_array[2]])
        label2 = ttk.Label(root,image = logo2)
        label2.grid(row = 0,column = 2)
        logo3 = PhotoImage(file = path + '//' +pics[rd_array[3]])
        label3 = ttk.Label(root,image = logo3)
        label3.grid(row = 1,column = 0)
        logo4 = PhotoImage(file = path + '//' +pics[rd_array[4]])
        label4 = ttk.Label(root,image = logo4)
        label4.grid(row = 1,column = 2)
        logo5 = PhotoImage(file = path + '//' +pics[rd_array[5]])
        label5 = ttk.Label(root,image = logo5)
        label5.grid(row = 2,column = 0)
        logo6 = PhotoImage(file = path + '//' +pics[rd_array[6]])
        label6 = ttk.Label(root,image = logo6)
        label6.grid(row = 2,column = 1)
        logo7 = PhotoImage(file = path + '//' +pics[rd_array[7]])
        label7 = ttk.Label(root,image = logo7)
        label7.grid(row = 2,column = 2)
        text1 = rd.randrange(len(fear_text))
        label8 = ttk.Label(root, text = fear_text[text1],justify = CENTER,font = ("Comic Sans MS", 18),wraplength = 225)
        label8.grid(row = 1, column =1)
        frame = ttk.Frame(root)
        frame.grid(row = 0,column = 3,rowspan = 3)
        frame.config(height = 675,width = 225)
        l = ttk.Label(frame,text = pickup_text[3],justify = CENTER,font = ("Comic Sans MS", 18),wraplength = 500)
        l.grid(row = 0,column=0)
        
        button1 = ttk.Button(frame,text = button_names[18]
                             ,command = lambda: callback(urls[18]),width = 25,style = '1.TButton')
        button1.grid(row = 1,column = 0)
        
        button2 = ttk.Button(frame,text = button_names[19]
                             ,command = lambda: callback(urls[19]),width = 25)
        button2.grid(row = 2,column = 0)
        
        button3 = ttk.Button(frame,text = button_names[20]
                             ,command = lambda: callback(urls[20]),width = 25,style = '1.TButton')
        button3.grid(row = 3,column = 0)
        
        button4 = ttk.Button(frame,text = button_names[21]
                             ,command = lambda: callback(urls[21]),width = 25)
        button4.grid(row = 4,column = 0)
        
        button5 = ttk.Button(frame,text = button_names[22]
                             ,command = lambda: callback(urls[22]),width = 25,style = '1.TButton')
        button5.grid(row = 5,column = 0)
        button5 = ttk.Button(frame,text = "WARNING: YOU ARE FOREVER STUCK IN THIS APPLICATION.....JK! CLICK HERE TO QUIT!"
                             ,command = lambda: quit_window(root),width = 35,style = 'Quit.TButton')
        button5.grid(row = 6,column = 0)
        root.mainloop()
def neutral():
    path1 = "songs/neutral"
    music = os.listdir(path1)
    mixer.init()
    a = rd.randrange(len(music))
    mixer.music.load(path1 + '//'+ music[a])
    mixer.music.play()
    root = Tk()
    rd_array = rd.sample(range(64),8)
    path = "ppm_resized"
    pics = os.listdir(path)
    while True:
        root.title("MOOD UP !")
        root.resizable(False,False)
        root.configure(background = "#fff7cc")
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',background = "#214fc6",foreground = "#ffffff",#51ffd8
                        font = ("Bradley Hand ITC", 18,"bold"),wraplength = 225,
                        justify = CENTER)
        style.configure('1.TButton',background = "#17fdad",foreground = "#724500",
                        font = ("Bradley Hand ITC", 18,"bold"),wraplength = 225,
                        justify = CENTER)
        style.configure('Quit.TButton',background = "#ff0000",foreground = "#ffffff",
                        font = ("Impact", 15),wraplength = 300,
                        justify = CENTER)
        style.configure('TFrame',background = "#fff7cc")
        style.configure('TLabel',foreground = "#724500",background = "#fffc00")
        logo = PhotoImage(file = path + '//' +pics[rd_array[0]])
        label = ttk.Label(root,image = logo)
        label.grid(row = 0,column = 0)
        logo1 = PhotoImage(file = path + '//' +pics[rd_array[1]])
        label1 = ttk.Label(root,image = logo1)
        label1.grid(row = 0,column =1)
        logo2 = PhotoImage(file = path + '//' +pics[rd_array[2]])
        label2 = ttk.Label(root,image = logo2)
        label2.grid(row = 0,column = 2)
        logo3 = PhotoImage(file = path + '//' +pics[rd_array[3]])
        label3 = ttk.Label(root,image = logo3)
        label3.grid(row = 1,column = 0)
        logo4 = PhotoImage(file = path + '//' +pics[rd_array[4]])
        label4 = ttk.Label(root,image = logo4)
        label4.grid(row = 1,column = 2)
        logo5 = PhotoImage(file = path + '//' +pics[rd_array[5]])
        label5 = ttk.Label(root,image = logo5)
        label5.grid(row = 2,column = 0)
        logo6 = PhotoImage(file = path + '//' +pics[rd_array[6]])
        label6 = ttk.Label(root,image = logo6)
        label6.grid(row = 2,column = 1)
        logo7 = PhotoImage(file = path + '//' +pics[rd_array[7]])
        label7 = ttk.Label(root,image = logo7)
        label7.grid(row = 2,column = 2)
        text1 = rd.randrange(len(neutral_text))
        label8 = ttk.Label(root, text = neutral_text[text1],justify = CENTER,font = ("Bradley Hand ITC", 18,"bold"),wraplength = 225)
        label8.grid(row = 1, column =1)
        frame = ttk.Frame(root)
        frame.grid(row = 0,column = 3,rowspan = 3)
        frame.config(height = 675,width = 225)
        l = ttk.Label(frame,text = pickup_text[4],justify = CENTER,font = ("Bradley Hand ITC", 18,"bold"),wraplength = 500)
        l.grid(row = 0,column=0)
        
        button1 = ttk.Button(frame,text = button_names[24]
                             ,command = lambda: callback(urls[24]),width = 25,style = '1.TButton')
        button1.grid(row = 1,column = 0)
        
        button2 = ttk.Button(frame,text = button_names[25]
                             ,command = lambda: callback(urls[25]),width = 25)
        button2.grid(row = 2,column = 0)
        
        button3 = ttk.Button(frame,text = button_names[26]
                             ,command = lambda: callback(urls[26]),width = 25,style = '1.TButton')
        button3.grid(row = 3,column = 0)
        
        button4 = ttk.Button(frame,text = button_names[27]
                             ,command = lambda: callback(urls[27]),width = 25)
        button4.grid(row = 4,column = 0)
        
        button5 = ttk.Button(frame,text = button_names[28]
                             ,command = lambda: callback(urls[28]),width = 25,style = '1.TButton')
        button5.grid(row = 5,column = 0)
        button5 = ttk.Button(frame,text = "WARNING: YOU ARE FOREVER STUCK IN THIS APPLICATION.....JK! CLICK HERE TO QUIT!"
                             ,command = lambda: quit_window(root),width = 35,style = 'Quit.TButton')
        button5.grid(row = 6,column = 0)
        root.mainloop()



