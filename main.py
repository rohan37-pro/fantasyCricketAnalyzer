import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def search_t20_world_cup(browser='chrome'):
    # Set up the browser
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        print("Unsupported browser. Supported browsers are 'chrome' and 'firefox'.")
        return
    
    # Open Google
    driver.get('https://m.cricbuzz.com/cricket-series/7476/icc-mens-t20-world-cup-2024/matches')
    time.sleep(2)

    #driver.execute_script("window.scrollBy(0, 350)")
    #target_element = driver.find_element((By.XPATH, 'span.cbPlusIco.cbCrtIcnDark.rotate-90.dark\\:cbCrtIcn'))
    
    #target_element.click()

    
    input("Press Enter to quit...")

    # Close the browser
    driver.quit()

search_t20_world_cup()


