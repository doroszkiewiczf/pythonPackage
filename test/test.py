from adviceAdder import advices
from adviceAdder import comments
from csvOperations import adviceCSVreader
from csvOperations import adviceCSVwriter
import sys


adviceList = list()

adviceList = adviceCSVreader.readAdvices(adviceList, 'advices.csv')

for i in range(adviceList.__len__()):
                sys.stdout.write(str(i) + ": ")
                print(adviceList[i].text)

adviceCSVwriter.writeAdvices(adviceList, 'advices5.csv')
advices.add_advice(adviceList)
advices.remove_advice(adviceList)
comments.add_comment(adviceList[0])

