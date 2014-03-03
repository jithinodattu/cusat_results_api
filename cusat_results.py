import requests
from bs4 import BeautifulSoup

def fetch(keywords):
	params = extract_params(keywords)
	url    = "http://results.cusat.ac.in/regforms/mrklst-main.php"
	html   = query(url, params)
	bundle = souping(html)
	scores = extract_scores(bundle) 
	scores = add_details(scores, params)
	return scores

def souping(html):
	soup = BeautifulSoup(html)
	table = soup.findAll('table', {"width": "70%"})
	name      = str(table[0].find('b').get_text())
	branch    = str(table[1].findAll('td')[1].get_text())
	bundle = table[2].findAll('tr')		# list of tr containing score of each subject
	bundle[0] = name, branch			# remove first tr containing titles
	return bundle

def add_details(scores, params):
	for score in scores:
		score['reg_no']       = params["rno"]
		score['semester']     = params["sem"]
		score['exam_date']    = params["edate"]
		score['exam_type']    = params["exam"]
	return scores


def extract_scores(bundle):
	scores = []
	name = bundle[0][0]
	branch = bundle[0][1]
	del(bundle[0])
	for tr in bundle:
		score = {}
		score['name']         = name
		score['branch']       = branch
		td                    = tr.findAll('td')
		score['subject_code'] = str(td[0].get_text())
		score['subject']      = str(td[1].get_text())
		score['marks']        = str(td[2].get_text())
		score['result']       = str(td[3].get_text())
		scores.append(score)
	return scores


def query(url, params):
	req  = requests.post(url, params)
	html = req.content
	return html


def extract_params(data):
	reg_no    = data[0]
	semester  = data[1]
	exam_type = data[2]
	exam_date = data[3]
	params    = {"reg": "R", "rno": reg_no, "degree": "B.Tech", "sem": semester, "exam": exam_type, "edate": exam_date}
	print params
	return params

if __name__ == "__main__":
	print fetch(['12090411','IV', 'Regular', 'APRIL 2013'])




