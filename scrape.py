from selenium import webdriver
from bs4 import BeautifulSoup
import json

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


print("soup ends")

# Find the article content section
article_content = soup.find("div", class_="article-body")


if article_content is not None:
    # Find h1 entries within the article content
    h1_entries = article_content.find_all("h1")
    # for entry in h1_entries:
    #     print("entry content")
    #     # print(entry.text.strip())

    # Find paragraphs within the article content
    paragraphs = article_content.find_all("p")
    dataset = []

    for entry in paragraphs:
        dataset.append(entry.text.strip())
        # print("paragraph content")
        # print(entry.text.strip())
    # print(dataset)
    # more_content = soup.find("div", class_="accordion-body")
# accordion = more_content.find_all("ul")
# data = []
# for acc in accordion:
#     data.append(acc.text.strip())
# for d in data:
#     print(d)
    clean_data = []
    # for i in range(1, len(dataset)):
    #     if i == len(dataset) - 1:
    #         clean_data.append(dataset[len(dataset) - 1])

    #     elif dataset[i] != '' and dataset[i-1] == '' and dataset[i+1] == '':
    #         clean_data.append(dataset[i])
    for i in range(len(dataset)):
        if dataset[i] != '':
            clean_data.append(dataset[i])

    print(clean_data)
    print(len(clean_data), "is the size of clean data")
    print(len(h1_entries), "is the number of h1 entries")

    with open("corpus.txt", "w") as file:
        for i in range(len(dataset)):
            if dataset[i] != '':
                file.write(dataset[i])
                file.write('\n')

    # for entry in h1_entries:
    #     dataset.append(entry.text.strip())

    # for paragraph in paragraphs:
    #     dataset.append(paragraph.text.strip())

else:
    print("Article content not found.")


