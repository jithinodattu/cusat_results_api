PYTHON API FOR CUSAT RESULTS RETRIEVAL

REQUIREMENTS

	urllib2
	requests
	BeautifulSoup4

USAGE

	from cusat_results import *
	reg_no = '12090411'
	sem    = 'IV'              # 'I&II', 'II', 'III',....
	type   = 'Regular'         # Regular, Supplimentary, Special Supplementary 
	date   = 'APRIL 2013'      # 'NOV 2013', 'SEP 2013', 'JUNE 2013', 'AUG 2013', 'FEB 2013',...
	keywords = reg_no, sem, type, date # create a list of keywords
	scores = fetch(keywords)
