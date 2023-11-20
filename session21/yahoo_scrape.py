import csv
import urllib.request
import string
from bs4 import BeautifulSoup

DOWNLOAD_URL = "https://finance.yahoo.com/trending-tickers"

def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)


def parse_html(html):
    """
    Analyze the html page, find the information and return the move list of tuples (Ticker, Price)
    """
    soup = BeautifulSoup(html, features="html.parser")

    stock_table = soup.find("table", attrs={"class": "W(100%)"})
    # print(stock_table)

    trending_tickers = []

    for item in stock_table:
        stock_item = item.find_all("tr", attrs={"class":"simpTblRow"})
        
        # get ticker
        for container in stock_item:
            ticker_link = container.find("a")
            ticker = ticker_link.string
            # return ticker
        
        # get name
        company = item.find_all("td", attrs={"class": "Va(m)"})
        print(company)
        

        


parse_html(download_page(DOWNLOAD_URL).read())