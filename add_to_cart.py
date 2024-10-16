from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open the e-commerce qwbsite
    driver.get("https://www.demoblaze.com")
    # To Ensure the page loads fully
    driver.implicitly_wait(10)
    
    #Step 2: Select the catagory 'Laptop'
    laptop_category = driver.find_element(By.LINK_TEXT, "Laptops")
    laptop_category.click()
    # Time for the products to load
    time.sleep(10)
    
    # Step 3: Click on the first product on the list
    first_product = driver.find_elements(By.CLASS_NAME, "hrefch")[0]
    product_name = first_product.text  # Store the product name
    print(f"Selected Product: {product_name}")
    first_product.click()
    # Ensure the product page is fully loaded
    time.sleep(10)
    
    # Step 4: Click the 'Add to cart' button
    add_to_cart = driver.find_element(By.LINK_TEXT, "Add to cart")
    add_to_cart.click()
    # Ensure the product page is fully loaded
    time.sleep(10)
    
    # Step 5: Handle the alert that appears
    alert = driver.switch_to.alert
    alert.accept()
    
    # Step 6: Verify the product is in the cart
    driver.find_element(By.LINK_TEXT, "Cart").click()
    # Wait fo the cart page to load
    time.sleep(10)
    
    # Retrieve product title and price from the cart
    cart_item_title = driver.find_element(By.XPATH, "//tr[@class='success']/td[2]").text
    cart_item_price = driver.find_element(By.XPATH, "//tr[@class='success']/td[3]").text

    # Print the product information
    print(f"Product successfully added to the cart!")
    print(f"Product Name: {cart_item_title}")
    print(f"Product Price: {cart_item_price}")

        
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
    