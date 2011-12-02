"""
Functions for searching Google and retrieving urls to PDFs
"""

import urllib
import simplejson

def getPDFURL(pdf_title):
    """
    Search google for exact match of the title of this paper 
    and return the url to the pdf file, or 'notfound' if no exact match was 
    found.
    
    pdf_title: string, name of the paper.
    Returns url to the PDF, or 'notfound' if unsuccessful
    """
    
    # get results in JSON
    query = urllib.urlencode({'q' : pdf_title + ' filetype:pdf'})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' \
          % (query)
    search_results = urllib.urlopen(url)
    json = simplejson.loads(search_results.read())
    results = json['responseData']['results']
    
    # sift through them in search of an exact match
    for r in results:
        if r['title'] == '<b>' + pdf_title + '</b>':
            return r['url']
    
    return 'notfound'
      
