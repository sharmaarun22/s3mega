from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import time

# mention the driver location
serv_obj = Service('C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()

try:
    driver.get("https://mega.io/desktop#downloadapps")

    linux_locator = driver.find_element(By.XPATH, "//h6[normalize-space()='Linux']")
    driver.execute_script("arguments[0].scrollIntoView();", linux_locator)

    time.sleep(1)

    linux_locator.click()

    download_links = driver.find_elements(By.XPATH, "//div/a[normalize-space()='Download']")
    invalid_links = 0

    for download_link in download_links:
        link = download_link.get_attribute("href")
        if "linux" in link:
            try:
                res = requests.head(link)
                if res.status_code > 400:
                    print(f"{link} is an invalid link")
                    invalid_links += 1
                else:
                    print(f"{link} is valid")
            except Exception as e:
                print(f"server error: {e}")

    if not invalid_links:
        print("\n*********All the Download links are working fine.*********")
    else:
        print(f"Total invalid links are {invalid_links}")

finally:
    driver.quit()

