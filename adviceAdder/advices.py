import sys

class Advice(object):


    def __init__(self, title, autor, rate, text, comments ):
        self.title = title
        self.autor = autor
        self.rate = rate
        self.text = text
        self.comments = comments

    def printing(self):

        print(self.title, "\t\t | Rate:", "%.2f" % self.rate,
              "\t\t | Comments", self.comments.__len__())

    def rated(self, rating, comm):

        self.rate = ((self.rate*self.comments.__len__())+rating)\
                    / (self.comments.__len__() + 1)
        self.comments.append(comm)



def add_advice(adviceList):
    advice_author = input("Author name: ")
    advice_title = input("Title: ")
    advice_text = input("Advice text: ")
    advice_comments = list()
    adviceList.append(Advice(advice_title, advice_author,
                         0, advice_text, advice_comments))


def remove_advice(adviceList):
    answ = True
    while answ:
        print('\n')
        i = 0
        for ad in adviceList:
            sys.stdout.write(str(i) + ": ")
            ad.printing()
            i += 1
        print('\n')
        answ = input("Choose advice to REMOVE or press e to go back ")
        if answ == "e":
            print(" Going back...")
            answ = False
        elif answ.isdigit():
            if -1 < int(answ) < adviceList.__len__():
                adlist.pop(int(answ))
            else:
                print("\n There is no advice with this number!")
        elif answ != "":
            print("\n Not Valid Choice Try again")
