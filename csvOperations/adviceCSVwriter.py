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

def writeAdvices(adviceList, fileName)
   with open(fileName, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|', quotechar=' ')
    for i in range(adviceList.__len__()):
        com_list = list()
        com_list.append(adviceList[i].title)
        com_list.append(adviceList[i].autor)
        com_list.append(adviceList[i].rate)
        com_list.append(adviceList[i].text)
        for j in range(adviceList[i].comments.__len__()):
            com_list.append(adviceList[i].comments[j].author)
            com_list.append(adviceList[i].comments[j].text)
        writer.writerow(com_list)

