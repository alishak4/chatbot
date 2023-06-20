import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = 'https://support.monday.com/hc/en-us/articles/360021702939-monday-workdocs'
response = requests.get(url)
page_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Find the question and answer elements
questions = soup.find_all('h2', class_='article-section-title')
answers = soup.find_all('div', class_='article-section-content')

# Extract the questions and answers from the elements
qa_pairs = []
for question, answer in zip(questions, answers):
    qa_pairs.append((question.text.strip(), answer.text.strip()))

print(qa_pairs)
# Main interaction loop
print("Bot: Hello, How can I assist you with Monday Workdocs?")
while True:
    user_input = input("You: ")
    found_answer = False
    for question, answer in qa_pairs:
        if user_input.lower() in question.lower():
            print("Bot:", answer)
            found_answer = True
            break
    if not found_answer:
        print("Bot: I'm sorry, I couldn't find an answer to your question.")
