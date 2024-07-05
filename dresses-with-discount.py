from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    options=options
)
driver.get("https://www.koton.com/kadin-elbise/")

#get all women dresses
dresses = driver.find_elements(By.CLASS_NAME, "js-product-wrapper.product-item")

#find dresses which have discount
dresses_with_discount = []
for dress in dresses:
    try:
        sub1 = dress.find_element(By.CLASS_NAME, "product-item__info")
        sub2 = dress.find_element(By.CLASS_NAME, "product-item__info-box")
        discount = dress.find_element(By.CLASS_NAME, "product-item__info-campaign")
        if discount.text.strip():  
            dresses_with_discount.append(dress)
    except:
        continue

#extract their links
discounted_dress_links = []
for dress in dresses_with_discount:
    link = ""
    try:
        part = dress.get_attribute('data-url')
        link = "https://www.koton.com"+part
        discounted_dress_links.append(link)
    except:
        continue

#print discount links
for dress_link in discounted_dress_links:
    print(dress_link)
    print("/n")