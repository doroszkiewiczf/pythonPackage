import csv
class Comment(object):
    def __init__(self, author, text):
        self.author = author
        self.text = text

class Advice(object):
    def __init__(self, title, autor, rate, text, comments ):
    	self.title = title
        self.autor = autor
        self.rate = rate
        self.text = text
        self.comments = comments

def readAdvices(adviceList, fileName)
   with open(fileName, newline='') as csvfile:
       reader = csv.reader(csvfile, delimiter='|', quotechar=' ')
       for row in reader:
	   newComments = list()
	   for i in range(4, row.__len__(), 2):
	       newComent = Comment(row[i], row[i+1])
	       newComments.append(newComent)
	   newAdvice = Advice(row[0], row[1], float(row[2]), row[3], newComments)
	   adviceList.append(newAdvice)
   return adviceList

