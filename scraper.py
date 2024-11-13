from bs4 import BeautifulSoup
import requests
import csv

# Define the TechCrunch URL
news_url = "https://techcrunch.com/latest/"

# Send a GET request with headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(news_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article links using the `loop-card__title-link` class
    articles = soup.find_all('a', class_='loop-card__title-link')

    # Open the CSV file to write data
    with open('techcrunch_news.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'URL'])

        # Loop through articles to get details, but limit to 10
        for article in articles[:10]:  # Limit to the first 10 articles
            # Extract title and URL
            title = article.text.strip()
            url = article['href']

            # Write data to the CSV file
            csv_writer.writerow([title, url])

        print("Successfully wrote 10 articles to CSV.")
else:
    print("Failed to fetch the webpage:", response.status_code)
