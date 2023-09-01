import webbrowser
import requests
from bs4 import BeautifulSoup
from repool_util import loadPubs


def lookup(titles):
    for title in titles:
        search_url = f"https://www.google.com/search?q={title}"
        try:
            response = requests.get(search_url)
            response.raise_for_status()

            # Parse the search results page using BeautifulSoup.
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the first search result link and open it in the default web browser.
            search_results = soup.find_all("a")
            for result in search_results:
                if result.get("href").startswith("/url?q="):
                    first_result_url = result.get("href")[7:].split('&')[0]  # Extract the URL.
                    webbrowser.open(first_result_url, new=2)
                    break  # Stop after opening the first result.
            else:
                print(f"No search results found for '{title}'")
        except Exception as e:
            print(f"Error opening the browser: {str(e)}")


options = ['venue', 'title', 'authors']
search_in = input("Choose what to search for " + str(options) + ": ").strip().lower()

if search_in not in options:
    print(f"Invalid option. Please choose from {', '.join(options)}")
else:
    word = input("Enter the word to search for: ").strip()

    if word:
        pubs = loadPubs('pubs_nips')
        google_it = 'title'
        p = [x[google_it] for x in pubs if word.lower() in x.get(search_in, '').lower()]

        if p:
            print(f"Number of results found: {len(p)}")
            lookup(p)
        else:
            print('No results found for your search.')
    else:
        print('Please enter a word to search for.')
