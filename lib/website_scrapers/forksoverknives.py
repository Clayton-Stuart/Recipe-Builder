from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    from recipe_scraper_utilities import recipe
else:
    from lib.website_scrapers.recipe_scraper_utilities import recipe

def readURL(url, FireFox=False):
    if FireFox:
        profile = webdriver.FirefoxOptions()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)

        profile.set_preference("--headless")

        driver = webdriver.Chrome(options=profile)
        driver.delete_all_cookies()
    
    else:
        options = Options()
        options.add_argument('user-agent=rand')
        options.add_argument("--ignore-certificate-errors");
        options.add_argument("--disable-popup-blocking");
        options.add_argument('--incognito')
        options.add_argument('--disable-back-forward-cache')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disk-cache-size=0')
        options.add_argument('--gpu-disk-cache-size-kb=0')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--aggressive-cache-discard')
        
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(options=options)
        driver.delete_all_cookies()

    driver.get(url)
    steps_output = []
    steps_header_output = []

    name = driver.find_elements(By.TAG_NAME, "h1")[0].text
    ingredients_output = driver.find_elements(By.CLASS_NAME, "mb-8")[0].text
    
    steps_block = driver.find_elements(By.CLASS_NAME, "mb-8")[1]
    steps_block_ls = steps_block.find_elements(By.TAG_NAME, "li")

    for i in range(len(steps_block_ls)):
        steps_output.append(steps_block_ls[i].text)
        steps_header_output.append("Step " + str(i+1))


    return recipe(name=name, ingredients=ingredients_output, steps=steps_output, titles=steps_header_output)