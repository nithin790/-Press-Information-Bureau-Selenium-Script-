from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import PyPDF2
from io import BytesIO

# Set up the browser
driver = webdriver.Chrome()

# Navigate to the webpage with the PDF link
driver.get("https://pib.gov.in/FactsheetDetails.aspx?Id=149065")

# Use explicit wait for the link to the PDF using link text
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
try:
    pdf_link = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Download PDF"))
    )
    pdf_url = pdf_link.get_attribute("href")

    # Download the PDF file
    response = requests.get(pdf_url)
    pdf_content = BytesIO(response.content)

    # Open the PDF file and extract text
    pdf_reader = PyPDF2.PdfFileReader(pdf_content)
    pdf_text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_text += page.extractText()

    # Print or process the extracted text
    print(pdf_text)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
