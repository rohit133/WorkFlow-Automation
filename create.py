import subprocess
import sys
import os
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


directory = "E:\Projects-GitHub\My Projects"
browser = webdriver.Chrome(executable_path=r"C:\Dev\chromedriver.exe")
browser.get("https://github.com/login")


def create():
    folderName = sys.argv[1]
    path = os.path.join(directory,folderName)
    os.makedirs(path)

    userName = browser.find_element(By.XPATH,"//*[@id='login_field']")
    userName.click()
    userName.send_keys("Your UserName") # use your username 

    passWord = browser.find_element(By.XPATH,"//*[@id='password']")
    passWord.click()
    passWord.send_keys("Your Password") # Use your Password

    submit = browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[11]")
    submit.click()


#   Creating new Repo 
    browser.get("https://github.com/new")
    NewRepo = browser.find_element(By.XPATH,"//*[@id='repository_name']")
    NewRepo.click()
    NewRepo.send_keys(folderName)  
    
    
#   Submitting request 
    create_btn = browser.find_element(By.XPATH,"//*[@id='new_repository']/div[5]/button")
    time.sleep(5)
    create_btn.click()


#   remote access 
    hasCode = browser.find_element(By.XPATH,"//*[@id='empty-setup-push-repo-echo']/span[1]")
    print(hasCode.text)
    p = subprocess.Popen("create.cmd", stdin = subprocess.PIPE)
    time.sleep(2)

    browser.close()


    print("***** Work Flow Ready! *****")

if __name__ == "__main__" :
    create()