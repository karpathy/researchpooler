"""
Some examples of fun things that can be done using the current 'API'
"""

from repool_util import loadPubs, openPDFs

def demo1():
    """
    You wrote an algorithm and benchmarked it on the MNIST dataset. You are 
    wondering how your results compare with those in the literature:
    1. Finds all publications that mention mnist
    2. Print out their titles
    3. Open the three latest publications that mention it at least twice
    
    Pre-requisites:
    - Assumes 'pubs_nips' exists and that pdf text is present. 
      This can be obtained by running 
      nips_download_parse.py and then nips_add_pdftext.py, or by downloading it 
      from site (https://sites.google.com/site/researchpooler/home)
    
    Side-effects:
    - will use os call to open a pdf with default program
    """
    
    print "loading the NIPS publications dataset..."
    pubs = loadPubs('pubs_nips')
    
    # get all papers that mention mnist
    p = [x for x in pubs if 'mnist' in x.get('pdf_text',{})]
    print "titles of papers that mention MNIST dataset:"
    for x in p:
        print x['title']
    print "total of %d publications mention MNIST." %(len(p),)
    
    # sort by number of occurences
    occ = [(x['year'], x['pdf']) for i,x in enumerate(p) if x['pdf_text']['mnist']>1]
    occ.sort(reverse = True)
    
    # open the top 3 latest in browser
    print "opening the top 3..."
    openPDFs([x for year,x in occ[:3]])

if __name__ == '__main__':
    demo1()
