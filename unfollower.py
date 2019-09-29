from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import sys

if(len(sys.argv) <= 2):
    print("python3 unfollower.py username password")
    quit()

base_url = "https://www.instagram.com/"


driver = webdriver.Chrome(ChromeDriverManager().install())

while (driver.current_url != base_url):
    driver.get(base_url+"accounts/login")
    time.sleep(2.0)
    driver.find_element_by_name("username").send_keys(sys.argv[1])
    driver.find_element_by_name("password").send_keys(sys.argv[2])
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5.0)
print("Logged into user {username}".format(username=sys.argv[1]))

driver.get(base_url+sys.argv[1])
print("Getting user page")

#driver.find_element_by_xpath("//*[@id='react-root']/section/footer/div/nav/ul/li[11]/span/select").click()
#time.sleep(1.0)
#driver.find_element_by_xpath("//*[@id='react-root']/section/footer/div/nav/ul/li[11]/span/select/option[6]").click()
#time.sleep(1.0)

follow_link = driver.find_element_by_xpath("//a[@href='/{username}/following/']".format(username=sys.argv[1]))

while not driver.current_url == (base_url+sys.argv[1]+"/following/"):
    follow_link.click()
    print("Clicking folowers")
    time.sleep(2.0)

attempts = 0
while True:
    ran = random.uniform(1.0,20.0)
    try:

        followed = driver.find_element_by_xpath("//button[contains(text(),'Following')]")
        if followed == None:
            input("No followers... Press enter to exit")
            quit()
        print(str(followed))
        followed.click()
        if driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]") != None:
            driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]").click()
        attempts += 1
    except:
        print("Failed unfollowing, trying again")
    print("Unfollowed: {attempts} and sleeping {seconds} seconds".format(attempts=attempts,seconds=ran))
    time.sleep(ran)
