from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(5)
username = browser.find_element(By.NAME,"username")
password = browser.find_element(By.NAME,"password")
time.sleep(5)
username.send_keys("YOUR-USERNAME")
password.send_keys("YOUR-PASSWORD")
time.sleep(2)
deneme =browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
deneme.click()
time.sleep(23)
arama = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div/div[2]/div/div")
arama.click()
time.sleep(3)
gereksiz = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
gereksiz.click()
time.sleep(5)
mes = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button")
mes.click()
time.sleep(3)
def mesaj1():
    kisi = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input")
    kisi.send_keys("Who you want to send")
    time.sleep(2)
    kisitik = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[3]/div/button")
    kisitik.click()
    time.sleep(2)
    gereksiz2 = browser.find_element(By.XPATH,
                                     "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div")
    gereksiz2.click()
    time.sleep(5)
    mesajasıl = browser.find_element(By.XPATH,
                                     "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    mesajasıl.send_keys("The message you want to send")
    time.sleep(2)
    gönder = browser.find_element(By.XPATH,
                                  "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div")
    gönder.click()
    time.sleep(5)
    gerigel = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[5]/div/a/div")
    gerigel.click()
    time.sleep(2)

def mesaj2():
    mes = browser.find_element(By.XPATH,
                               "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button")
    mes.click()
    kisi = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input")
    kisi.send_keys("Who you want to send")
    time.sleep(2)
    kisitik = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[3]/div/button")
    kisitik.click()
    time.sleep(2)
    gereksiz2 = browser.find_element(By.XPATH,
                                     "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div")
    gereksiz2.click()
    time.sleep(5)
    mesajasıl = browser.find_element(By.XPATH,
                                     "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    mesajasıl.send_keys("The message you want to send")
    time.sleep(2)
    gönder = browser.find_element(By.XPATH,
                                  "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div")
    gönder.click()
    time.sleep(5)
    gerigel = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[5]/div/a/div")
    gerigel.click()
    time.sleep(586)


mesaj1()
mesaj2()
browser.close()
