import urllib.request
from bs4 import BeautifulSoup
from repool_util import savePubs

pubs = []
warnings = []

# Loop over years from 2006 to 2022
for year in range(2006, 2023):
    # Construct the URL for the specific year
    url = f"https://proceedings.neurips.cc/paper_files/paper/{year}"

    print(f"downloading proceedings from NIPS year {year}...")
    print(url)

    with urllib.request.urlopen(url) as f:
        s = f.read()

    print("done. Parsing...")
    soup = BeautifulSoup(s, 'html.parser')

    # Find the section containing publication information
    publication_section = soup.find('div', {'class': 'container-fluid'})

    # Iterate over each publication entry
    for publication_entry in publication_section.find_all('li', {'class': 'none'}):
        new_pub = {}

        # Extract title
        title_tag = publication_entry.find('a', {'title': 'paper title'})
        if title_tag:
            new_pub['title'] = title_tag.text.strip()

        # Extract authors
        authors_tag = publication_entry.find('i')
        if authors_tag:
            authors = authors_tag.text.strip().split(',')
            new_pub['authors'] = [author.strip() for author in authors]

        # Add publication to the list
        if new_pub:
            new_pub['venue'] = f'NeurIPS {year}'
            pubs.append(new_pub)

    print(f"Read in {len(pubs)} publications for year {year}.")

# show warnings, if any were generated
if len(warnings) > 0:
    print(f"{len(warnings)} warnings:")
    for x in warnings:
        print(x)
else:
    print("No warnings generated.")

# finally, save pickle as output
fname = "pubs_nips"
print("saving pickle in %s" % fname)
savePubs(fname, pubs)
print("all done.")
