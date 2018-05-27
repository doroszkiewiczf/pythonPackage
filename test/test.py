from adviceAdder import advices
from adviceAdder import comments
from csvOperations import adviceCSVreader
from csvOperations import adviceCSVwriter

adviceList = list()

adviceCSVreader.readAdvices(adviceList, 'advices.csv')

for i in range(adviceList.__len__()):
                sys.stdout.write(str(i) + ": ")
                adviceList[i].printing()
