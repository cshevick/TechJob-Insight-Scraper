from bs4 import BeautifulSoup
import requests

# Function to scrape job information from GitHub repository page
def get_job_info():
    """Scrape job information from a GitHub repository page and return a list of job details."""
    git_url = "https://github.com/SimplifyJobs/Summer2025-Internships"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(git_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Select all rows in the table
        rows = soup.find_all('tr')  # Table rows

        job_list = []

        # Loop through each row and extract job details
        for row in rows[1:]:  # Skip header row
            columns = row.find_all('td')  # Find all cells in the row

            # Ensure this row has the expected number of columns and contains valid job data
            if len(columns) >= 4:
                job_name = columns[0].text.strip()      # Company name
                job_title = columns[1].text.strip()     # Job title
                location = columns[2].text.strip()      # Location

                # Check if the row likely represents a real job entry
                if job_name and job_title and location and "↳" not in job_name:
                    # Attempt to find the application link, if it exists
                    apply_link_tag = columns[3].find('a')
                    apply_link = apply_link_tag['href'] if apply_link_tag else "No link available"

                    job_info = {
                        'Company': job_name,
                        'Title': job_title,
                        'Location': location,
                        'Link': apply_link
                    }

                    job_list.append(job_info)
        return job_list
    else:
        print("Failed to fetch job listings:", response.status_code)
        return []
