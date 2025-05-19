from bs4 import BeautifulSoup
import requests
from transformers import pipeline
import torch
import GithubScraper  # import other scraper


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
    """Summarize a long text by splitting it into chunks and then combining the summaries."""
    text_chunks = split_text(text, max_chunk_length=500)
    summaries = [
        summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        for chunk in text_chunks
    ]
    final_summary = " ".join(summaries)
    return final_summary

# Function to get the main content of an article from its URL
def get_article_content(url):
    """Retrieve and return the main content of an article from the given URL."""
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
    """Scrape TechCrunch articles, summarize them, and write to an HTML file with a split-screen layout."""
    news_url = "https://techcrunch.com/latest/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(news_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('a', class_='loop-card__title-link')

        # Write articles and job data to an HTML file with split-screen layout
        with open('techcrunch_news.html', 'w', encoding='utf-8') as file:
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<style>\n")
            file.write(".container { display: flex; }\n")
            file.write(".articles-section { width: 50%; padding: 20px; overflow-y: auto; border-right: 1px solid #ccc; }\n")
            file.write(".jobs-section { width: 50%; padding: 20px; overflow-y: auto; }\n")
            file.write("body { font-family: Arial, sans-serif; margin: 0; padding: 0; }\n")
            file.write("h1 { text-align: center; }\n")
            file.write("ul { list-style-type: none; padding: 0; }\n")
            file.write("li { margin-bottom: 20px; }\n")
            file.write("</style>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<h1>Welcome, Tech Buddy</h1>\n")
            file.write("<div class='container'>\n")

          
            file.write("<div class='articles-section'>\n")
            file.write("<h2>TechCrunch 10 Most Recent Articles and Summaries</h2>\n")
            file.write("<ul>\n")

            for article in articles[:10]: 
                title = article.text.strip()
                url = article['href']

              
                article_text = get_article_content(url)
                summary = summarize_long_text(article_text) if article_text else "Summary not available."

              
                file.write(f"<li><a href='{url}' target='_blank'>{title}</a><br>\n")
                file.write(f"<p><strong>Summary:</strong> {summary}</p></li><br><br>\n")

            file.write("</ul>\n")
            file.write("</div>\n")

            # Jobs Section
            file.write("<div class='jobs-section'>\n")
            file.write("<h2>Recent Job Postings</h2>\n")

            # Insert job postings from GithubScraper
            job_list = GithubScraper.get_job_info()
            for job in job_list[:20]:
                file.write(f"<p>Company: {job['Company']}<br>")
                file.write(f"Title: {job['Title']}<br>")
                file.write(f"Location: {job['Location']}<br>")
                file.write(f"Link: <a href='{job['Link']}' target='_blank'>Apply</a></p><br>")

            file.write("</div>\n")
            file.write("</div>\n")  
            file.write("</body>\n")
            file.write("</html>\n")

        print("Successfully wrote 10 articles and summaries to techcrunch_news.html.")
    else:
        print("Failed to fetch the webpage:", response.status_code)


# Run the function
scrape_and_summarize_techcrunch_articles()
