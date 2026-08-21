# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# define url
url = "https://seleniumbase.io/other/drag_and_drop"

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# find the source
source = driver.find_element(By.XPATH, '//*[@id="drag1"]')

# find the destination
destination = driver.find_element(By.XPATH, '//*[@id="div1"]')

actions=ActionChains(driver) 
#driver.execute_script("window.scrollTo(0, window.scrollY + 200)") 
actions.drag_and_drop(source,destination).perform() 

# pause the program for 5 seconds to view the results
sleep(5)

