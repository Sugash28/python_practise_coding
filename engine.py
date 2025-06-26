import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Your Google Custom Search API key and Custom Search Engine ID
api_key = 'AIzaSyBK8erWyl9NKo1L16PGcxE7rqmXxkI1jxQ'
cse_id = '13b81dae5d5cf44fe'

# Function to perform Google Custom Search
def google_search(query, api_key, cse_id):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check for HTTP errors
    return response.json()

# Function to extract text from a URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text from the page
        text = soup.get_text()

        # Remove excess whitespace
        clean_text = ' '.join(text.split())

        return clean_text
    except Exception as e:
        print(f"Error while extracting text from {url}: {e}")
        return None

# Main program loop to search and extract data
while True:
    query = input("Enter a search query: ")
    search_results = google_search(query, api_key, cse_id)

    # Extract URLs from search results
    urls = [item['link'] for item in search_results.get('items', [])]
    print("Found URLs:", urls)

    # List to store extracted text
    extracted_text_list = []

    # Extract and store text from each URL
    for url in urls:
        text = extract_text_from_url(url)
        if text:  # If text is not None, add it to the list
            extracted_text_list.append(text)

    # Print the entire list
    print("\nExtracted Text List:")
    for idx, text in enumerate(extracted_text_list, 1):
        print(f"\n--- Text from URL {idx} ---")
        print(text[:50])  # Print the first 500 characters of each text for brevity
    
    # Print the list structure to verify it contains all strings
    print("\nComplete List Structure:")
   # print(extracted_text_list)  # This prints the list as a Python list of strings
    

    break  # Exit after one search iteration (remove this if you want the loop to continue)
