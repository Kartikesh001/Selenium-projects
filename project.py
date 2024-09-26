import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Initialize WebDriver
driver = webdriver.Chrome()

# Set your query
query = "laptop"

# Create a folder to store the data
os.makedirs("data", exist_ok=True)

# Initialize the file counter
file_counter = 1

for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=82JPIJIXTHA6&sprefix=laptop%2Caps%2C230&ref=nb_sb_noss_1")

    
    time.sleep(2)

   
    elems = driver.find_elements(By.CLASS_NAME, "aok-relative")  # Use find_elements to get all matching elements

    print(f"{len(elems)} items found on page {i}")

    # Loop through each found element
    for elem in elems:
        # Get the text or HTML data
        d = elem.get_attribute("outerHTML")
        
        # Save the data to a file with a unique name
        with open(f"data/{query}_{file_counter}.html", "w", encoding="utf-8") as f:
            f.write(d)
        
        # Increment the file counter
        file_counter += 1

# Close the browser after all pages are processed
driver.close()
