import sys
import csv
import os
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_crmwindow import Ui_CRMWindow

BookDictCur = {"BookId": "", "Name": "", "Author": "", "Year": "","Rating": ""}
MaxBookId = 0

class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_CRMWindow()
        self.ui.setupUi(self)
        
        global MaxBookId
        global BookDictCur

        if os.path.exists('books.csv'):
          with open('books.csv') as f:
              reader = csv.DictReader(f, delimiter='|')
              for row in reader:
                  BookDictCur = row
                  MaxBookId = int(BookDictCur ['BookId'])
  
        # Initialization Line Edit
        #self.ui.leBookId.setText("5")
        self.ui.leBookId.setText(BookDictCur ['BookId'])  
        self.ui.leBookName.setText(BookDictCur ['Name'])
        self.ui.leAuthor.setText(BookDictCur ['Author'])
        self.ui.leYear.setText(BookDictCur ['Year'])
        self.ui.leRating.setText(BookDictCur ['Rating'])

        # Onclick event
        self.ui.pbAddBook.clicked.connect(self.AddBookClick)
        self.ui.leBookName.textChanged.connect(self.TextChanged)
        self.ui.leAuthor.textChanged.connect(self.TextChanged)
        #self.ui.leYear.textChanged.connect(self.TextChanged)
        #self.ui.leRating.textChanged.connect(self.TextChanged)
        self.ui.pbSearch.clicked.connect(self.SearchField)

    def IdentityBook(none):
        global MaxBookId
        MaxBookId += 1
        return MaxBookId

    def AddBookClick(self):
        # Add New Book
        BookDictCur ['BookId'] = str(self.IdentityBook())
        BookDictCur ['Name'] = self.ui.leBookName.text()
        BookDictCur ['Author'] = self.ui.leAuthor.text()
        BookDictCur ['Year'] = self.ui.leYear.text()
        BookDictCur ['Rating'] = self.ui.leRating.text()
        self.ui.pbAddBook.setEnabled(False)
        if os.path.exists('books.csv'):
          wr_option = 'a' 
        else:
          wr_option = 'w'      
        with open('books.csv', wr_option) as f:
            writer = csv.DictWriter(f, fieldnames=list(BookDictCur.keys()), delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
            if (wr_option == 'w'): writer.writeheader()  
            writer.writerow(BookDictCur)
        #print (BookDictCur ['BookId'] + "|" +BookDictCur['Name'] + "|" + BookDictCur['Author'] + "|" + BookDictCur['Year'] + "|" + BookDictCur['Rating'])
        self.ui.leBookId.setText(BookDictCur ['BookId'])      

    def TextChanged(self):
        # Call when change text in EditLine
        # print (self.ui.leBookName.text() + "|" + BookDictCur["Name"])
        if (self.ui.leBookName.text() != BookDictCur["Name"]) or (self.ui.leAuthor.text() != BookDictCur["Author"]): #or (self.ui.leYear.text() != BookDictCur["Year"]) or (self.ui.leRating.text() != BookDictCur["Rating"]*/):
           #print("Enabled")
           self.ui.pbAddBook.setEnabled(True)
        else:
           #print("Disabled")
           self.ui.pbAddBook.setEnabled(False)
    
    def SearchField(self):
        if os.path.exists('books.csv'):
          with open('books.csv') as f:
              reader = csv.DictReader(f, delimiter='|')
              for row in reader:
                  BookDictCur = row
                  if (BookDictCur[self.ui.comboBox.currentText()] == self.ui.leSearchValue.text()):
                      print (BookDictCur ['BookId'] + "|" +BookDictCur['Name'] + "|" + BookDictCur['Author'] + "|" + BookDictCur['Year'] + "|" + BookDictCur['Rating'])
                      #break
              print ('')       
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())