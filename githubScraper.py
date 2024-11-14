from bs4 import BeautifulSoup
import requests


def get_job_info():
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
                job_name = columns[0].text.strip()
                job_title = columns[1].text.strip()
                location = columns[2].text.strip()

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

        # Print the job information
        for job in job_list[:20]:  # Limit to the first 20 jobs
            print(f"Company: {job['Company']}")
            print(f"Title: {job['Title']}")
            print(f"Location: {job['Location']}")
            print(f"Link: {job['Link']}")
            print("-" * 40)

        print("Successfully retrieved 20 jobs.")
    else:
        print("Failed to fetch the webpage:", response.status_code)


get_job_info()
