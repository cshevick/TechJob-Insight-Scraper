from bs4 import BeautifulSoup
import requests
from transformers import pipeline
import torch

# Set up the summarizer
device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

# Function to split text into chunks if it's too long for the summarizer
def split_text(text, max_chunk_length=500):
    """Split text into chunks of a specified maximum length."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_chunk_length):
        chunk = ' '.join(words[i:i + max_chunk_length])
        chunks.append(chunk)

    return chunks

# Function to summarize a long text
def summarize_long_text(text):
    """Summarize a long text by splitting it into chunks."""
    text_chunks = split_text(text, max_chunk_length=500)
    summaries = [summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for chunk in text_chunks]
    final_summary = " ".join(summaries)
    return final_summary

# Function to get the main content of an article from its URL
def get_article_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p', class_='wp-block-paragraph')
        article_text = [p.get_text().strip() for p in paragraphs if p.get_text().strip()]
        return " ".join(article_text)
    else:
        print("Failed to retrieve the article")
        return None

# Function to scrape articles and save summaries in an HTML file
def scrape_and_summarize_techcrunch_articles():
    news_url = "https://techcrunch.com/latest/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(news_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('a', class_='loop-card__title-link')

        with open('techcrunch_news.html', 'w', encoding='utf-8') as file:
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")
            file.write("<body>\n")
            file.write("<h1>Welcome, Tech Buddy</h1>\n")
            file.write("<p>TechCrunch 10 most recent articles and summaries:</p>\n")
            file.write("<ul>\n")

            for article in articles[:10]:  # Limit to the first 10 articles
                title = article.text.strip()
                url = article['href']

                # Get the article content and summarize it
                article_text = get_article_content(url)
                summary = summarize_long_text(article_text) if article_text else "Summary not available."

                # Write the article title, URL, and summary to the HTML file
                file.write(f"<li><a href='{url}' target='_blank'>{title}</a><br>\n")
                file.write(f"<p><strong>Summary:</strong> {summary}</p></li><br><br>\n")

            file.write("</ul>\n")
            file.write("</body>\n")
            file.write("</html>\n")

        print("Successfully wrote 10 articles and summaries to techcrunch_news.html.")
    else:
        print("Failed to fetch the webpage:", response.status_code)


# Run the function
scrape_and_summarize_techcrunch_articles()
