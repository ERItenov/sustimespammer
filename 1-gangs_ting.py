#Kør kun denne fil 1 gang på din computer, så er de rette dependencies installeret

import subprocess
import sys
subprocess.run([sys.executable, '-m', 'pip3', 'install', '--user', 'selenium'])
subprocess.run([sys.executable, '-m', 'pip3', 'install', '--user', 'webdriver-manager'])
