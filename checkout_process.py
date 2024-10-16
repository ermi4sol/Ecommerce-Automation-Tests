from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open the e-commerce website
    driver.get("https://www.demoblaze.com")
    driver.implicitly_wait(10)  # Ensure page loads fully

    # Step 2: Click on the 'Laptops' category
    laptop_category = driver.find_element(By.LINK_TEXT, "Laptops")
    laptop_category.click()
    time.sleep(10)  # Give time for the products to load

    # Step 3: Click on the first product in the list
    first_product = driver.find_elements(By.CLASS_NAME, "hrefch")[0]
    product_name = first_product.text  # Store the product name
    print(f"Selected Product: {product_name}")
    first_product.click()

    # Step 4: Click the 'Add to Cart' button
    time.sleep(10)  # Ensure the product page is fully loaded
    add_to_cart_button = driver.find_element(By.LINK_TEXT, "Add to cart")
    add_to_cart_button.click()

    # Step 5: Handle the alert that appears
    time.sleep(10)  # Wait for the alert
    alert = driver.switch_to.alert
    alert.accept()

    # Step 6: Go to the cart and verify the product
    driver.find_element(By.LINK_TEXT, "Cart").click()
    time.sleep(10)  # Wait for the cart page to load
    
    # Step 7: Click the 'place order' button
    place_order = driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]")
    place_order.click()
    time.sleep(10)
    
    # Step 8: Fill the order details
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "city").send_keys("New York")
    driver.find_element(By.ID, "card").send_keys("1234567812345678")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")

    # Step 9: Click the 'Purchase' button
    purchase = driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]")
    purchase.click()
    time.sleep(10)
    
    # Step 10: capture and print the confirmation message
    confirmation_message = driver.find_element(By.XPATH, "//h2").text
    print(f"Confirmation Message: {confirmation_message}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
    