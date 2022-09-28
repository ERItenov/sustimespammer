import PySimpleGUI as sg

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

def sus():
    driver.get('https://www.sustime.dk')
    driver.find_element(By.XPATH, '//*[@id="systime"]/div/div[2]/div/div[2]/div/div[3]/button').send_keys(Keys.RETURN)

def fane(n):
    # definerer navnet på nuværende fane
    fanenavn = "fane " + str(n)
    # definerer kommandoen der skal køres som javascript for driveren, laver en ny tab og navngiver den
    window_open = str("window.open('about:blank', '" + fanenavn + "'" + ');')
    # kører javascript-kommandoen
    driver.execute_script(str(window_open))
    # skifter til det rigtige tab
    driver.switch_to.window(fanenavn)
    sus()

def sustime(delay, faner):
    sus()
    final_faner = faner - 1
    if delay <= 0:
        for i in range(int(final_faner)):
            fane(i)
        time.sleep(tid)
    else:
        for i in range(int(final_faner)):
            fane(i)
            time.sleep(delay)
        time.sleep(tid)

layout = [
    [sg.Text("Hvor mange faner?"),
     sg.In(size=(10, 2), enable_events=True, key='-Times-')
    ],
    [
        sg.Text("Hvor mange sekunders ekstra forsinkelse skal der være?"),
        sg.In(size=(10, 2), enable_events=True, key='-Delay-')
    ],
    [
        sg.Button("Start", key="--Start--")
    ]
 ]

window = sg.Window("sustimespammer", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '--Start--':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        delay = int(values["-Delay-"])
        times = int(values["-Times-"])
        print(str(delay))
        print(str(times))
        sustime(delay, times)
