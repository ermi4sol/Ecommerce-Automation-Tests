# Ecommerce Automation Tests

This project contains a set of automated tests for an ecommerce website using Selenium WebDriver with Python. These tests demonstrate my skills in test automation, particularly for web applications.

## Project Overview

The project includes three main test scripts:

1. `product_search.py`: Searches for products in the 'Laptops' category and lists them.
2. `add_to_cart.py`: Adds a product to the cart and verifies its presence.
3. `checkout_process.py`: Completes the entire purchase process from product selection to order confirmation.

These tests are designed to run on the demo website [https://www.demoblaze.com](https://www.demoblaze.com), which is a sample ecommerce platform.

## Technologies Used

- Python
- Selenium WebDriver
- ChromeDriver
- webdriver_manager

## Setup and Installation

1. Ensure you have Python installed on your system. This project was developed with Python 3.x.

2. Clone this repository:
   ```
   git clone https://github.com/ermi4sol/Ecommerce-Automation-Tests.git
   cd ecommerce-automation-tests
   ```

3. Install the required packages:
   ```
   pip install selenium webdriver_manager
   ```

## Running the Tests

To run each test script, use the following commands:

1. Product Search Test:
   ```
   python product_search.py
   ```

2. Add to Cart Test:
   ```
   python add_to_cart.py
   ```

3. Checkout Process Test:
   ```
   python checkout_process.py
   ```

## Test Descriptions

### Product Search Test (`product_search.py`)
This test navigates to the 'Laptops' category and prints out the names of all available laptop products.

### Add to Cart Test (`add_to_cart.py`)
This test selects the first laptop from the 'Laptops' category, adds it to the cart, and verifies that the product is correctly added to the cart.

### Checkout Process Test (`checkout_process.py`)
This test simulates the entire purchasing process:
1. Selects a laptop
2. Adds it to the cart
3. Proceeds to checkout
4. Fills in order details
5. Completes the purchase
6. Verifies the confirmation message

## Notes

- These tests use implicit waits and sleep times to handle page loading. In a production environment, it would be better to use explicit waits for more reliable test execution.
- The tests are designed for demonstration purposes and may need adjustments for use in a real-world testing scenario.

## Future Improvements

- Implement a test suite to run all tests sequentially
- Add more detailed error handling and logging
- Implement parameterized testing for different products and categories
- Create a configuration file for test data and website URLs

## Contributing

This is a personal project for my portfolio, but I welcome any suggestions or feedback. Please feel free to open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).