from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_hot100() -> pd.DataFrame:
    '''
    This function scrapes the top 100 songs from billboard.com and return a 
    DataFrame including the song title and artist

    Output:
    Pandas DataFrame
    '''

    # Define the base url
    url = "https://www.billboard.com/charts/hot-100"
    
    # Request the url data
    response = requests.get(url)

    # Create soup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Define select string
    title_select = 'div.chart-results-list .c-title.a-truncate-ellipsis'
    
    # Parse song titles
    titles = [li.get_text().strip() for li in soup.select(title_select)]
    
    # Define artist select
    artist_select = 'div.chart-results-list .c-label.a-no-trucate'
    
    # Parse song arists
    artists = [li.get_text().strip() for li in soup.select(artist_select)]

    songs = pd.DataFrame({"title": titles, "artist": artists})

    return songs

