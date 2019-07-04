
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
import os

def iconFromBase64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.showMaximized()
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.wantWidth = self.screen.width()
        self.wantHeight = self.screen.height()
        main.setGeometry(0, 0, self.wantWidth, self.wantHeight)
        main.setWindowIcon(iconFromBase64(ico))
        main.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint)
        main.setStyleSheet("QWidget {background-color : #000000}")

        main.setWindowTitle("Myers-Briggs Type Indicator")

        self.index = [
            {"rangeStart": 0, "resultA": 0, "resultB": 1},
            {"rangeStart": 1, "resultA": 2, "resultB": 3},
            {"rangeStart": 2, "resultA": 2, "resultB": 3},
            {"rangeStart": 3, "resultA": 4, "resultB": 5},
            {"rangeStart": 4, "resultA": 4, "resultB": 5},
            {"rangeStart": 5, "resultA": 6, "resultB": 7},
            {"rangeStart": 6, "resultA": 6, "resultB": 7}
        ]
        
        self.result = [0, 0, 0, 0, 0, 0, 0, 0, ""]

        self.nowCol = 0
        self.maxCol = len(self.index)
        self.nowI = 0
        self.maxI = 10

        #tree_question
        self.tree_question = ET.parse('mbti_sorted.xml')
        self.tree_question_root = self.tree_question.getroot()
        self.questions = []
        for elem in self.tree_question_root:
            att = elem.attrib
            self.questions.append((att["id"], att["q"], att["a"], att["b"]))
        self.questions.append(["", "", "", ""])

        #tree_OneOfEight
        self.tree_result = ET.parse('mbti_result.xml')
        self.tree_result_root = self.tree_result.getroot()
        self.desc_result = {}
        for elem in self.tree_result_root:
            att = elem.attrib
            content = elem.text
            self.desc_result[att["id"]] = (att["title"], content)

        self.buttonFont = QtGui.QFont("Consolas", 20, QtGui.QFont.Normal)

        self.leftBtn = QtWidgets.QPushButton(main)
        self.leftBtn.setGeometry(QtCore.QRect(
            self.wantWidth/10, self.wantHeight/1.9, self.wantWidth*8/10, self.wantWidth/12))
        self.leftBtn.setObjectName("leftBtn")
        self.leftBtn.setFont(self.buttonFont)
        self.leftBtn.setStyleSheet(
            "QPushButton {background-color : rgb(50,50,50);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(104,33,122);color : #FFFFFF;}")
        self.leftBtn.show()

        self.rightBtn = QtWidgets.QPushButton(main)
        self.rightBtn.setGeometry(QtCore.QRect(
            self.wantWidth/10, self.wantHeight*11/16, self.wantWidth*8/10, self.wantWidth/12))
        self.rightBtn.setObjectName("rightBtn")
        self.rightBtn.setFont(self.buttonFont)
        self.rightBtn.setStyleSheet(
            "QPushButton {background-color : rgb(50,50,50);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(104,33,122);color : #FFFFFF;}")
        self.rightBtn.show()
        
        self.questionLabel = QtWidgets.QLabel(main)
        self.questionLabel.setGeometry(QtCore.QRect(
            0, self.wantHeight/2.5, self.wantWidth, 60))
        self.questionLabel.setObjectName("questionLabel")
        self.LabelFont = QtGui.QFont("Consolas", 28, QtGui.QFont.Normal)
        self.questionLabel.setFont(self.LabelFont)
        self.questionLabel.setStyleSheet(
            "QLabel {color : #FFFFFF;background-color:None}")
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.show()

        self.resultLabelFont = QtGui.QFont("Consolas", 90, QtGui.QFont.Normal)

        self.resultLabel = QtWidgets.QLabel(main)
        self.resultLabel.setGeometry(QtCore.QRect(self.wantWidth/16, self.wantHeight*5.5/16, self.wantWidth*14/16, self.wantHeight/8))
        self.resultLabel.setObjectName("resultLabel")
        self.resultLabel.setFont(QtGui.QFont("Consolas", 48, QtGui.QFont.Normal))
        self.resultLabel.setStyleSheet("QLabel {background-color : rgb(50,50,50,0%);color : #FFFFFF;}")
        self.resultLabel.setText("")
        self.resultLabel.hide()

        self.resultLabelDesc = QtWidgets.QLabel(main)
        self.resultLabelDesc.setGeometry(QtCore.QRect(self.wantWidth/16, self.wantHeight*7.5/16, self.wantWidth*14/16, self.wantHeight*7/16))
        self.resultLabelDesc.setObjectName("resultLabelDesc")
        self.resultLabelDesc.setFont(QtGui.QFont("Consolas", 20, QtGui.QFont.Normal))
        self.resultLabelDesc.setStyleSheet("QLabel {background-color : rgb(50,50,50,50%);color : #FFFFFF;margin:15px;}")
        self.resultLabelDesc.setText("")
        self.resultLabelDesc.setWordWrap(True)
        self.resultLabelDesc.hide()

        self.resultLabel1a = QtWidgets.QPushButton(main)
        self.resultLabel1a.setGeometry(QtCore.QRect(self.wantWidth/2-self.wantHeight*3/8, self.wantHeight/8, 0, 128))
        self.resultLabel1a.setObjectName("resultLabel1a")
        self.resultLabel1a.setStyleSheet("QPushButton {background-color : rgb(104,33,122,100%);}")
        self.resultLabel1a.show()

        self.resultLabel2a = QtWidgets.QPushButton(main)
        self.resultLabel2a.setGeometry(QtCore.QRect(
            self.wantWidth/2-self.wantHeight*1.5/8, self.wantHeight/8, 0, 128))
        self.resultLabel2a.setObjectName("resultLabel2a")
        self.resultLabel2a.setStyleSheet("QPushButton {background-color : rgb(104,33,122,100%);}")
        self.resultLabel2a.show()

        self.resultLabel3a = QtWidgets.QPushButton(main)
        self.resultLabel3a.setGeometry(QtCore.QRect(
            self.wantWidth/2, self.wantHeight/8, 0, 128))
        self.resultLabel3a.setObjectName("resultLabel3a")
        self.resultLabel3a.setStyleSheet("QPushButton {background-color : rgb(104,33,122,100%);}")
        self.resultLabel3a.show()

        self.resultLabel4a = QtWidgets.QPushButton(main)
        self.resultLabel4a.setGeometry(QtCore.QRect(
            self.wantWidth/2+self.wantHeight*1.5/8, self.wantHeight/8, 0, 128))
        self.resultLabel4a.setObjectName("resultLabel4a")
        self.resultLabel4a.setStyleSheet("QPushButton {background-color : rgb(104,33,122,100%);}")
        self.resultLabel4a.show()

        self.resultLabel1 = QtWidgets.QPushButton(main)
        self.resultLabel1.setGeometry(QtCore.QRect(
            self.wantWidth/2-self.wantHeight*3/8, self.wantHeight/8, 128, 128))
        self.resultLabel1.setObjectName("resultLabel1")
        self.resultLabel1.setFont(self.resultLabelFont)
        self.resultLabel1.setStyleSheet("QPushButton {background-color : rgb(50,50,50,50%);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(104,33,122,50%);color : #FFFFFF;}")
        self.resultLabel1.setText("?")
        self.resultLabel1.show()

        self.resultLabel2 = QtWidgets.QPushButton(main)
        self.resultLabel2.setGeometry(QtCore.QRect(
            self.wantWidth/2-self.wantHeight*1.5/8, self.wantHeight/8, 128, 128))
        self.resultLabel2.setObjectName("resultLabel2")
        self.resultLabel2.setFont(self.resultLabelFont)
        self.resultLabel2.setStyleSheet(
            "QPushButton {background-color : rgb(50,50,50,50%);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(104,33,122,50%);color : #FFFFFF;}")
        self.resultLabel2.setText("?")
        self.resultLabel2.show()

        self.resultLabel3 = QtWidgets.QPushButton(main)
        self.resultLabel3.setGeometry(QtCore.QRect(
            self.wantWidth/2, self.wantHeight/8, 128, 128))
        self.resultLabel3.setObjectName("resultLabel3")
        self.resultLabel3.setFont(self.resultLabelFont)
        self.resultLabel3.setStyleSheet("QPushButton {background-color : rgb(50,50,50,50%);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(104,33,122,50%);color : #FFFFFF;}")
        self.resultLabel3.setText("?")
        self.resultLabel3.show()

        self.resultLabel4 = QtWidgets.QPushButton(main)
        self.resultLabel4.setGeometry(QtCore.QRect(
            self.wantWidth/2+self.wantHeight*1.5/8, self.wantHeight/8, 128, 128))
        self.resultLabel4.setObjectName("resultLabel4")
        self.resultLabel4.setFont(self.resultLabelFont)
        self.resultLabel4.setStyleSheet("QPushButton {background-color : rgb(50,50,50,50%);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(104,33,122,50%);color : #FFFFFF;}")
        self.resultLabel4.setText("?")
        self.resultLabel4.show()

        self.resetButton = QtWidgets.QPushButton(main)
        self.resetButton.setGeometry(QtCore.QRect(
            self.wantWidth*1.5/16, self.wantHeight/8, 128, 128))
        self.resetButton.setObjectName("resultLabel4")
        self.resetButton.setFont(QtGui.QFont("Consolas", 60, QtGui.QFont.Normal))
        self.resetButton.setStyleSheet("QPushButton {background-color : rgb(50,50,50,50%);color : #FFFFFF;}QPushButton::hover{background-color :  rgb(150,33,33,90%);color : #FFFFFF;}")
        self.resetButton.setText("⏎")
        self.resetButton.show()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(main)

        self.leftBtn.clicked.connect(self.leftBtnClicked)
        self.rightBtn.clicked.connect(self.rightBtnClicked)
        self.resetButton.clicked.connect(self.resetClicked)

    def resetClicked(self):
        self.result = [0, 0, 0, 0, 0, 0, 0, 0, ""]
        self.nowCol = 0
        self.nowI = 0
        self.resultLabel1.setText("?")
        self.resultLabel2.setText("?")
        self.resultLabel3.setText("?")
        self.resultLabel4.setText("?")

        self.leftBtn.show()
        self.rightBtn.show()
        self.questionLabel.show()
        self.resultLabel.setText("")
        self.resultLabelDesc.setText("")
        self.resultLabel.hide()
        self.resultLabelDesc.hide()
        self.retranslateUi()

        self.resultLabel1a.resize(0,128)
        self.resultLabel2a.resize(0,128)
        self.resultLabel3a.resize(0,128)
        self.resultLabel4a.resize(0,128)

    def leftBtnClicked(self):
        self.result[self.index[self.nowCol]["resultA"]] += 1
        if self.nowCol < self.maxCol:
            if self.nowI < self.maxI:
                self.nowI += 1
                
                if self.nowCol == 0:
                    self.resultLabel1a.resize(self.nowI/self.maxI*128,128)
                elif self.nowCol == 1:
                    self.resultLabel2a.resize(self.nowI/self.maxI*64,128)
                elif self.nowCol == 2:
                    self.resultLabel2a.resize(64+self.nowI/self.maxI*64,128)
                elif self.nowCol == 3:
                    self.resultLabel3a.resize(self.nowI/self.maxI*64,128)
                elif self.nowCol == 4:
                    self.resultLabel3a.resize(64+self.nowI/self.maxI*64,128)
                elif self.nowCol == 5:
                    self.resultLabel4a.resize(self.nowI/self.maxI*64,128)
                elif self.nowCol == 6:
                    self.resultLabel4a.resize(64+self.nowI/self.maxI*64,128)

                self.retranslateUi()

            if self.nowI == self.maxI:
                tempRes = ""
                if self.nowCol == 0:
                    tempRes = self.findFinal(0, 1, 'E', 'I')
                    self.resultLabel1.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel1a.resize(0,0)
                elif self.nowCol == 2:
                    tempRes = self.findFinal(2, 3, 'S', 'N')
                    self.resultLabel2.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel2a.resize(0,0)
                elif self.nowCol == 4:
                    tempRes = self.findFinal(4, 5, 'T', 'F')
                    self.resultLabel3.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel3a.resize(0,0)
                elif self.nowCol == 6:
                    tempRes = self.findFinal(6, 7, 'J', 'P')
                    self.resultLabel4.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel4a.resize(0,0)

                self.nowI = 0
                self.nowCol += 1
                self.retranslateUi()

        if self.nowCol == self.maxCol:
            self.showResult()

        print(self.nowCol)
        print(self.nowI)

    def rightBtnClicked(self):
        self.result[self.index[self.nowCol]["resultB"]] += 1
        if self.nowCol < self.maxCol:
            if self.nowI < self.maxI:
                self.nowI += 1

                if self.nowCol == 0:
                    self.resultLabel1a.resize(self.nowI/self.maxI*128,128)
                elif self.nowCol == 1:
                    self.resultLabel2a.resize(self.nowI/self.maxI*64,128)
                elif self.nowCol == 2:
                    self.resultLabel2a.resize(64+self.nowI/self.maxI*64,128)
                elif self.nowCol == 3:
                    self.resultLabel3a.resize(self.nowI/self.maxI*64,128)
                elif self.nowCol == 4:
                    self.resultLabel3a.resize(64+self.nowI/self.maxI*64,128)
                elif self.nowCol == 5:
                    self.resultLabel4a.resize(self.nowI/self.maxI*64,128)
                elif self.nowCol == 6:
                    self.resultLabel4a.resize(64+self.nowI/self.maxI*64,128)

                self.retranslateUi()

            if self.nowI == self.maxI:
                tempRes = ""
                if self.nowCol == 0:
                    tempRes = self.findFinal(0, 1, 'E', 'I')
                    self.resultLabel1.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel1a.resize(0,0)
                elif self.nowCol == 2:
                    tempRes = self.findFinal(2, 3, 'S', 'N')
                    self.resultLabel2.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel2a.resize(0,0)
                elif self.nowCol == 4:
                    tempRes = self.findFinal(4, 5, 'T', 'F')
                    self.resultLabel3.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel3a.resize(0,0)
                elif self.nowCol == 6:
                    tempRes = self.findFinal(6, 7, 'J', 'P')
                    self.resultLabel4.setText(tempRes)
                    self.result[8] += tempRes
                    self.resultLabel4a.resize(0,0)

                self.nowI = 0
                self.nowCol += 1
                self.retranslateUi()

        if self.nowCol == self.maxCol:
            self.resultLabel.setText("")
            self.showResult()

        print(self.nowCol)
        print(self.nowI)

    def showResult(self):
        print(self.result[8])
        print(self.desc_result[self.result[8]][0])
        print(self.desc_result[self.result[8]][1])
        self.resultLabel.setText(self.desc_result[self.result[8]][0])
        self.resultLabelDesc.setText(self.desc_result[self.result[8]][1])
        self.leftBtn.hide()
        self.rightBtn.hide()
        self.questionLabel.hide()
        self.resultLabel.show()
        self.resultLabelDesc.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.leftBtn.setText(_translate(
            "main", self.questions[self.nowCol*10+self.nowI][2]))
        self.questionLabel.setText(_translate(
            "main", self.questions[self.nowCol*10+self.nowI][1]))
        self.rightBtn.setText(_translate(
            "main", self.questions[self.nowCol*10+self.nowI][3]))

    def findFinal(self, scoreA, scoreB, resultA, resultB):
        if self.result[scoreA] >= self.result[scoreB]:
            return resultA
        else:
            return resultB


ico = b"iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACLz2ctAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAAM9SURBVHhe7d2xbSVVGIZhQxekVLEpIT0sNVALARVAD4Sk28ImpETUAFgaCcn6ZQ2au/POnPs8kuWJrVdH99MZ2199+Panv18g8vX2HRICJCVAUgIkJUBSAiQlQFICJCVAUk93E/Lpjx+3p96/P/vt6Xk5AUkJkJQASQmQ1NIjZBocn37/c3t6jA/ffbM9/eeX73/dnt73w28ft6f3rTxWnICkBEhKgKQESGqZEbL3huNKI2QyDRMjBL4QAZISICkBkrrlCDnjhmOvR4+Qyco3Jk5AUgIkJUBSAiR1qRFS3WYcMY2QyaOHyeSOtyhOQFICJCVAUgIkdfkRMn14nz5sP9swWeV2xAlISoCkBEhKgKSyEbJ3cEz2fgC/4zB5NCME3iFAUgIkJUBStxwhk6vfjlSm8XOlYeIEJCVAUgIkJUBSAiQlQFICJCVAUgIkdcpNyBm3HhM3IbMr3Y44AUkJkJQASQmQ1OVHiMHxeEYIbARISoCkBEgqGyFHGByzI7/8boTwlARISoCkBEjq4SNkGhxGw+PtHRxHbpzOGCZOQFICJCVAUgIkJcCFvA6Ot19XJ0BSAiQlQFICJCVAUgIkJUBSAiQlQFKHXsfy6lVneh3r0TcfP3/+a3v6cpyApARISoCkBEhq6REyfVBfZSSdMULO+D0RJyApAZISICkBklpmhBz5y1B7XX1gTY4MEyOE5QmQlABJCZDULUfIkcGx90P5Hf8/yRlDzAhhKQIkJUBSAiS1zAg54y9BPds/Tpx+zkYISxEgKQGSEiApAf4Pr0Pn7RfHCJCUAEkJkJQASS0T4Ostxdsvrs8JSEqApARISoCkDr2ONVn5Fa29w+aOr2Od8erVxAlISoCkBEhKgKSWHiF7TWPF4DiHE5CUAEkJkJQAST18hExW+VO+dxwcEyMENgIkJUBSAiR1ygiZTMNkssoH/8mRQXRENTgmTkBSAiQlQFICJJWNkL2udItyxN7Bsff3WPa+LnalwTFxApISICkBkhIgqcuPkMkdb1GmEXJkcFx9XOzlBCQlQFICJCVAUrccIXvtHStXt8rgmDgBSQmQlABJCZDU0iOE63MCkhIgKQGSEiChl5d/AG2mJMp4S80KAAAAAElFTkSuQmCC"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
