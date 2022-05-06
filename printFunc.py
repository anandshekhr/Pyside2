#helps in including print functions in python Pyside2

#libraries
from PySide2 import QtPrintSupport
from PySide2 import QtWidgets,QtGui
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#function with different operations

#function to show printer dialog box in GUI
def print_file():
    dialog = QtPrintSupport.QPrintDialog()
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        handlePaintRequestForBOM(dialog.printer())

#------------Print Preview in GUI------------------------------------------------------------------------------------------
def printPreview_file(self):
    dialog = QtPrintSupport.QPrintPreviewDialog()
    dialog.paintRequested.connect(handlePaintRequestForBOM)
    dialog.exec_()

#------------Print handler to print Table widget Data-------------------------------------------------------------------------------------------------------------------
def handlePaintRequestForBOM(printer):
    #make tables on printing page and view table widget data from GUI to print page
    tableFormat = QtGui.QTextTableFormat()

    #setting for table like border size , border style, cell spacing, top Margin, cell padding
    tableFormat.setBorder(0.5)
    tableFormat.setBorderStyle(QTextFrameFormat.BorderStyle.BorderStyle_Inset)
    tableFormat.setCellSpacing(0)
    tableFormat.setTopMargin(5)
    tableFormat.setCellPadding(10)
    document = QtGui.QTextDocument()
    cursor = QtGui.QTextCursor(document)
    table = cursor.insertTable(
        TableWidgetName.rowCount(), 5,tableFormat)
    
    for row in range(table.rows()):
        for col in range(0,5):
            # set cursor position and insert text at the specific position
            cursor.insertText(TableWidgetName.item(row, col).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
    document.print_(printer)    
