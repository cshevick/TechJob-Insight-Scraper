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

      
        rows = soup.find_all('tr')  

        job_list = []

        
        for row in rows[1:]:  
            columns = row.find_all('td')  

          
            if len(columns) >= 4:
                job_name = columns[0].text.strip()     
                job_title = columns[1].text.strip()   
                location = columns[2].text.strip()    

             
                if job_name and job_title and location and "↳" not in job_name:
                  
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
