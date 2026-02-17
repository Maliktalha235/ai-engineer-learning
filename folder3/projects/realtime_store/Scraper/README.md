# Scraper Module

Handles automated data extraction from e-commerce websites.

## Features
- Multi-category scraping
- Multi-page scraping  
- Pagination handling
- Rating extraction
- Price cleaning & formatting
- Structured dictionary output

## Key Functions

### `scrape_category(category)`
- There are 2 categories laptops and tablets
- Scrapes all pages of a given category
- Returns structured product data

### `scrape_all_categories()`
- Iterates through predefined categories
- Combines results into a single dataset
