import requests
from bs4 import BeautifulSoup
import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=700)
window.config(padx=20, pady=20)

target_url = "https://news.ycombinator.com/"
link_array = []


def make_request():
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def link_text():
    link_soup = make_request()
    for link in link_soup.find_all("span", attrs={"class": "titleline"}):
        link_array.append(str(link.text).split("(")[0])


def text_insert():
    for link in link_array:
        note_text.insert("1.0", link+"\n")


def news_click():
    text_insert()


link_text()

tk_btn = tkinter.Button(text="NEWS", command=news_click)
tk_btn.pack()

note_text = tkinter.Text()
note_text.config(width=400, height=560)
note_text.pack()

window.mainloop()
