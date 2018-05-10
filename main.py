import sys


# Импортируем наш интерфейс из файла
from untitled import *
from PyQt5 import QtCore, QtGui, QtWidgets
from holdem_argparser import parse_cards
from holdem_calc import run


class MyWin(QtWidgets.QMainWindow):
  def __init__(untitled, parent=None):
    QtWidgets.QWidget.__init__(untitled, parent)

    untitled.ui = Ui_MainWindow()
    untitled.ui.setupUi(untitled)
    untitled.ui.textBrowser.setText("");
    # Здесь прописываем событие нажатия на кнопку
    untitled.ui.pushButton_55.clicked.connect(untitled.pushButton_55)
    untitled.ui.Board.clicked.connect(untitled.Board)
    untitled.ui.unknown_card.clicked.connect(untitled.unknown_card)

    untitled.ui.S_A.clicked.connect(untitled.S_A)
    untitled.ui.S_A.setIcon(QtGui.QIcon("img/S_A.jpg"))
    untitled.ui.S_A.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_2.clicked.connect(untitled.S_2)
    untitled.ui.S_2.setIcon(QtGui.QIcon("img/S_2.jpg"))
    untitled.ui.S_2.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_3.clicked.connect(untitled.S_3)
    untitled.ui.S_3.setIcon(QtGui.QIcon("img/S_3.jpg"))
    untitled.ui.S_3.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_4.clicked.connect(untitled.S_4)
    untitled.ui.S_4.setIcon(QtGui.QIcon("img/S_4.jpg"))
    untitled.ui.S_4.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_5.clicked.connect(untitled.S_5)
    untitled.ui.S_5.setIcon(QtGui.QIcon("img/S_5.jpg"))
    untitled.ui.S_5.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_6.clicked.connect(untitled.S_6)
    untitled.ui.S_6.setIcon(QtGui.QIcon("img/S_6.jpg"))
    untitled.ui.S_6.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_7.clicked.connect(untitled.S_7)
    untitled.ui.S_7.setIcon(QtGui.QIcon("img/S_7.jpg"))
    untitled.ui.S_7.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_8.clicked.connect(untitled.S_8)
    untitled.ui.S_8.setIcon(QtGui.QIcon("img/S_8.jpg"))
    untitled.ui.S_8.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_9.clicked.connect(untitled.S_9)
    untitled.ui.S_9.setIcon(QtGui.QIcon("img/S_9.jpg"))
    untitled.ui.S_9.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_T.clicked.connect(untitled.S_T)
    untitled.ui.S_T.setIcon(QtGui.QIcon("img/S_T.jpg"))
    untitled.ui.S_T.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_J.clicked.connect(untitled.S_J)
    untitled.ui.S_J.setIcon(QtGui.QIcon("img/S_J.jpg"))
    untitled.ui.S_J.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_Q.clicked.connect(untitled.S_Q)
    untitled.ui.S_Q.setIcon(QtGui.QIcon("img/S_Q.jpg"))
    untitled.ui.S_Q.setIconSize(QtCore.QSize(70,70))
    untitled.ui.S_K.clicked.connect(untitled.S_K)
    untitled.ui.S_K.setIcon(QtGui.QIcon("img/S_K.jpg"))
    untitled.ui.S_K.setIconSize(QtCore.QSize(70,70))

    untitled.ui.C_A.clicked.connect(untitled.C_A)
    untitled.ui.C_A.setIcon(QtGui.QIcon("img/C_A.jpg"))
    untitled.ui.C_A.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_2.clicked.connect(untitled.C_2)
    untitled.ui.C_2.setIcon(QtGui.QIcon("img/C_2.jpg"))
    untitled.ui.C_2.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_3.clicked.connect(untitled.C_3)
    untitled.ui.C_3.setIcon(QtGui.QIcon("img/C_2.jpg"))
    untitled.ui.C_3.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_4.clicked.connect(untitled.C_4)
    untitled.ui.C_4.setIcon(QtGui.QIcon("img/C_4.jpg"))
    untitled.ui.C_4.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_5.clicked.connect(untitled.C_5)
    untitled.ui.C_5.setIcon(QtGui.QIcon("img/C_5.jpg"))
    untitled.ui.C_5.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_6.clicked.connect(untitled.C_6)
    untitled.ui.C_6.setIcon(QtGui.QIcon("img/C_6.jpg"))
    untitled.ui.C_6.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_7.clicked.connect(untitled.C_7)
    untitled.ui.C_7.setIcon(QtGui.QIcon("img/C_7.jpg"))
    untitled.ui.C_7.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_8.clicked.connect(untitled.C_8)
    untitled.ui.C_8.setIcon(QtGui.QIcon("img/C_8.jpg"))
    untitled.ui.C_8.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_9.clicked.connect(untitled.C_9)
    untitled.ui.C_9.setIcon(QtGui.QIcon("img/C_9.jpg"))
    untitled.ui.C_9.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_T.clicked.connect(untitled.C_T)
    untitled.ui.C_T.setIcon(QtGui.QIcon("img/C_T.jpg"))
    untitled.ui.C_T.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_J.clicked.connect(untitled.C_J)
    untitled.ui.C_J.setIcon(QtGui.QIcon("img/C_J.jpg"))
    untitled.ui.C_J.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_Q.clicked.connect(untitled.C_Q)
    untitled.ui.C_Q.setIcon(QtGui.QIcon("img/C_Q.jpg"))
    untitled.ui.C_Q.setIconSize(QtCore.QSize(70,70))
    untitled.ui.C_K.clicked.connect(untitled.C_K)
    untitled.ui.C_K.setIcon(QtGui.QIcon("img/C_K.jpg"))
    untitled.ui.C_K.setIconSize(QtCore.QSize(70,70))


    untitled.ui.H_A.clicked.connect(untitled.H_A)
    untitled.ui.H_A.setIcon(QtGui.QIcon("img/H_A.jpg"))
    untitled.ui.H_A.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_2.clicked.connect(untitled.H_2)
    untitled.ui.H_2.setIcon(QtGui.QIcon("img/H_2.jpg"))
    untitled.ui.H_2.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_3.clicked.connect(untitled.H_3)
    untitled.ui.H_3.setIcon(QtGui.QIcon("img/H_3.jpg"))
    untitled.ui.H_3.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_4.clicked.connect(untitled.H_4)
    untitled.ui.H_4.setIcon(QtGui.QIcon("img/H_4.jpg"))
    untitled.ui.H_4.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_5.clicked.connect(untitled.H_5)
    untitled.ui.H_5.setIcon(QtGui.QIcon("img/H_5.jpg"))
    untitled.ui.H_5.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_6.clicked.connect(untitled.H_6)
    untitled.ui.H_6.setIcon(QtGui.QIcon("img/H_6.jpg"))
    untitled.ui.H_6.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_7.clicked.connect(untitled.H_7)
    untitled.ui.H_7.setIcon(QtGui.QIcon("img/H_7.jpg"))
    untitled.ui.H_7.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_8.clicked.connect(untitled.H_8)
    untitled.ui.H_8.setIcon(QtGui.QIcon("img/H_8.jpg"))
    untitled.ui.H_8.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_9.clicked.connect(untitled.H_9)
    untitled.ui.H_9.setIcon(QtGui.QIcon("img/H_9.jpg"))
    untitled.ui.H_9.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_T.clicked.connect(untitled.H_T)
    untitled.ui.H_T.setIcon(QtGui.QIcon("img/H_T.jpg"))
    untitled.ui.H_T.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_J.clicked.connect(untitled.H_J)
    untitled.ui.H_J.setIcon(QtGui.QIcon("img/H_J.jpg"))
    untitled.ui.H_J.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_Q.clicked.connect(untitled.H_Q)
    untitled.ui.H_Q.setIcon(QtGui.QIcon("img/H_Q.jpg"))
    untitled.ui.H_Q.setIconSize(QtCore.QSize(70,70))
    untitled.ui.H_K.clicked.connect(untitled.H_K)
    untitled.ui.H_K.setIcon(QtGui.QIcon("img/H_K.jpg"))
    untitled.ui.H_K.setIconSize(QtCore.QSize(70,70))

    untitled.ui.D_A.clicked.connect(untitled.D_A)
    untitled.ui.D_A.setIcon(QtGui.QIcon("img/D_A.jpg"))
    untitled.ui.D_A.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_2.clicked.connect(untitled.D_2)
    untitled.ui.D_2.setIcon(QtGui.QIcon("img/D_2.jpg"))
    untitled.ui.D_2.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_3.clicked.connect(untitled.D_3)
    untitled.ui.D_3.setIcon(QtGui.QIcon("img/D_3.jpg"))
    untitled.ui.D_3.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_4.clicked.connect(untitled.D_4)
    untitled.ui.D_4.setIcon(QtGui.QIcon("img/D_4.jpg"))
    untitled.ui.D_4.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_5.clicked.connect(untitled.D_5)
    untitled.ui.D_5.setIcon(QtGui.QIcon("img/D_5.jpg"))
    untitled.ui.D_5.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_6.clicked.connect(untitled.D_6)
    untitled.ui.D_6.setIcon(QtGui.QIcon("img/D_6.jpg"))
    untitled.ui.D_6.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_7.clicked.connect(untitled.D_7)
    untitled.ui.D_7.setIcon(QtGui.QIcon("img/D_7.jpg"))
    untitled.ui.D_7.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_8.clicked.connect(untitled.D_8)
    untitled.ui.D_8.setIcon(QtGui.QIcon("img/D_8.jpg"))
    untitled.ui.D_8.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_9.clicked.connect(untitled.D_9)
    untitled.ui.D_9.setIcon(QtGui.QIcon("img/D_9.jpg"))
    untitled.ui.D_9.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_T.clicked.connect(untitled.D_T)
    untitled.ui.D_T.setIcon(QtGui.QIcon("img/D_T.jpg"))
    untitled.ui.D_T.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_J.clicked.connect(untitled.D_J)
    untitled.ui.D_J.setIcon(QtGui.QIcon("img/D_J.jpg"))
    untitled.ui.D_J.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_Q.clicked.connect(untitled.D_Q)
    untitled.ui.D_Q.setIcon(QtGui.QIcon("img/D_Q.jpg"))
    untitled.ui.D_Q.setIconSize(QtCore.QSize(70,70))
    untitled.ui.D_K.clicked.connect(untitled.D_K)
    untitled.ui.D_K.setIcon(QtGui.QIcon("img/D_K.jpg"))
    untitled.ui.D_K.setIconSize(QtCore.QSize(70,70))

    #board
    untitled.ui.Board.setIcon(QtGui.QIcon("img/board.jpg"))
    untitled.ui.Board.setIconSize(QtCore.QSize(60,60))

    #unknown_card
    untitled.ui.unknown_card.setIcon(QtGui.QIcon("img/unknown_card.jpg"))
    untitled.ui.unknown_card.setIconSize(QtCore.QSize(60,60))
    
    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
  def S_A(untitled):
    untitled.ui.plainTextEdit.insertPlainText('As ')  
    untitled.ui.S_A.setEnabled(False)
  def S_2(untitled):
    untitled.ui.plainTextEdit.insertPlainText('2s ')
    untitled.ui.S_2.setEnabled(False)
  def S_3(untitled):
    untitled.ui.plainTextEdit.insertPlainText('3s ')
    untitled.ui.S_3.setEnabled(False)
  def S_4(untitled):
    untitled.ui.plainTextEdit.insertPlainText('4s ')
    untitled.ui.S_4.setEnabled(False)
  def S_5(untitled):
    untitled.ui.plainTextEdit.insertPlainText('5s ')
    untitled.ui.S_5.setEnabled(False)
  def S_6(untitled):
    untitled.ui.plainTextEdit.insertPlainText('6s ')
    untitled.ui.S_6.setEnabled(False)
  def S_7(untitled):
    untitled.ui.plainTextEdit.insertPlainText('7s ')
    untitled.ui.S_7.setEnabled(False)
  def S_8(untitled):
    untitled.ui.plainTextEdit.insertPlainText('8s ')
    untitled.ui.S_8.setEnabled(False)
  def S_9(untitled):
    untitled.ui.plainTextEdit.insertPlainText('9s ')
    untitled.ui.S_9.setEnabled(False)
  def S_T(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Ts ')
    untitled.ui.S_T.setEnabled(False)
  def S_J(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Js ')
    untitled.ui.S_J.setEnabled(False)
  def S_Q(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Qs ')
    untitled.ui.S_Q.setEnabled(False)
  def S_K(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Ks ')
    untitled.ui.S_K.setEnabled(False)
    untitled.ui.S_K.setEnabled(False)

  def C_A(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Ac ')  
    untitled.ui.C_A.setEnabled(False)
  def C_2(untitled):
    untitled.ui.plainTextEdit.insertPlainText('2c ')
    untitled.ui.C_2.setEnabled(False)
  def C_3(untitled):
    untitled.ui.plainTextEdit.insertPlainText('3c ')
    untitled.ui.C_3.setEnabled(False)
  def C_4(untitled):
    untitled.ui.plainTextEdit.insertPlainText('4c ')
    untitled.ui.C_4.setEnabled(False)
  def C_5(untitled):
    untitled.ui.plainTextEdit.insertPlainText('5c ')
    untitled.ui.C_5.setEnabled(False)
  def C_6(untitled):
    untitled.ui.plainTextEdit.insertPlainText('6c ')
    untitled.ui.C_6.setEnabled(False)
  def C_7(untitled):
    untitled.ui.plainTextEdit.insertPlainText('7c ')
    untitled.ui.C_7.setEnabled(False)
  def C_8(untitled):
    untitled.ui.plainTextEdit.insertPlainText('8c ')
    untitled.ui.C_8.setEnabled(False)
  def C_9(untitled):
    untitled.ui.plainTextEdit.insertPlainText('9c ')
    untitled.ui.C_9.setEnabled(False)
  def C_T(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Tc ')
    untitled.ui.C_T.setEnabled(False)
  def C_J(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Jc ')
    untitled.ui.C_J.setEnabled(False)
  def C_Q(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Qc ')
    untitled.ui.C_Q.setEnabled(False)
  def C_K(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Kc ')
    untitled.ui.C_K.setEnabled(False)

  def H_A(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Ah ')  
    untitled.ui.H_A.setEnabled(False)
  def H_2(untitled):
    untitled.ui.plainTextEdit.insertPlainText('2h ')
    untitled.ui.H_2.setEnabled(False)
  def H_3(untitled):
    untitled.ui.plainTextEdit.insertPlainText('3h ')
    untitled.ui.H_3.setEnabled(False)
  def H_4(untitled):
    untitled.ui.plainTextEdit.insertPlainText('4h ')
    untitled.ui.H_4.setEnabled(False)
  def H_5(untitled):
    untitled.ui.plainTextEdit.insertPlainText('5h ')
    untitled.ui.H_5.setEnabled(False)
  def H_6(untitled):
    untitled.ui.plainTextEdit.insertPlainText('6h ')
    untitled.ui.H_6.setEnabled(False)
  def H_7(untitled):
    untitled.ui.plainTextEdit.insertPlainText('7h ')
    untitled.ui.H_7.setEnabled(False)
  def H_8(untitled):
    untitled.ui.plainTextEdit.insertPlainText('8h ')
    untitled.ui.H_8.setEnabled(False)
  def H_9(untitled):
    untitled.ui.plainTextEdit.insertPlainText('9h ')
    untitled.ui.H_9.setEnabled(False)
  def H_T(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Th ')
    untitled.ui.H_T.setEnabled(False)
  def H_J(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Jh ')
    untitled.ui.H_J.setEnabled(False)
  def H_Q(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Qh ')
    untitled.ui.H_Q.setEnabled(False)
  def H_K(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Kh ')
    untitled.ui.H_K.setEnabled(False)

  def D_A(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Ad ')  
    untitled.ui.D_A.setEnabled(False)
  def D_2(untitled):
    untitled.ui.plainTextEdit.insertPlainText('2d ')
    untitled.ui.D_2.setEnabled(False)
  def D_3(untitled):
    untitled.ui.plainTextEdit.insertPlainText('3d ')
    untitled.ui.D_3.setEnabled(False)
  def D_4(untitled):
    untitled.ui.plainTextEdit.insertPlainText('4d ')
    untitled.ui.D_4.setEnabled(False)
  def D_5(untitled):
    untitled.ui.plainTextEdit.insertPlainText('5d ')
    untitled.ui.D_5.setEnabled(False)
  def D_6(untitled):
    untitled.ui.plainTextEdit.insertPlainText('6d ')
    untitled.ui.D_6.setEnabled(False)
  def D_7(untitled):
    untitled.ui.plainTextEdit.insertPlainText('7d ')
    untitled.ui.D_7.setEnabled(False)
  def D_8(untitled):
    untitled.ui.plainTextEdit.insertPlainText('8d ')
    untitled.ui.D_8.setEnabled(False)
  def D_9(untitled):
    untitled.ui.plainTextEdit.insertPlainText('9d ')
    untitled.ui.D_9.setEnabled(False)
  def D_T(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Td ')
    untitled.ui.D_T.setEnabled(False)
  def D_J(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Jd ')
    untitled.ui.D_J.setEnabled(False)
  def D_Q(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Qd ')
    untitled.ui.D_Q.setEnabled(False)
  def D_K(untitled):
    untitled.ui.plainTextEdit.insertPlainText('Kd ')
    untitled.ui.D_K.setEnabled(False)

  def Board(untitled):
    untitled.ui.plainTextEdit.insertPlainText('-b ')
    untitled.ui.Board.setEnabled(False)


  def unknown_card(untitled):
    untitled.ui.plainTextEdit.insertPlainText('? ')

  def pushButton_55(untitled):
    rezultat=''
    text = open('text.txt').read()
    textBoard = open('Board.txt').read()
    
    newStr = untitled.ui.plainTextEdit.toPlainText()
    lengthOfString = len(newStr)
    newStrBoard = ""
    newStrPlayer = ""

    if "b" in  newStr:
      indexOfBoard = newStr.index("b")
      
      for i in range(indexOfBoard + 2,lengthOfString):
        newStrBoard = newStrBoard + newStr[i]

      for i in range(0,indexOfBoard - 2):
        newStrPlayer = newStrPlayer + newStr[i]

      
      cardsOfBoard = newStrBoard.strip().split(' ')
      cardsOfPlayer = newStrPlayer.strip().split(' ')
      
      if len(cardsOfBoard) < 9 and len(cardsOfBoard) > 15:
        untitled.ui.textBrowser.setText("Board must have a length of 3, 4, or 5.")
        untitled.ui.textBrowser.update()
        
      else:
        cards, board = parse_cards(cardsOfPlayer, cardsOfBoard)
        run(cards, 100000, False, board, None, True)
        text = open('text.txt').read()
        untitled.ui.textBrowser.setText(text);

      # # if len(newStrBoard) < 9 or len(newStrBoard) > 15:
      #   textBoard = open('Board.txt').read()
      #   untitled.ui.textBrowser.setText(textBoard)
      #   print(len(newStrBoard))
      # else:
      
    elif newStr == "":
        untitled.ui.textBrowser.setText("You enter empty string")
    elif lengthOfString % 2 == 1:
        untitled.ui.textBrowser.setText("You must provide a even number of hole cards")
    else:
        cards, board = parse_cards(newStr.strip().split(' '), None)
        run(cards, 100000, False, board, None, True)
    # mas = newStr.split('\n')
    # rezultat += newStr
        text = open('text.txt').read()
        untitled.ui.textBrowser.setText(text);
    newStr = newStr = untitled.ui.plainTextEdit.setText("");
    untitled.ui.S_A.setEnabled(True)
    untitled.ui.S_2.setEnabled(True)
    untitled.ui.S_3.setEnabled(True)
    untitled.ui.S_4.setEnabled(True)
    untitled.ui.S_5.setEnabled(True)
    untitled.ui.S_6.setEnabled(True)
    untitled.ui.S_7.setEnabled(True)
    untitled.ui.S_8.setEnabled(True)
    untitled.ui.S_9.setEnabled(True)
    untitled.ui.S_T.setEnabled(True)
    untitled.ui.S_J.setEnabled(True)
    untitled.ui.S_Q.setEnabled(True)
    untitled.ui.S_K.setEnabled(True)

    untitled.ui.H_2.setEnabled(True)
    untitled.ui.H_3.setEnabled(True)
    untitled.ui.H_4.setEnabled(True)
    untitled.ui.H_5.setEnabled(True)
    untitled.ui.H_6.setEnabled(True)
    untitled.ui.H_7.setEnabled(True)
    untitled.ui.H_8.setEnabled(True)
    untitled.ui.H_9.setEnabled(True)
    untitled.ui.H_T.setEnabled(True)
    untitled.ui.H_J.setEnabled(True)
    untitled.ui.H_Q.setEnabled(True)
    untitled.ui.H_K.setEnabled(True)

    untitled.ui.C_2.setEnabled(True)
    untitled.ui.C_3.setEnabled(True)
    untitled.ui.C_4.setEnabled(True)
    untitled.ui.C_5.setEnabled(True)
    untitled.ui.C_6.setEnabled(True)
    untitled.ui.C_7.setEnabled(True)
    untitled.ui.C_8.setEnabled(True)
    untitled.ui.C_9.setEnabled(True)
    untitled.ui.C_T.setEnabled(True)
    untitled.ui.C_J.setEnabled(True)
    untitled.ui.C_Q.setEnabled(True)
    untitled.ui.C_K.setEnabled(True)

    untitled.ui.D_2.setEnabled(True)
    untitled.ui.D_3.setEnabled(True)
    untitled.ui.D_4.setEnabled(True)
    untitled.ui.D_5.setEnabled(True)
    untitled.ui.D_6.setEnabled(True)
    untitled.ui.D_7.setEnabled(True)
    untitled.ui.D_8.setEnabled(True)
    untitled.ui.D_9.setEnabled(True)
    untitled.ui.D_T.setEnabled(True)
    untitled.ui.D_J.setEnabled(True)
    untitled.ui.D_Q.setEnabled(True)
    untitled.ui.D_K.setEnabled(True)

    untitled.ui.Board.setEnabled(True)


if __name__=="__main__":
  app = QtWidgets.QApplication(sys.argv)
  myapp = MyWin()
  myapp.show()
  sys.exit(app.exec_())
