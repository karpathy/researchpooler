"""
Standalone helper script.

Load nips pubs_ file, and adds to every paper its word counts under key 
'pdf_text'. The PDF for each paper is downloaded from NIPS site.
"""

from repool_util import loadPubs, savePubs, stringToWordDictionary
from pdf_read import convertPDF

pubs_all = loadPubs('pubs_nips')
print 'loaded pubs with %d entries.' % (len(pubs_all),)

#possibly place restrictions on pubs to process here
pubs = pubs_all

for i,p in enumerate(pubs):
    
    #if the pdf url does not exist, in future this could possibly use google
    #search to try to look up a link for the pdf first.
    if p.has_key('pdf') and not p.has_key('pdf_text'):
        
        # try to open the PDF from downloaded location
        processed = False
        try:
            floc = p['pdf'].index('NIPS')
            fname = p['pdf'][floc:]
            txt = convertPDF('downloads/'+fname)
            processed = True
            print 'found %s in file!' % (p['title'],)
        except:
            pass
            
        if not processed:
            # download the PDF and convert to text
            try:
                print 'downloading pdf for [%s] and parsing...' % (p.get('title', 'an un-titled paper'))
                txt = convertPDF(p['pdf'])
                processed = True
                print 'processed from url!'
            except:
                print 'error: unable to open download the pdf from %s' % (p['pdf'],)
                print 'skipping...'
        
        if processed:
            # convert to bag of words and store
            try:
                p['pdf_text'] = stringToWordDictionary(txt)
            except:
                print 'was unable to convert text to bag of words. Skipped.'
                
        
    print '%d/%d = %.2f%% done.' % (i+1, len(pubs), 100*(i+1.0)/len(pubs))
    
savePubs('pubs_nips', pubs_all)