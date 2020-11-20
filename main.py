import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading


def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url = "https://worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    soup = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = soup.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""


    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data  +  text  +" "+  " "  +  count + "\n"
    # print(all_data)
    return all_data

def country_data():
    name = textfield.get()
    url = "https://worldometers.info/coronavirus/country/"+name 
    html_data = get_html_data(url)
    soup = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = soup.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""


    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data  +  text  + "(" + name + ")" + "  "  +  count  + "\n"
    
    mainlabel['text'] = all_data

def reload():
    new_data = get_covid_data()
    mainlabel['text']=new_data



get_covid_data()    


def notifications()
    while True:
        plyer.notification.notify(
            title = "COVID-19 DATA TRACKER",
            message = get_covid_data(),
            timeout = 10,
            app_icon = "corona.ico"
            
        )
        time.sleep(3600)


root = tk.Tk() 
root.geometry("900x500")
root.iconbitmap("img.ico")   
root.title("COVID-19 DATA TRACKER")
root.configure(background="white")
f = ("helvetica", 18 , "bold")
banner = tk.PhotoImage(file="corona.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack() 

entry = tk.Label(root, font=f, text="Enter the country name:")
entry.pack()

textfield = tk.Entry(root, width=40,)
textfield.pack()

mainlabel = tk.Label(root, text=get_covid_data(), font=f , bg="white")
mainlabel.pack()

gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=country_data)
gbtn.pack()

rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()

#thead

n1 = threading.Thread(target=notifications)
n1.setDaemon(True)
n1.start()


root.mainloop()
    



