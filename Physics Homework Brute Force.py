# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:25:28 2022

@author: Matthew
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import tkinter as tk
from tkinter import simpledialog


urlquestion = tk.Tk()
urlquestion.geometry("200x100")
theurl = simpledialog.askstring("Input","Please go into the quiz and copy paste the URL in here :)",parent=urlquestion)
urlquestion.destroy()


usernamequestion = tk.Tk()
usernamequestion.geometry("200x100")
theusername = simpledialog.askstring("Input","Username Please :)",parent=usernamequestion)
usernamequestion.destroy()



passwordquestion = tk.Tk()
passwordquestion.geometry("200x100")
thepassword = simpledialog.askstring("Input","Password Please :)",parent=passwordquestion)
passwordquestion.destroy()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get(theurl)

#driver.get("https://moodle.gatewayk12.org/2425/mod/quiz/attempt.php?attempt=799&cmid=2090&page=0")

time.sleep(2)

# Locate elements and perform actions
username = driver.find_element(By.XPATH,  "//input[@name='username']")

username.send_keys(theusername)

password = driver.find_element(By.XPATH,  "//input[@name='password']")
password.send_keys(thepassword)

logInButton = driver.find_element(By.XPATH, "//button[@id='loginbtn']")
logInButton.click()

driver.implicitly_wait(3)


ProblemNum = 1


while ProblemNum <= 20:
    isCorrect = driver.find_element(By.CLASS_NAME, "state")
    currentNum = 10
    thousandCoveredFlag = False
    hundredCoveredFlag = False
    tensCoveredFlag = False
    onesCoveredFlag = False
    decimalsCoveredFlag = False

    while (str(isCorrect.text) == "Incorrect" or str(isCorrect.text) == "Not complete"):
        answerbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']")))
        #answerbox = driver.find_element(By.XPATH,"//input[@type='text']")
        answerbox.clear()
        answerbox.send_keys(str(currentNum))
        checkbutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
        #checkbutton = driver.find_element(By.XPATH, "//button[@type='submit']")
        checkbutton.click()


        isCorrect = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"state")))
        #isCorrect = driver.find_element(By.CLASS_NAME, "state")

        if currentNum < 100 and currentNum >= 10 and onesCoveredFlag == False:
            currentNum += 0.1

        if currentNum > 100 and tensCoveredFlag == False:
            currentNum = 0
            tensCoveredFlag = True

        if currentNum < 10 and hundredCoveredFlag == False:
            currentNum += 0.01
            onesCoveredFlag = True

        if currentNum > 10 and onesCoveredFlag and tensCoveredFlag and not thousandCoveredFlag:
            if not hundredCoveredFlag:
                currentNum = 100
                hundredCoveredFlag = True
            currentNum += 1

        if currentNum > 999 and not decimalsCoveredFlag:
            currentNum = 0
            decimalsCoveredFlag = True

        if currentNum < 1 and decimalsCoveredFlag:
            currentNum += 0.001

        if currentNum > 1 and decimalsCoveredFlag and not thousandCoveredFlag:
            currentNum = 1000
            thousandCoveredFlag = True

        if currentNum < 10000 and thousandCoveredFlag:
            currentNum += 10

        if currentNum >= 10000:
            currentNum += 100

        if currentNum > 100000:
            print("BruteForceFailed")
            break

    currentNum = 10
    ProblemNum += 1
    NextButton = driver.find_element(By.ID, "mod_quiz-next-nav")
    NextButton.click()

    driver.implicitly_wait(3)


driver.quit()