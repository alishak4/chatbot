from selenium import webdriver
from bs4 import BeautifulSoup

# Configure Selenium webdriver
driver = webdriver.Chrome()  # You may need to download and specify the path to the Chrome webdriver
url = "https://support.monday.com/hc/en-us/articles/360021702939-monday-workdocs"

# Load the webpage
driver.get(url)

# Extract the page source after content has loaded
page_source = driver.page_source

# Close the Selenium webdriver
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find the article content section
article_content = soup.find("div", class_="article-body")

if article_content is not None:
    # Find h1 entries within the article content
    h1_entries = article_content.find_all("h1")

    # Find paragraphs within the article content
    paragraphs = article_content.find_all("p")

    accordion_body = article_content.find_all("accordion-body")

    dataset = []

    for entry in h1_entries:
        dataset.append(entry.text.strip())

    for paragraph in paragraphs:
        dataset.append(paragraph.text.strip())

    for accordion in accordion_body:
        dataset.append(accordion.text.strip())

    # Print the dataset
    for data in dataset:
        print(data)
else:
    print("Article content not found.")
