from setuptools import setup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
#######################################################
#Customizables:

#Hvor lang tid skal fanerne være åbne (sekunder)?
tid = 60

#Hvor mange faner skal åbne?
faner = 10


#delay mellem hver faneåbning (0 slår delay fra)
delay = 0

###############################################################################
#Ændr INTET nedenunder denne linje! (Hvis du vil have det til at virke, altså.)
###############################################################################

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#Funktionen til at åbne siden og trykke på knappen
def sus():
    driver.get('https://www.sustime.dk')
    driver.find_element(By.XPATH, '//*[@id="systime"]/div/div[2]/div/div[2]/div/div[3]/button').send_keys(Keys.RETURN)

#åbner browseren
sus()
#loopet til at åbne flere tabs
#grunden til, at if else statementet for delay er udenfor funktionen er, at jeg ikke vil spilde
#så meget som en millisekund af mit amogus tid på at checke en funktion i stedet for at amoguse
if delay <= 0:
    for i in range(int(faner)):
        #definerer navnet på nuværende fane
        fanenavn = "fane " + str(i)
        #definerer kommandoen der skal køres som javascript for driveren, laver en ny tab og navngiver den
        window_open = str("window.open('about:blank', '" + fanenavn + "'"+');')
        #kører javascript-kommandoen
        driver.execute_script(str(window_open))
        #skifter til det rigtige tab
        driver.switch_to.window(fanenavn)
        sus()
else:
    for i in range(int(faner)):
        # definerer navnet på nuværende fane
        fanenavn = "fane " + str(i)
        # definerer kommandoen der skal køres som javascript for driveren, laver en ny tab og navngiver den
        window_open = str("window.open('about:blank', '" + fanenavn + "'" + ');')
        # kører javascript-kommandoen
        driver.execute_script(str(window_open))
        # skifter til det rigtige tab
        driver.switch_to.window(fanenavn)
        sus()
        time.sleep(delay)
time.sleep(tid)