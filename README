REsearch POOLer (repool) 
Project site: https://sites.google.com/site/researchpooler/home

Authors: Andrej Karpathy <karpathy@cs.stanford.edu> || <andrej.karpathy@gmail.com>, http://cs.stanford.edu/~karpathy/

-------------------------------------------------------------------------------
MOTIVATION AND PLAN
-------------------------------------------------------------------------------
- Ever wish you could right away view all papers published based on a keyword in title or abstract?
- Or, ever wish you could look up the most similar paper (content wise) to some paper on some random url?
- How about searching for all papers that report a result on a particular dataset?
-> Literature review is much harder than it should be.

This set of tools is an initiative to fix this problem. Here's the master plan and types of scripts in this project:

STAGE 1 scripts: scripts for raw data gathering and parsing that output pickles in an intermediate dictionary-based representation. These will include mostly scripts that download files, parse HTML, etc.
STAGE 2 scripts: scripts that enrich the intermediate representations from STAGE 1 in various ways. For example, a script could iterate over publications in database, and if it finds that some entry is missing its pdf contents, it could attempt a google search to find the pdf, and add it if successful.
STAGE 3 scripts: tools and helper functions that can analyze the intermediate representations and produce higher level scripts that do more interesting things. For example, functionality such as 'find all documents that are similar to this one', or 'find object detection papers in psychology'. All kinds of fun Machine Learning can go here as well, like LDA etc.
STAGE 4 files: create nice web-based UI (maybe using Google App Engine?) to make the project accessible and easy to use. These will be modules that interact with STAGE 3 scripts on the backend.

-------------------------------------------------------------------------------
INSTALLATION
-------------------------------------------------------------------------------
1. Download pubs_nips from the site[*] (https://sites.google.com/site/researchpooler/downloads)
2. Browse around (project is young, no installation needed so far!)
3. Download/Install current Python dependencies:

BeautifulSoup   [for easy and robust HTML parsing]
PDFMiner        [for parsing PDFs and extracting text]
simplejson      [OPTIONAL. for parsing outputs of Google searches using their API]

4. Enjoy the demos

[*] Instead of downloading the database you can also regenerate the pubs_nips database yourself using the two scripts I wrote. Simply run:
$> python nips_download_parse.py
(takes a few seconds) and then
$> python nips_add_pdftext.py
(takes potentially an hour or two because it has to download and parse all papers published at NIPS since 2003)
-------------------------------------------------------------------------------
EXAMPLE USAGE
-------------------------------------------------------------------------------
Say you unexpectedly became very interested in Deep Belief Networks. It now takes 3 lines of python to open all NIPS papers that mention 'deep' in title inside your browser: (also see demo2)

>>> pubs = loadPubs('pubs_nips')
>>> p = [x['pdf'] for x in pubs if 'deep' in x['title'].lower()]
>>> openPDFs(p)

Or maybe you want to open all papers that mention MNIST dataset? (demo1 also shows how you can easily go on to open the 3 latest ones.)
>>> pubs = loadPubs('pubs_nips')
>>> p = [x['title'] for x in pubs if 'mnist' in x.get('pdf_text',{})]
>>> openPDFs(p)

Or how about opening papers that are most similar to some paper at some url? See demo3.

-------------------------------------------------------------------------------
ORGANIZATION, I/O AND DATA REPRESENTATIONS
-------------------------------------------------------------------------------

Here's the idea for the near future, I think: there will be several stage1 scripts, each of which is reponsible for parsing a particular venue of publications. For example, the stage1 script nips_download_parse.py parses and outputs all publications in NIPS from 2003 to 2011. (but does not analyze the text)

The idea is to have very similar scripts for other venues, such as ICML, or CVPR, etc... The output of each such script should be a pickled list of dictionaries. Each dictionary represents a publication. For example:
[{'title': 'Solving AI using Random Forests', 'authors': ['Jim Smith', 'Bill Smith', 'year': 2020, 'venue': 'NIPS 2020', 'pdf': 'http://google.com/ai'}, 
...]

this representation is a flexible start, as some conference pages provide more information than others, and we don't want to force any particular structure from the get go. In other words, the database could contain some papers that have the author, title, and abstract, but not the full text. Another entry might have the full text, but maybe it is missing author or title. Stage 2 scripts will be useful to go over these representations, and fill in details in whatever ways possible. (such as maybe hooking into other sites like Google Scholar, etc?) 

Note: I am well aware that the "flat list of dictionaries pickled in a file" representation isn't scalable. However, I am a believer of avoiding premature encapsulation. Goal is to keep things as flat as possible, as long as possible, and to avoid immediate over-engineering of things.

Lastly, this representation is actually kinda neat because it lets you run all kinds of nice queries very quickly using list comprehensions. For example:

#all papers by Andrew Ng
>>> [x['title'] for x in pubs if any("A. Ng" in a for a in x['authors'])]

-------------------------------------------------------------------------------
FAQ
-------------------------------------------------------------------------------
Q: Your file x does this, but that's bad practice, and you want to do y. Also you have a bug in z.
A: Most likely agreed. These scripts/functions are something I hacked together in 3 days during periods of about 1am to 6am. I'd be happy to hear thoughs/suggestions or see fixes or better/alternative ways of doing things. Check the website for this project, which comes with discussion forum attached.

-------------------------------------------------------------------------------
MANPOWER ADVERTISEMENTS / IDEAS
-------------------------------------------------------------------------------
Advertisement posting 1:
1. Pick your favorite conference/journal
2. Look through their page and write an HTML parser in style of my nips_download_parse.py
3. Output the same type of representation as described above in  a file 'pubs_conferenceblah'
4. Publish the scripts you used so that it is faster for others to do similar things
5. Upload your output pubs_ file, or send it to me for publishing

Advertisement posting 2:
It should be possible to take arbitrary directory full of PDF files, and create pubs_ file for them. Can Title, Authors be reliably extracted from PDFs somehow? Can tools be made that at least partially automate the process so that different parsers don't have to be written for each venue? Can we find large databases of papers/information online that we can scrape and enter?

Advertisement posting 3:
Heavy duty Machine Learning tools (such as Naive Bayes, lol) needed that can work on top of representations stored in pubs_ files and answer questions such as: 'what papers in database are most similar to the one on this url?', or, 'What are the common topics?'

etc etc...