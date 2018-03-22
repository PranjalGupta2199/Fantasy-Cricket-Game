import sys
from PyQt4.QtGui import *

app = QApplication (sys.argv)

listwidget = QlistWidget()

for i in range (10):
        item = QListWidgetItem("Item %i" %i)
        listwidget.addItem(item)
 
listwidget.show()
sys.exit(app.exec_())
