import sys


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
