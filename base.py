from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set the path to the ChromeDriver executable
chromedriver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Set the API URL
api_url = 'https://www.googleapis.com/books/v1/volumes?q=kaplan%20test%20prep'

# Set the number of times to hit the URL
num_requests = 10000

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening a window)

# Create a new Chrome session
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Send requests to the API URL
for _ in range(num_requests):
    driver.get(api_url)
    time.sleep(0.005)  # Add a delay to avoid overwhelming the server

# Close the Chrome session
driver.quit()
