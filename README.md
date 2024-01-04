# Web Scraping Swiggy Restaurants in Bangalore

## Overview
This Python script uses the `requests` and `BeautifulSoup` libraries to perform web scraping on Swiggy's website to extract a list of best restaurants in Bangalore. The extracted data, which includes restaurant names, is then saved to a CSV file.

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- `BeautifulSoup` library (`pip install beautifulsoup4`)

## Usage
1. Install the required libraries:
    pip install requests beautifulsoup4

2. Run the Python script:
    python scrapper.py

## Script Details
- The script sends an HTTP GET request to Swiggy's website, simulating a request from a web browser.
- It handles HTTP errors using `requests.exceptions.HTTPError` and other exceptions.
- Upon successful response (status code 200), it extracts restaurant names from the HTML using BeautifulSoup.
- The extracted data is written to a CSV file named `Bangalore_2.csv` in the `csv` directory.

## Notes
- Ensure that your Python environment has the required libraries installed.
- Respect the terms of service of the website you are scraping.
- Customize the script as needed based on the HTML structure of the website.
