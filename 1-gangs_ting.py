#Kør kun denne fil 1 gang på din computer, så er de rette dependencies installeret

import subprocess
import sys
subprocess.run([sus.executable, '-m', 'pip', 'install', 'selenium'])
subprocess.run([sus.executable, '-m', 'pip', 'install', 'webdriver-manager'])
