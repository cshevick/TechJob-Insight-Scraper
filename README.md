# Tech Buddy

A web scraping application that fetches recent articles from TechCrunch and the latest job postings from a GitHub repository. This application summarizes articles using NLP and presents a split-screen HTML file with article summaries on one side and job listings on the other. This application is designed to help users stay updated on recent tech news and know when new internships are posted.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements) 
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Overview

The TechCrunch & GitHub Job Scraper is designed to provide users with recent TechCrunch articles along with relevant job postings. Each article is summarized using NLP models, and job postings display the company name, job title, location, and a direct "Apply" link. The final output is a split-screen HTML file displaying both articles and job listings for easy browsing.

- **TechCrunch Article Summarization**: Fetch and summarize the latest TechCrunch articles.
- **Job Listings from GitHub**: Retrieve recent job postings from a GitHub repository for internships.
- **HTML Output**: Generates a split-screen HTML layout displaying articles on one side and job listings on the other.

## Features

- **Web Scraping**: Uses BeautifulSoup and Requests to scrape data from TechCrunch and GitHub.
- **Text Summarization**: Leverages a pre-trained NLP model (BART) to summarize long-form articles.
- **HTML Generation**: Creates a dynamic HTML file with a split-screen layout for articles and jobs.

## Requirements

- **Python 3.7+**
- **BeautifulSoup4**: For HTML parsing
- **Requests**: For sending HTTP requests
- **Transformers (Hugging Face)**: For text summarization using the BART model
- **Torch**: Required by Transformers for the summarization model

## Usage
Running the Script
- Run ArticleScraper.py to scrape data, generate summaries, and create the HTML file.
- Upon successful execution, the HTML output (techcrunch_news.html) will display:
    - **Left Column**: Recent TechCrunch articles with summaries.
    - **Right Column**: Latest job postings from GitHub with "Apply" links.


## Project Structure
- ArticleScraper.py: Main script for scraping TechCrunch articles, summarizing content, and generating the HTML output.
- GithubScraper.py: A separate module to handle GitHub job scraping.
techcrunch_news.html: HTML output file displaying articles and jobs side-by-side.

## License
This project is open source and licensed under the MIT License.

