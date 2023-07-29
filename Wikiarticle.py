from bs4 import BeautifulSoup
import PySimpleGUI as sg
import webbrowser
import requests

sg.theme('DarkAmber')

column_to_be_centered = [[sg.Text(size=(50,5), font=('Courier New' ,25), justification='center')],
                         [sg.Text(size=(50,5), font=('Courier New' ,25), key='subj', justification='center')],
                         [sg.Button('Search', size=10, font=10)],
                         [sg.Button('Open', size=10, font=10), sg.Button('Exit', size=10, font=10)]]

layout = [[sg.VPush()],
          [sg.Push(), sg.Column(column_to_be_centered,element_justification='c'), sg.Push()],
          [sg.VPush()]]


window = sg.Window("Random Wikiarticle   *You Need To Be Connected To The WIFI*", layout, resizable=True, finalize=True)

while True:
    event, values = window.read()

    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    window['subj'].update(f'{title}')

    if event == "Open":
        url = f"https://en.wikipedia.org/wiki/{title}"
        webbrowser.open(url)
        break
    elif event == "Search":
        pass
    elif event == "Exit":
        break
    else:
        break

window.close()
