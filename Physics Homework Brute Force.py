# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:25:28 2022

@author: Matthew
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
#driver.get("https://moodle.gatewayk12.org/2223/mod/quiz/attempt.php?attempt=4643&page=7&cmid=5885")#CHANGE LINK
driver.get("https://moodle.gatewayk12.org/2223/mod/quiz/attempt.php?attempt=4643&cmid=5885#question-5039-1")
username = driver.find_element_by_name("username")
username.send_keys("mxb100")
password = driver.find_element_by_name("password")
password.send_keys("405055")
signInButton = driver.find_element_by_name("signin")
signInButton.click()
driver.implicitly_wait(3)
yes = driver.find_element_by_xpath("/html/body/app-root/secure/div/app-header/div/div[3]/div/cl-input/div/input")
yes.send_keys("Moodle")
yes.send_keys(Keys.ENTER)




#maybe this registers the changes and I just need to delete the other files?

handles = driver.window_handles
driver.switch_to.window(handles[1])

print(driver.title)


NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()
NextButton = driver.find_element_by_id("mod_quiz-next-nav")
NextButton.click()


ProblemNum = 14

while ProblemNum <= 20:
    isCorrect = driver.find_element_by_class_name("state")
    currentNum = 10
    thousandCoveredFlag = False
    hundredCoveredFlag = False
    tensCoveredFlag = False
    onesCoveredFlag = False
    decimalsCoveredFlag = False


    answerboxID = "q5039:"+str(ProblemNum)+"_answer"
    checkButtonID = "q5039:"+str(ProblemNum)+"_-submit"

    while (str(isCorrect.text) == "Incorrect"):
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
