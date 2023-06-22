import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from selenium import webdriver
from bs4 import BeautifulSoup

# # Configure Selenium webdriver
# driver = webdriver.Chrome()  # You may need to download and specify the path to the Chrome webdriver
# url = "https://support.monday.com/hc/en-us/articles/360021702939-monday-workdocs"

# # Load the webpage
# driver.get(url)

# # Extract the page source after content has loaded
# page_source = driver.page_source

# # Close the Selenium webdriver
# driver.quit()

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(page_source, "html.parser")


# print("soup ends")

# # Find the article content section
# article_content = soup.find("div", class_="article-body")


# if article_content is not None:
#     # Find h1 entries within the article content
#     h1_entries = article_content.find_all("h1")
#     # for entry in h1_entries:
#     #     print("entry content")
#     #     # print(entry.text.strip())

#     # Find paragraphs within the article content
#     paragraphs = article_content.find_all("p")
#     dataset = []

#     for entry in paragraphs:
#         dataset.append(entry.text.strip())
#         # print("paragraph content")
#         # print(entry.text.strip())
#     # print(dataset)

#     clean_data = []
#     for i in range(1, len(dataset)):
#         if i == len(dataset) - 1:
#             clean_data.append(dataset[len(dataset) - 1])

#         elif dataset[i] != '' and dataset[i-1] == '' and dataset[i+1] == '':
#             clean_data.append(dataset[i])

with open("corpus.txt", "r") as file:
    corpus = file.read()

# corpus = []
# labels = []

# for i, data in enumerate(clean_data):
#     corpus.append(data)
#     labels.append(f'Response {i + 1}')

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
preprocessed_corpus = []

for sentence in corpus:
    tokens = word_tokenize(sentence.lower())
    words = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    preprocessed_sentence = ' '.join(words)
    preprocessed_corpus.append(preprocessed_sentence)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_corpus)

def generate_response(user_input):
    preprocessed_input = []
    tokens = word_tokenize(user_input.lower())
    for token in tokens:
        if token not in stop_words:
            lemmatized_token = lemmatizer.lemmatize(token)
            preprocessed_input.append(lemmatized_token)
    
    preprocessed_input = ' '.join(preprocessed_input)
    
    input_vector = vectorizer.transform([preprocessed_input])
    similarities = cosine_similarity(input_vector, X)
    most_similar_index = similarities.argmax()
    response = corpus[most_similar_index]
    
    return response

while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break
    
    response = generate_response(user_input)
    print("ChatBot:", response)
