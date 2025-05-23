# Job Portal Scraper

This project is a web scraper designed to extract job listing data from the "Job Portal System" section of [shaxzodbek.com](https://shaxzodbek.com/) and store it in a database for further use. When executed, the script sends HTTP requests to the site, parses relevant pages, and extracts useful information from each job post.

## Key Features

- Automatically scrapes job listings from a job portal website
- Extracts key data such as:
  - Job title
  - Company name
  - Location
  - Salary (if available)
  - Posting date
- Saves the data into a SQLite or other supported database
- Avoids duplication by checking for existing entries

## Requirements

Before running the project, make sure the following Python libraries are installed:

