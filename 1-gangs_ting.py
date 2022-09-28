#Kør kun denne fil 1 gang på din computer, så er de rette dependencies installeret

import subprocess
import sys
subprocess.run([sys.executable, '-m', 'pip3.10', 'install', '--user', 'selenium'])
subprocess.run([sys.executable, '-m', 'pip3.10', 'install', '--user', 'webdriver-manager'])
subprocess.run([sys.executable, '-m', 'pip3.10', 'install', '--user', 'PyQt6'])
