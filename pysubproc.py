import os
import sys
import time
import subprocess
# import tkinter as tk
# import mysql.connector as mysql

calculatorfile = "./pycalculator.py"
calculatorfile2 = "./pycalculator2.py"

def main():
    
    p1 = subprocess.Popen([sys.executable, calculatorfile])
    p2 = subprocess.Popen([sys.executable, calculatorfile2])
    
    p1.wait()
    p2.wait()
    # Wait for both processes to complete
    # p1.terminate()
    # p2.terminate()
    # p1.kill()
    # p2.kill()
    # p1.communicate()
    # p2.communicate()
    # p1.stdout.close()
    # p2.stdout.close()
    # p1.stderr.close()
    # p2.stderr.close()
    # p1.stdin.close()
    # p2.stdin.close()
    # p1.stdout.flush()
    # p2.stdout.flush()
    # p1.stderr.flush()
    # p2.stderr.flush()
    # p1.stdin.flush()
    # p1.stdout.read()
    # p2.stdin.read()
    # p1.stderr.read()
    
if __name__ == "__main__":
    main()
    # p1 = subprocess.Popen(['python', calculatorfile])
    # p2 = subprocess.Popen(['python', calculatorfile2])
    # p1.wait()
    # p2.wait()
    # time.sleep(5)
    # os.system('taskkill /f /im python.exe')
    # os.system('taskkill /f /im pythonw.exe')