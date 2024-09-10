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


username = driver.find_element_by_name("username")
username.send_keys(theusername)
password = driver.find_element_by_name("password")
password.send_keys(thepassword)
signInButton = driver.find_element_by_name("signin")
signInButton.click()
driver.implicitly_wait(3)
yes = driver.find_element_by_xpath("/html/body/app-root/secure/div/app-header/div/div[3]/div/cl-input/div/input")
yes.send_keys("Moodle")
yes.send_keys(Keys.ENTER)



handles = driver.window_handles
driver.switch_to.window(handles[1])

ProblemNum = 1

questionAttemptTotal = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div[2]/div/section/div[2]/form/div/div[1]')
questionAttemptPart = questionAttemptTotal.get_attribute("id")[9:13]

    
while ProblemNum <= 20:
    isCorrect = driver.find_element_by_class_name("state")
    currentNum = 10
    thousandCoveredFlag = False
    hundredCoveredFlag = False
    tensCoveredFlag = False
    onesCoveredFlag = False
    decimalsCoveredFlag = False


    answerboxID = "q"+questionAttemptPart+":"+str(ProblemNum)+"_answer"
    checkButtonID = "q"+questionAttemptPart+":"+str(ProblemNum)+"_-submit"
    
    while (str(isCorrect.text) == "Incorrect" or str(isCorrect.text) == "Not complete"):
        

        
        
        answerbox = driver.find_element_by_id(answerboxID)
        answerbox.clear()
        answerbox.send_keys(str(currentNum))
        checkbutton = driver.find_element_by_id(checkButtonID)
        checkbutton.click()
        isCorrect = driver.find_element_by_class_name("state")
        if currentNum < 100 and currentNum >= 10 and onesCoveredFlag == False:
            currentNum+=0.1
            
            
        if currentNum > 100 and tensCoveredFlag == False:
            currentNum = 0    #here
            tensCoveredFlag = True
            
            
        if currentNum < 10 and hundredCoveredFlag == False:
            currentNum+=0.01
            onesCoveredFlag = True
            
            
        if currentNum > 10 and onesCoveredFlag == True and tensCoveredFlag == True and thousandCoveredFlag == False:
            if hundredCoveredFlag == False:
                currentNum = 100
                hundredCoveredFlag = True
            currentNum+=1
            
            
        if(currentNum > 999 and decimalsCoveredFlag == False):
            currentNum= 0    #here
            decimalsCoveredFlag = True
            
            
        if (currentNum < 1 and decimalsCoveredFlag == True):
            currentNum+=0.001
            
            
        if (currentNum > 1 and decimalsCoveredFlag == True and thousandCoveredFlag == False):
            currentNum = 1000
            thousandCoveredFlag = True
            
            
        if (currentNum < 10000 and thousandCoveredFlag == True):
            currentNum += 10
            
            
        if currentNum >= 10000:
            currentNum +=100
        
        if currentNum > 100000:
            print("printBruteForceFailed")
            break
        
    currentNum = 10   
    ProblemNum+=1
    NextButton = driver.find_element_by_id("mod_quiz-next-nav")
    NextButton.click()
    driver.implicitly_wait(3)
