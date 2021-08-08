#Imports 
import requests
import json
import tkinter
from tkinter import * 
from tkinter.font import Font

# Defining The window 
root = tkinter.Tk()
#Title 
root.title("News App")
#Geometry 
root.geometry("1200x500")
root.resizable(width=0, height=0)

#NewsAPI 
request = requests.get("https://saurav.tech/NewsAPI/top-headlines/category/health/in.json")
jason=request.json()["articles"];


#News Array 
FirstNews = jason[0]
SecondNews = jason[1]
ThirdNews = jason[2]
FourthNews = jason[3]
FifthNews = jason[4]

#News
FirstTitle = FirstNews["title"]
SecondTitle = SecondNews["title"]
thirdNews = ThirdNews["title"]
FourthNews =FourthNews["title"]
FifthNews = FifthNews["title"]

#Css
font = Font(
family="Helvetica",
size= 42,
slant="italic",

	)

#tkinter window 
news = Label(root , text = FirstTitle,padx = 10 , pady = 30 , font = "font")
news2 = Label(root , text = SecondTitle,padx = 10 , pady = 30, font = "font")
news3 = Label(root , text = thirdNews,padx = 10 , pady = 30, font = "font")
news4 = Label(root , text = FourthNews,padx = 10 , pady = 30, font = "font")
news5 = Label(root , text = FifthNews,padx = 10 , pady = 30, font = "font")

#To Diplay 
news.pack()
news2.pack()
news3.pack()
news4.pack()
news5.pack()


root.mainloop()