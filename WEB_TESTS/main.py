from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to the webdriver executable (you need to download the appropriate driver for your browser)
# Download ChromeDriver: https://sites.google.com/chromium.org/driver/
driver_path = 'path/to/chromedriver'

# Initialize the Chrome webdriver
driver = webdriver.Chrome(executable_path=driver_path)

# Open Google's homepage
driver.get("https://www.google.com")

# Find the search input field by its name attribute (assuming it's named 'q')
search_box = driver.find_element("name", "q")

# Type the search query
search_box.send_keys("Python programming")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for a moment to ensure search results are loaded
time.sleep(2)

# Capture the search results
search_results = driver.find_elements_by_css_selector('h3')  # Assuming search results are represented by h3 tags

# Print the search results titles
for result in search_results:
    print(result.text)

# Close the browser window
driver.quit()
