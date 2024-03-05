from selenium import webdriver

# Specify the path to the ChromeDriver executable
chrome_driver_path = "/path/to/chromedriver"

# Specify the path to the Chrome browser executable (optional, if not in the system PATH)
chrome_binary_path = "/path/to/chrome.exe"

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = (
    chrome_binary_path  # Uncomment if specifying the Chrome binary path
)

# Create a ChromeDriver instance
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Navigate to the specified URL
url = "https://pib.gov.in/FactsheetDetails.aspx?Id=149065"
driver.get(url)

# Close the browser
driver.quit()
