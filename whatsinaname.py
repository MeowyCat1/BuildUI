from tkinter import *
import requests

def submit():
    name = entrybox.get()
    gender = requests.get("https://api.genderize.io", params= {"name":name}).json()["gender"]
    age = requests.get("https://api.agify.io", params= {"name":name}).json()["age"]
    nationalitycode = requests.get("https://api.nationalize.io", params= {"name":name}).json()["country"][0]["country_id"]
    nationalityname = requests.get(f"https://restcountries.com/v3.1/alpha/{nationalitycode}").json()[0]["name"]["common"]
    output.config(text= f"{name} is an {age} year old {gender} from {nationalityname}")

window = Tk()
window.config(bg= "antiquewhite")
window.title("What's in a name?")
window.geometry("400x400")
window.resizable(False,False)

Label(window, text= "Name Finder", font= ("Times New Roman", 20, "bold"), bg= "antiquewhite").pack(pady= 10)

entrybox = Entry(window, font= ("Times New Roman", 15), bg= "antiquewhite")

entrybox.pack(pady= 10)

Button(text= "Submit", command= submit, font= ("Times New Roman", 15), bg= "antiquewhite").pack(pady= 10)

output = Label(font= ("Times New Roman", 15), bg= "antiquewhite")

output.pack(pady= 10)

window.mainloop()