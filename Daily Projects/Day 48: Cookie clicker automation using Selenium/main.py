from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)
language_button = driver.find_element(By.ID, value="langSelect-EN")
language_button.click()

sleep(5)

cookie = driver.find_element(By.ID, value="bigCookie")

store_items = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except ValueError:
            print("Couldn't find cookie count or items")

        timeout = time() + wait_time

    if time() > five_min:
        cookies_element = driver.find_element(By.ID, value="cookies")
        print(f"Final result: {cookies_element.text}")
        break
