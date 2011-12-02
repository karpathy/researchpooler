""" Functions: useful general utils """

import cPickle
import re
from os import startfile

def savePubs(filename, pubs_to_save):
    """ 
    save a list of publications into a file using Python's pickle
    filename: string
    pubs_to_save: List of Publication objects
    
    returns nothing
    """
    
    file = open(filename, 'w')
    cPickle.dump(pubs_to_save, file)
    file.close()

def loadPubs(filename):
    """
    retrieve a saved list of publications
    filename: string
    returns list of dictionaries, each representing a Publication
    """
    
    unpicklefile = open(filename, 'r')
    pubs = cPickle.load(unpicklefile)
    unpicklefile.close()
    return pubs
    
def openPDFs(pdf_lst):
    """
    uses an os call to open a list of pdfs
    pdf_lst: list of strings: paths (or urls) of pdfs to open
    """
    if len(pdf_lst)>10:
        print "more than 10? that can't be right. Request denied."
        return
        
    for x in pdf_lst:
        startfile(x)
        
def stringToWordDictionary(str):
    """
    Takes a string and returns dictionary that stores frequency of every word.
    Some stop words are removed.
    
    str: string
    returns dictionary of word counts for each word. Example: d['hello'] -> 5
    """
    str = str.lower() #convert to lower case
    m = re.findall('[a-zA-Z\-]+', str)
    m = [x for x in m if len(x) > 2] #filter out small words
    
    # count number of occurences of each word in dict and return it
    d = {}
    for i in m: d[i] = d.get(i,0) + 1
    
    # remove stopwords
    stopwords = ['the', 'and', 'for', 'that', 'can', 'this', 'which', \
                 'where', 'are', 'from', 'our', 'not', 'with', 'use', \
                 'then', 'than', 'but', 'have', 'was', 'were', 'these', \
                 'each', 'used', 'set', 'such', 'using', 'when', 'those' \
                 'may', 'also']
    
    #cid is some kind of artifact from the pdf conversion that occurs very often
    stopwords.extend(['cid'])
    
    keys = d.keys()
    for k in keys:
        if k in stopwords: 
            del d[k]
    
    return d
