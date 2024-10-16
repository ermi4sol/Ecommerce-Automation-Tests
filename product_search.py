from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the e-commerce website
    driver.get("https://www.demoblaze.com")

    # Wait for the page to load fully
    driver.implicitly_wait(10)  # Wait up to 10 seconds

    # Locate the product category (Example: Laptops) and click on it
    laptop_category = driver.find_element(By.LINK_TEXT, "Laptops")
    laptop_category.click()

    # Give some time for products to load
    time.sleep(3)

    # Extract the product titles
    products = driver.find_elements(By.CLASS_NAME, "card-title")
    
    if products:
        print("Products found:")
        for product in products:
            print(product.text)
    else:
        print("No products found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
