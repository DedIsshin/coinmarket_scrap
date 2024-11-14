import sys
sys.path.insert(0, '/Users/Dias/scrap_new_coinmarket/coinmarket_scrap/src')

from main import DiasScrape

scrape = DiasScrape()

# Get the news
scrape.get_news()