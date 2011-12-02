"""
Functions for PDF parsing tools and utils
"""

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO

import urllib

def convertPDF(pdf_path, codec='ascii'):
    """
    Takes path to a PDF and returns the text inside it as string
    
    pdf_path: string indicating path to a .pdf file. Can also be a URL starting 
              with 'http'
    codec: can be 'ascii', 'utf-8', ...
    returns string of the pdf, as it comes out raw from PDFMiner
    """
    
    if pdf_path[:4] == 'http':
        print 'first downloading %s ...' % (pdf_path,)
        urllib.urlretrieve(pdf_path, 'temp.pdf')
        pdf_path = 'temp.pdf'
    
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    
    fp = file(pdf_path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    
    str = retstr.getvalue()
    retstr.close()
    
    return str
