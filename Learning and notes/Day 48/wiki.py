from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

all_numbers = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")
english_articles = all_numbers[1]
#english_articles.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

#driver.quit()