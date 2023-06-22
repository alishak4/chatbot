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
soup = BeautifulSoup(page_source, 'html.parser')


# Find the article content section
article_content = soup.find("div", class_="article-body")


if article_content is not None:

    # Find the question and answer elements
    questions = article_content.find_all('h1')
    answers =  article_content.find_all('p')
       
    for q in questions:
        print(q.text.strip())
    for a in answers:
        print(a.text.strip())
   # print(a.text.strip())
# Extract the questions and answers from the elements
# qa_pairs = []
# for question, answer in zip(questions, answers):
#     qa_pairs.append((question.text.strip(), answer.text.strip()))

# Print the extracted question and answer pairs
# for pair in qa_pairs:
#     print(f'Question: {pair[0]}')
#     print(f'Answer: {pair[1]}')
#     print('---')
