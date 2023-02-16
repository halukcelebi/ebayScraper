from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://www.ebay.de/itm/304698405920?hash=item46f170b420:g:7lwAAOSwKCZjbezX";

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url);
#
#pic_url = driver.find_elements(By.CLASS_NAME,"d-picture-minview__container");
#pic_url = driver.find_elements(By.CLASS_NAME,"d-picture-minview__container");
#pic_url = driver.find_elements(By.CLASS_NAME,"ux-image-filmstrip-carousel");
#pic_url = driver.find_elements(By.CLASS_NAME,"ux-image-filmstrip-carousel-item");
#pic_url = driver.find_elements(By.CLASS_NAME,"g-hdn");



"""
#to get all links 
pic_url = driver.find_elements(By.XPATH,"//a[@href]")
print(pic_url)
for pc in pic_url: 
    url_ = pc.get_attribute("href");
    print(url_)
    print(pc.text)
    print('\n')

"""
wait = WebDriverWait(driver, 50)
t = time.time()

product_img_xpath = '//div[contains(@class,"s-item")]//img'

try:
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'Export_XLSX_Normal') and contains(@onclick, 'captureDomEvent')]"))).click()
    
    """
    
    wait.until(EC.visibility_of_element_located((By.XPATH, product_img_xpath)))
    time.sleep(1)
    imgs = driver.find_elements_by_xpath(product_img_xpath)
    for img in imgs:
        print(img.get_attribute('href'))
    """    
except: 
    elapsed = time.time() - t ;
    print(elapsed); 



"""
product_img_xpath = '//div[contains(@class,"s-item")]//img'
elems = driver.find_elements(By.XPATH,product_img_xpath)
for elem in elems:
    print(elem.get_attribute('src'))

"""

driver.quit();