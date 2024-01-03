
import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By









#url of website
url="https://aividur.com/AskQuestion"

options=webdriver.ChromeOptions()
#options.add_experimental_option("detach",True) #leaves browser open untill .close is used, good for debugging
options.add_argument("--headless=new")


driver=webdriver.Chrome(options=options) # will open chrome locally untill .close is used

# going to login page

urllogin="https://aividur.com/loginpage"
userid="kseth"
password="password1234"

driver.get(urllogin)

#enter userid and password

useridtext=driver.find_element(By.ID,"UserID")
useridtext.send_keys(userid)
passwordtext=driver.find_element(By.ID,"Password")
passwordtext.send_keys(password)
loginbutton=driver.find_element(By.ID,"login")
loginbutton.click()

#changing to question url
driver.get(url)

while(driver.current_url != url):
    # waiting for website to update without this url
    # is not updated but program continues causing errors
    time.sleep(1)
    driver.get(url)

#changing to world cup cricket bot
bottype= Select(driver.find_element(By.ID,"assistantDropdown"))
bottypetext=bottype.first_selected_option.text
print("before change")
print(bottypetext)

bottype.select_by_value("AWorldCupCricketBot")
# bottypetext=bottype.first_selected_option.text  gets selected value of dropdown menu
bottypetext=bottype.first_selected_option.text

print("after change")
print(bottypetext)

#this will be the data collected from exotel to be entered into the bot
data_to_enter="did Australia win against India?"

textbox=driver.find_element(By.ID,"question") #textbox to enter question

#entering data into textbox
textbox.send_keys(data_to_enter)

print("textbox value")
print(textbox.text)
#submitting the question to the bot
submitbutton=driver.find_element(By.ID,"askButton") #the submit button

submitbutton.click() #selecting and clicking


#retrieving what the bot says back

botanswer=driver.find_element(By.ID,"answerText")


while(botanswer.text==""):
    time.sleep(1)
    # using sleep to allow for website to update text without this messages are blank









answer=botanswer.text

print("bot text ")
print(answer)



driver.quit()
print("quitting driver")

