
# eBay Web Scraping Application

## Overview

This is a web scraping application built using Flask, BeautifulSoup, and pandas. The application scrapes eBay for product listings based on user queries, stores the data in an Excel file, and displays the results in a web interface. Additionally, it provides a visual analysis of the scraped product prices.

## Features

- **Web Scraping**: Scrapes eBay for product listings based on user queries.
- **Data Storage**: Stores scraped data in an Excel file (`ebay_products.xlsx`).
- **Web Interface**: Displays the scraped data in a web interface using Flask.
- **Data Visualization**: Provides a histogram to visualize the distribution of product prices.

## Installation

### Prerequisites

- Python 3.6+
- `pip` (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/your-username/ebay-web-scraping-app.git
cd ebay-web-scraping-app
```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install Flask requests beautifulsoup4 pandas openpyxl matplotlib seaborn
```

### Create Necessary Directories

Ensure that the `templates` directory exists and contains the `index.html` and `results.html` files.

## Usage

### Run the Application

```bash
python app.py
```

### Access the Application

Open your web browser and go to `http://127.0.0.1:5000/`.

### Search for Products

1. Enter your search query on the home page.
2. Click the search button.
3. View the results on the results page.

### Data Visualization

After scraping the data, a histogram of the product prices is displayed using Matplotlib and Seaborn.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── scrape_ebay.py         # eBay scraping script
├── ebay_products.xlsx     # Excel file to store scraped data
├── templates
│   ├── index.html         # Home page template
│   └── results.html       # Results page template
└── README.md              # This README file
```

## Screenshots

### Home Page

![Home Page](screenshots/home_page.png)

### Results Page

![Results Page](screenshots/results_page.png)

### Price Distribution

![Price Distribution](screenshots/price_distribution.png)

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with detailed descriptions of changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This application uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library for web scraping.
- The [pandas](https://pandas.pydata.org/) library is used for data manipulation and storage.
- Data visualization is done using [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/).

---
