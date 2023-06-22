from selenium import webdriver
from bs4 import BeautifulSoup
import csv

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
    # Find the first <h1> tag

    with open("corpus.csv", "w", newline='') as file:
        writer = csv.writer(file)

        #Write column headers
        writer.writerow(['Question', 'Response'])
        h1_tag = article_content.find_all('h1')

        for tag in h1_tag:
            print('new section')

            question = []
            question.append(tag.text.strip())
            print(tag.text.strip())

            p_tag = tag.find_next_sibling('p')
            paragraph = []
            paragraph.append(p_tag.get_text())

            print(p_tag.get_text())

            
            div_header_tag = p_tag.find_next('div', class_='accordion-header')
            if div_header_tag is not None:
                question.append(div_header_tag.get_text())
                print(div_header_tag.get_text())

            # header_text = div_header_tag.get_text()
                div_body_tag = div_header_tag.find_next("div", class_="accordion-body")
                paragraph.append(div_body_tag.get_text())
                print(div_body_tag.get_text())
            
            writer.writerow([question, paragraph])
        # with open("corpus.txt", "w") as file:
        #     for i in range(len(dataset)):
        #         if dataset[i] != '':
        #             file.write(dataset[i])
        #             file.write('\n')

        # for entry in h1_entries:
        #     dataset.append(entry.text.strip())

        # for paragraph in paragraphs:
        #     dataset.append(paragraph.text.strip())

else:
    print("Article content not found.")


