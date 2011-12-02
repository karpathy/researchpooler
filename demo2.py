"""
Some examples of fun things that can be done using the current 'API'
"""

from repool_util import loadPubs, openPDFs

def demo2():
    """
    You unexpectedly became very interested in Deep Belief Networks. As a first
    stab at some background reading, you want to:
    1. Find all NIPS publications with Deep in title
    2. open them in the browser
    
    Pre-requisites:
    - Assumes 'pubs_nips' exists. This can be obtained by running 
      nips_download_parse.py or by downloading it from site. See README.txt
    
    Side-effects:
    - will use os call to open a pdf with default program
    """
    
    pubs = loadPubs('pubs_nips')
    
    # get urls that correspond to publications with deep in title
    p = [x['pdf'] for x in pubs if 'deep' in x['title'].lower()]
    
    if len(p)>10:
        p=p[:10]
        print 'oops too many (%d) results! Only opening random 10.' % (len(p),)
        
    openPDFs(p)
    
if __name__ == '__main__':
    demo2()
