"""
Standalone helper script.

Parses NIPS proceedings for years 2003-2010, creates list of dictionaries
that store information about each publication, and saves the result as a 
pickle in current directory called pubs_nips.
"""

import urllib
from BeautifulSoup import BeautifulSoup, Tag, NavigableString
from repool_util import savePubs

pubs = []
warnings = []
for num in range(16, 24):
    year = 1987 + num
    
    url = "http://books.nips.cc/nips%d.html" % (num,)
    print "downloading proceedings from NIPS year %d..." % (year,)
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    
    print "done. Parsing..."
    soup = BeautifulSoup(s)
    soup = soup.find('table', {'width' : '600'}) # find the main table HTML
    soup = soup.contents[0].contents[0] # descend down <tr> and then <td>
    
    # iterate over this giant linear dump they have on the proceedings site
    venue = 'NIPS %d' % (year,)
    new_pub = {}
    old_count = len(pubs)
    for item in soup.contents:
    
        if isinstance(item, Tag):
            if item.name == 'b':
                
                # we stumbled by a new publication entry. If we were processing
                # one before this, then commit that one first then continue
                if new_pub:
                    if not new_pub.has_key('authors'):
                        warnings.append("oh oh no authors for publication... ")
                    
                    if not new_pub.has_key('title'):
                        warnings.append("oh oh no title for publication... ")
                    
                    new_pub['venue'] = venue
                    new_pub['year']= year
                    pubs.append(new_pub)
                
                # start new publication dictionary
                new_pub = {}
                new_title = str(item.contents[0]) # descend down a <b> tag
                new_title = new_title.replace('\n', '')
                new_pub['title'] = new_title
                
            if item.name == 'a':
                modifier = str(item.contents[0]).strip()
                if modifier == '[pdf]':
                    new_pub['pdf'] = str(item.attrs[0][1])
                elif modifier == '[bibtex]':
                    new_pub['bibtex'] = str(item.attrs[0][1])
                elif modifier == '[correction]':
                    new_pub['correction'] = str(item.attrs[0][1])
                elif modifier == '[supplemental]':
                    new_pub['supplemental'] = str(item.attrs[0][1])
                elif modifier == '[slide]':
                    new_pub['slide'] = str(item.attrs[0][1])
                elif modifier == '[audio]':
                    new_pub['audio'] = str(item.attrs[0][1])
                elif modifier == '[ps.gz]':
                    pass # ignore
                elif modifier == '[djvu]':
                    pass # ignore
                else:
                    warnings.append("warning: modifier %s skipped" %(modifier,))
                
        if isinstance(item, NavigableString):
            if len(str(item))>3:
                
                # this is probably the line describing authors
                author_str = str(item)
                author_str = author_str.replace('\n', '') # remove newlines
                author_list = author_str.split(',')
                if new_pub.has_key('authors'):
                    warnings.append("we're in trouble... %s, but already have "\
                                    "%s" % (str(item), new_pub['authors']))
                    
                new_pub['authors'] = [x.strip() for x in author_list]
        
    # I hate myself a little for this
    # TODO LATER_MAYBE: CODE CHUNK DUPLICATION
    if not new_pub.has_key('authors'):
        warnings.append("oh oh no authors for publication... ")
    if not new_pub.has_key('title'):
        warnings.append("oh oh no title for publication... ")
    new_pub['venue'] = venue
    new_pub['year']= year
    pubs.append(new_pub)
    
    print "read in %d publications for year %d." % (len(pubs) - old_count, year)
    

# show warnings, if any were generated
if len(warnings)>0:
    print "%d warnings:" % (len(warnings),)
    for x in warnings:
        print x
else:
    print "No warnings generated."

# finally, save pickle as output
print "read in a total of %d publications." % (len(pubs),)
fname = "pubs_nips"
print "saving pickle in %s" % (fname,)
savePubs(fname, pubs)
print "all done."
