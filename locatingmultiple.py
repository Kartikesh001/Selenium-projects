from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Initialize WebDriver
driver = webdriver.Chrome()

# Set your query
query = "laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=82JPIJIXTHA6&sprefix=laptop%2Caps%2C230&ref=nb_sb_noss_1")

    # Allow time for the page to load
    time.sleep(2)

    # Find all elements with the class "aok-relative" (you can replace this class if it is not the one you want)
    elems = driver.find_elements(By.CLASS_NAME, "aok-relative")  # Use find_elements to get all matching elements

    # Print the number of items found
    print(f"{len(elems)} items found")

    # Loop through the elements and print their text
    for elem in elems:
        print(elem.text)

    # Close the browser
    driver.close()
