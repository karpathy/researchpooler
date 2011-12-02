"""
Some examples of fun things that can be done using the current 'API'
"""

from repool_util import loadPubs, stringToWordDictionary, openPDFs
from repool_analysis import publicationSimilarityNaive
from pdf_read import convertPDF

def demo3():
    """
    You found a cool paper online and you want to find similar papers:
    1. Download and parse the pdf
    2. Compare to text of all publications in pubs_ database
    3. Open the top 3 matches in browser (but note that current matching alg is
                                          very basic and could be much improved)
    
    Pre-requisites:
    - Assumes 'pubs_nips' exists and contains pdf text inside 
      (under key 'pdf_text'). This can be obtained by running 
      nips_download_parse.py and then nips_add_pdftext.py 
      or by downloading it from site.
      (https://sites.google.com/site/researchpooler/home)
    
    Side-effects:
    - will use os call to open a pdf with default program
    """
    
    # fetch this pdf from website, parse it, and make a publication dict from it
    # here is a random pdf from Andrew's website
    url = 'http://ai.stanford.edu/~ang/papers/icml11-DeepEnergyModels.pdf'
    print "downloading %s..." % (url,)
    text = convertPDF(url) #extract the text
    bow = stringToWordDictionary(text) #extract the bag of words representation
    p = {'pdf_text' : bow} #create a dummy publication dict
    
    # calculate similarities to our publications
    print "loading database..."
    pubs = loadPubs('pubs_nips')
    print "computing similarities. (may take while with current implementation)"
    scores = publicationSimilarityNaive(pubs, p)
    
    # find highest scoring pubs
    lst = [(s, i) for i,s in enumerate(scores) if s>=0]
    lst.sort(reverse = True)
    
    # display top 50 matches
    m = min(50, len(lst))
    for s, i in lst[:m]:
        print "%.2f is similarity to %s." % (s, pubs[i]['title'])
    
    #open the top 3 in browser
    print "opening the top 3..."
    openPDFs([pubs[i]['pdf'] for s,i in lst[:3]])
    
if __name__ == '__main__':
    demo3()
