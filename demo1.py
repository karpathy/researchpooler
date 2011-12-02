"""
Some examples of fun things that can be done using the current 'API'
"""

from repool_util import loadPubs, openPDFs, stringToWordDictionary
from pdf_read import convertPDF

def demo1():
    """
    You wrote an algorithm and benchmarked it on the MNIST dataset. You are 
    wondering how your results compare with those in the literature:
    1. Finds all publications that mention mnist
    2. Print out their titles
    3. Open the three latest publications that mention it at least twice
    
    Pre-requisites:
    - Assumes 'pubs_nips' exists. This can be obtained by running 
      nips_download_parse.py or by downloading it from site. See README.txt
    
    Side-effects:
    - will use os call to open a pdf with default program
    """
    
    pubs = loadPubs('pubs_nips')
    
    # get all papers that mention mnist
    p = [x['title'] for x in pubs if 'mnist' in x.get('pdf_text',{})]
    print 'titles of papers that mention MNIST dataset:'
    for x in p:
        print x['title']
    
    # sort by number of occurences
    occ = [(x['year'], i) for i,x in p if x['pdf_text']['mnist']>1]
    occ.sort(reverse = True)
    
    # open the top 3 latest in browser
    print "opening the top 3..."
    openPDFs([x['pdf'] for x in occ[:3]])

if __name__ == '__main__':
    demo1()
