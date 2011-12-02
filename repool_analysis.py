""" 
Functions: some stage 3 functions. Analyze pubs_ files and 
provide more high-level functionality
"""

def publicationSimilarityNaive(train_pubs, test_pub):
    """ 
    Find similarities of publications to some particular publication,
    using a very simple overlap method.
    
    train_pubs: list of publications
    test_pub: a publication to compare to. Must contain 'pdf_text' key with the 
              bag of words that occur in that publication
    
    returns list of (scores, one for each of the train_pubs. Returns -1 for
            any score where a publication does not have the pdf_text available.
    """
    
    if not test_pub.has_key('pdf_text'): 
        return []
    
    scores = [-1 for i in range(len(train_pubs))]
    wnum_test = len(test_pub['pdf_text'])
    words = test_pub['pdf_text'].keys()
    
    for i,p in enumerate(train_pubs):
        if(i%100==0): print "%d/%d..." % (i, len(train_pubs))
        
        if not p.has_key('pdf_text'): continue
        
        #find score of the match
        wnum_train = len(p['pdf_text'])
        
        #a random thing I just thought of 5 seconds ago
        overlap = sum([1 for x in words if x in p['pdf_text'].keys()])
        scores[i] = 2.0 * overlap / (wnum_train + wnum_test)
        
    return scores
    
