###############################################################################
#Ændr INTET nedenunder denne linje! (Hvis du vil have det til at virke, altså.)
###############################################################################

#Hvor lang tid skal fanerne være åbne (sekunder)? Brug punktum, ikke komma.
tid = 50

#Hvor mange faner skal åbne?
faner = int(input('Hvor mange faner skal åbnes?'))


#delay mellem hver faneåbning i sekunder (0 minimerer delay) Brug punktum, ikke komma. Der er omkring 0.3 sekunders
#uundgåeligt delay, som man ikke kan slå fra
delay = int(input('Hvor langt delay skal der være mellem dem? (sekunder). Der er et delay på ca. 0,2 sekunder by default.'))


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

final_faner = faner - 1

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#Funktionen til at åbne siden og trykke på knappen
def sus():
    driver.get('https://www.sustime.dk')
    driver.find_element(By.XPATH, '//*[@id="systime"]/div/div[2]/div/div[2]/div/div[3]/button').send_keys(Keys.RETURN)

#laver og åbner ny fane, og åbner sustime i den
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

#åbner browseren
sus()
#loopet til at åbne flere tabs
#grunden til, at if else statementet for delay er udenfor funktionen er, at jeg ikke vil spilde
#så meget som et millisekund af min amogus-tid på at checke en funktion i stedet for at amoguse
if delay <= 0:
    for i in range(int(final_faner)):
        fane(i)
    time.sleep(tid)
else:
    for i in range(int(final_faner)):
        fane(i)
        time.sleep(delay)
    time.sleep(tid)
