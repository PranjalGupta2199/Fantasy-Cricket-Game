# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_application.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(894, 629)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 201, 24))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 141, 24))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 79, 24))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 131, 24))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 40, 51, 24))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 40, 141, 24))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 40, 41, 24))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(650, 40, 161, 24))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(830, 40, 79, 24))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(410, 310, 51, 41))
        self.commandLinkButton.setText(_fromUtf8(""))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 341, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 200, 341, 311))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 100, 151, 24))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 100, 79, 24))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(670, 100, 79, 24))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(510, 100, 151, 24))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(500, 190, 341, 311))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listWidget_2 = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(510, 150, 151, 24))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 140, 201, 36))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 32))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuManage_TEam = QtGui.QMenu(self.menubar)
        self.menuManage_TEam.setObjectName(_fromUtf8("menuManage_TEam"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtGui.QAction(MainWindow)
        self.actionNEW_Team.setObjectName(_fromUtf8("actionNEW_Team"))
        self.actionOPEN_Team = QtGui.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName(_fromUtf8("actionOPEN_Team"))
        self.actionSAVE_Team = QtGui.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName(_fromUtf8("actionSAVE_Team"))
        self.actionEVALUATE_Team = QtGui.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName(_fromUtf8("actionEVALUATE_Team"))
        self.menuManage_TEam.addSeparator()
        self.menuManage_TEam.addAction(self.actionNEW_Team)
        self.menuManage_TEam.addAction(self.actionOPEN_Team)
        self.menuManage_TEam.addAction(self.actionSAVE_Team)
        self.menuManage_TEam.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_TEam.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Your Selections", None))
        self.label_2.setText(_translate("MainWindow", "BATSMEN(BAT) :", None))
        self.label_3.setText(_translate("MainWindow", "###", None))
        self.label_4.setText(_translate("MainWindow", "Bowlers(BWL) :", None))
        self.label_5.setText(_translate("MainWindow", "###", None))
        self.label_6.setText(_translate("MainWindow", "AllRounders(AR) :", None))
        self.label_7.setText(_translate("MainWindow", "###", None))
        self.label_8.setText(_translate("MainWindow", "Wicket-Keeper(WK):", None))
        self.label_9.setText(_translate("MainWindow", "###", None))
        self.radioButton.setText(_translate("MainWindow", "BAT", None))
        self.radioButton_2.setText(_translate("MainWindow", "BWL", None))
        self.radioButton_3.setText(_translate("MainWindow", "AR", None))
        self.radioButton_4.setText(_translate("MainWindow", "WK", None))
        self.label_10.setText(_translate("MainWindow", "Points Available ", None))
        self.label_11.setText(_translate("MainWindow", "###", None))
        self.label_12.setText(_translate("MainWindow", "###", None))
        self.label_13.setText(_translate("MainWindow", "Points Used", None))
        self.label_14.setText(_translate("MainWindow", "Team Name", None))
        self.menuManage_TEam.setTitle(_translate("MainWindow", "Manage Team", None))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team", None))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team", None))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team", None))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team", None))


        self.radioButton.toggled.connect(lambda:self.display_avail_number(Avail_batsman))
        self.radioButton_2.toggled.connect(lambda:self.display_avail_number(Avail_bowler))
        self.radioButton_4.toggled.connect(lambda:self.display_avail_number(Avail_WicketKeeper))
        self.radioButton_3.toggled.connect(lambda:self.display_avail_number(Avail_Allrounder))
        self.radiocount = 0


        self.label_3.setText(str(len(Avail_batsman)))
        self.label_5.setText(str(len(Avail_bowler)))
        self.label_7.setText(str(len(Avail_Allrounder)))
        self.label_9.setText(str(len(Avail_WicketKeeper)))

        
        #self.actionNEW_Team.triggered.connect(lambda:self.create_team("abc"))
        #self.create_team("abc")
        #self.commandLinkButton.connect(self.team.add_member(self.listWidget.currentItem()))


    def display_avail_number(self,l):

        self.listWidget.clear()
        for i in range (len(l)):
            #item = QListWidgetItem(l[i])
            self.listWidget.addItem(l[i])
            self.listWidget.show()
        self.label_3.setText(str(len(Avail_batsman)))
        self.label_5.setText(str(len(Avail_bowler)))
        self.label_7.setText(str(len(Avail_Allrounder)))
        self.label_9.setText(str(len(Avail_WicketKeeper)))

    def create_team(self, text):
        global Team
        self.team = Team(text)



import sqlite3
db = sqlite3.connect("app.db")
cursor = db.cursor()


row = cursor.execute("SELECT * FROM app_data")

Available_players = []
Total_points = 1000
player_points = {}

Avail_batsman, Avail_bowler, Avail_Allrounder, Avail_WicketKeeper = [], [], [], []
player_value = {}
for row in cursor.execute("SELECT * FROM app_data"):
    Available_players.append(row[0])
    player_name,ctg = row[0],row[-1]
    if (ctg == "BAT") : Avail_batsman.append(player_name)
    elif (ctg == "BWL") : Avail_bowler.append(player_name)
    elif (ctg == "AR") : Avail_Allrounder.append(player_name)
    elif (ctg == "WK") : Avail_WicketKeeper.append(player_name)

    #player_points[player_name] = calculate_points(row)
    player_value[player_name] = row[-2]
#print(player_value)


class Team:

    def __init__(self, name):
        self.score = 1000
        self.team_name = name
        self.members = []

    def add_member(self, player):
        self.members.append(player)
        self.score -= player_value[player]
        if self.score != 0:
            self.score += player_value[player]
            print("Can't add player")


    def delete_member(self, player):
        self.current_team.remove(player)




























BAT, BWL, AR, WK = len(Avail_batsman), len(Avail_bowler), len(Avail_Allrounder), len(Avail_WicketKeeper)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
