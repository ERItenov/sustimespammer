import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

def sustime(delay, faner, tid):
    final_faner = faner - 1

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Funktionen til at åbne siden og trykke på knappen
    def sus():
        driver.get('https://www.sustime.dk')
        driver.find_element(By.XPATH, '//*[@id="systime"]/div/div[2]/div/div[2]/div/div[3]/button').send_keys(
            Keys.RETURN)

    # laver og åbner ny fane, og åbner sustime i den
    def fane(n):
        # definerer navnet på nuværende fane
        fanenavn = "fane " + str(n)
        # definerer kommandoen der skal køres som javascript for driveren, laver en ny fane og navngiver den
        window_open = str("window.open('about:blank', '" + fanenavn + "'" + ');')
        # kører javascript-kommandoen
        driver.execute_script(str(window_open))
        # skifter til det rigtige tab
        driver.switch_to.window(fanenavn)
        sus()

    # åbner browseren
    sus()
    time.sleep(delay)
    # loopet til at åbne flere tabs
    # grunden til, at if else statementet for delay er udenfor funktionen er, at jeg ikke vil spilde
    # så meget som et millisekund af min amogus-tid på at checke en funktion i stedet for at amoguse
    if delay <= 0:
        for i in range(int(final_faner)):
            fane(i)
        time.sleep(tid)
    else:
        for i in range(int(final_faner)):
            fane(i)
            time.sleep(delay)
        time.sleep(tid)


class input(QLineEdit):
    def __init__(self, placeholder, xpos, ypos, parent):
        super().__init__()
        self.move(int(xpos), int(ypos))
        self.setPlaceholderText(str(placeholder))
        self.setParent(parent)
        self.setValidator(QIntValidator())
        self.setFixedSize(200, 20)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("SusTimeSpammer")
        self.setContentsMargins(20,20,20,20)

        self.faner = input("Faner", 20, 50, self)
        self.delay = input("Ekstra forsinkelse (sekunder)", 20, 70, self)
        self.tid = input("Tid åbent (i sekunder)", 20, 90, self)

        button = QPushButton("Start", self)
        button.clicked.connect(self.func)
        button.clicked.connect(lambda:self.close())
        button.move(200, 150)
    def func(self):
        self.close()
        sustime(int(self.delay.text()), int(self.faner.text()), int(self.tid.text()))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
