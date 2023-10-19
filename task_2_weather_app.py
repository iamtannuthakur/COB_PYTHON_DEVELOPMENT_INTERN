from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x600+200+100")
root.resizable(False, False)
root.configure(bg="mediumseagreen")

def WeatherDetails():
 try:
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)

    ti=pytz.timezone(result)
    local_time=datetime.now(ti)
    c_time=local_time.strftime("%I:%M %p")
    clock.config(text=c_time)
    name.config(text="CURRENT WEATHER")

# Add API Key Weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=29e1063025a955d19aa90b3841da46b2"
    json_data=requests.get(api).json()
    t.config(text=str(json_data['main']['temp'] - 273.15))
    c.config(text=json_data['weather'][0]['main'])
    w.config(text=json_data['wind']['speed'])
    h.config(text=json_data['main']['humidity'])
    d.config(text=json_data['weather'][0]['description'])
    p.config(text=json_data['main']['pressure'])

 except Exception as e:
     messagebox.showerror("Weather App","Invalid Entry!!")


Label(text="Weather App ", font="impact 35 bold", bg="green",width=100, height=1).pack(pady=2)

textfield = tk.Entry(root,justify="center",width=17,font=("impact",25,"bold"))
textfield.place(x=50,y=80)
textfield.focus()
searcg_icon = PhotoImage(file="search_icon.png")
myimage = Button(image=searcg_icon, borderwidth=0, cursor="hand2", bg="black", command=WeatherDetails)
myimage.place(x=330,y=80)

#logo
logo= PhotoImage(file="logo.png")
logo_l = Label(image=logo,bg="mediumseagreen")
logo_l.place(x=10, y=200)


#Time
name=Label(root, font=("arial",15,"bold"),bg="mediumseagreen")
name.place(x=30, y=140)
clock=Label(root, font=("Merriweather",20),bg="mediumseagreen")
clock.place(x=30, y=170)

#Label
l1=Label(root,text="WIND",font=("Merriweather",15,"bold"),fg="White",bg="darkslategrey",width=15).place(x=120,y=450)

l2=Label(root,text="HUMIDITY",font=("Merriweather",15,"bold"),fg="White",bg="darkslategrey",width=20).place(x=250,y=450)

l3=Label(root,text="DESCRIPTION",font=("Merriweather",15,"bold"),fg="White",bg="darkslategrey",width=20).place(x=430,y=450)

l4=Label(root,text="PRESSURE",font=("Merriweather",15,"bold"),fg="White",bg="darkslategrey",width=15).place(x=650,y=450)

t=Label(font=("arial",40,"bold"),bg="mediumseagreen")
t.place(x=400,y=180)
c=Label(font=("arial",20,"bold"),bg="mediumseagreen")
c.place(x=420,y=250)

w=Label(text="",font=("arial",16,"bold"),fg="black",bg="mediumseagreen")
w.place(x=180,y=480)
h=Label(text="",font=("arial",16,"bold"),fg="black",bg="mediumseagreen")
h.place(x=340,y=480)
d=Label(text="",font=("arial",16,"bold"),fg="black",bg="mediumseagreen")
d.place(x=480,y=480)
p=Label(text="",font=("arial",16,"bold"),fg="black",bg="mediumseagreen")
p.place(x=740,y=480)

root.mainloop()