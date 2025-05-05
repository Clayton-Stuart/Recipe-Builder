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
    ingredients_output = []
    steps_output = []
    steps_header_output = []

    name = driver.find_elements(By.CLASS_NAME, "tasty-recipes-title")[0].text
    ingredients_body = driver.find_elements(By.CLASS_NAME, "tasty-recipes-ingredients-body")[0]
    titles = ingredients_body.find_elements(By.TAG_NAME, "h4")
    ingredients = ingredients_body.find_elements(By.TAG_NAME, "ul")

    if len(titles) == len(ingredients):
        for i in range(len(titles)):
            ingredients_output.append("<h>" + titles[i].text)
            for j in range(len(ingredients[i].find_elements(By.TAG_NAME, "li"))):
                ingredients_output.append(ingredients[i].find_elements(By.TAG_NAME, "li")[j].text)

    elif len(titles) < len(ingredients):
        for j in range(len(ingredients[0].find_elements(By.TAG_NAME, "li"))):
            ingredients_output.append(ingredients[0].find_elements(By.TAG_NAME, "li")[j].text)
        del ingredients[0]
        for i in range(len(titles)):
            ingredients_output.append("<h>" + titles[i].text)
            for j in range(len(ingredients[i].find_elements(By.TAG_NAME, "li"))):
                ingredients_output.append(ingredients[i].find_elements(By.TAG_NAME, "li")[j].text)


    else:
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i].find_elements(By.TAG_NAME, "li"))):
                ingredients_output.append(ingredients[i].find_elements(By.TAG_NAME, "li")[j].text)

    # ingredients works
    steps_block = driver.find_elements(By.CLASS_NAME, "tasty-recipes-instructions-body")[0]
    steps = steps_block.find_elements(By.TAG_NAME, "li")

    for i in range(len(steps)):
        steps_header_output.append("Step " + str(i+1))
        steps_output.append(steps[i].text)


    return recipe(name=name, ingredients=ingredients_output, titles=steps_header_output, steps=steps_output)    