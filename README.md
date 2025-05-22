# RERA Odisha Project Scraper

This project is a web scraper that extracts information about real estate projects registered with RERA (Real Estate Regulatory Authority) in Odisha, India. The scraper collects details of the first 6 projects listed on the RERA Odisha website.

## Project Details

The scraper collects the following information for each project:
- RERA Registration Number
- Project Name
- Promoter Name
- Promoter Address
- GST Number

## Dependencies

The project requires the following Python packages:
- `requests`: For making HTTP requests to the website
- `beautifulsoup4`: For parsing HTML and extracting data
- `selenium`: For dynamic web scraping
- `webdriver-manager`: For managing Chrome WebDriver

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt