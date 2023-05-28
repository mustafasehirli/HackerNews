import requests
from bs4 import BeautifulSoup
import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=700)
window.config(padx=20, pady=20)

target_url = "https://news.ycombinator.com/"
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')
link_array = []

for link in soup.find_all("span", attrs={"class": "titleline"}):
    link_array.append(link.text)


print(link_array[0])
window.mainloop()