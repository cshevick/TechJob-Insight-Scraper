# TechJob Insight Scraper

A web scraping application that scrapes recent articles from TechCrunch and the latest tech internship postings from a GitHub repository using BeautifulSoup and Requests. It then summarizes the articles using a pre-trained NLP model (BART). The application then creates an HTML file with a split-screen layout that displays the recent articles and a summary for each, along with the 20 most recent internship postings with the position name, location, and link to apply for each. This application allows the user to stay up to date with tech news as well as internship postings. 

## Installation
   1. Clone the repository in IDE of choice using: https://github.com/cshevick/TechJob-Insight-Scraper.git
   2. Install the required dependencies: pip install beautifulsoup4 requests transformers torch pandas

## Usage

Once you have cloned the repository in your IDE, run the 'ArticleScraper.py' python script. Upon successful completion, the program produces an HTML file that you can preview either in the built-in IDE HTML previewer, if available, or you can run in any HTML previewer in your browser, which will display the ten most recent TechCrunch articles and twenty most recent tech internships and info for each one.

## License
This project is open source and licensed under the MIT License. Feel free to modify and use the code as per your needs.

