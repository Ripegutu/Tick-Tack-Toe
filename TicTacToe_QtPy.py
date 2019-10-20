from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
import functions as func


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Tic Tack Toe")

        self.gameParameters()
        self.initUI()
        
    def gameParameters(self):
        self.player1Score = 0
        self.player2Score = 0
        self.player1Name = "Player 1"
        self.player2Name = "Player 2"
        print("Setting scores to zero!")

    def initUI(self):
        ###Main Menu##
        main_menu = QVBoxLayout()
        l1 = QLabel()
        l1.setText("Main Menu")
        main_menu.addWidget(l1)
        start_game = QPushButton("Start a Game")
        main_menu.addWidget(start_game)
        enter_player_ids = QPushButton("Enter Player Ids")
        main_menu.addWidget(enter_player_ids)
        view_score = QPushButton("View Score")
        main_menu.addWidget(view_score)
        exit_game = QPushButton("Exit Game")
        main_menu.addWidget(exit_game)
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(main_menu)

        # Signals for "Main Menu" 
        start_game.clicked.connect(self.startGame)
        enter_player_ids.clicked.connect(self.enterPlayerIds)
        view_score.clicked.connect(self.viewScore)
        exit_game.clicked.connect(self.close)

        ##File menu#
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        about = QAction("&About", self)
        file_menu.addAction(about)
        about.triggered.connect(self.displayAbout)
        close = QAction("&Close", self)
        close.triggered.connect(self.close)
        file_menu.addAction(close)

        self.show()

    def startGame(self):
        print("Start game pushed!")
    
    def enterPlayerIds(self):
        enterPLayerIds_dlg = EnterPlayerIds(self)
        enterPLayerIds_dlg.exec_()

    def viewScore(self, s):
        viewScore_dlg = DisplayScores(self)
        viewScore_dlg.exec_()

    def closeEvent(self,e):
        answer = QMessageBox.question(window, None, "You are about to leave the game.",
        QMessageBox.Ok | QMessageBox.Cancel)
        if answer & QMessageBox.Ok:
            return
        elif answer & QMessageBox.Cancel:
            e.ignore()

    def displayAbout(self):
        text = "<center>" \
            "<h1>Tick Tack Toe</h1>" \
            "&#8291;" \
            "</center>" \
            "<p>This is a game of tic tac toe.  <br/>" \
            "Version 1.0.0.0<br/>" \
            "Copyright &copy; Ripegutu Inc.</p>"
        QMessageBox.about(window, "About Tick Tack Toe", text)


class DisplayScores(QDialog):
    def __init__(self, parent):
        super(DisplayScores,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowTitle("Score View")
        
        QBtn = QDialogButtonBox.Ok

        self.score_label = QLabel()
        score_text = "The score is currently:\n Player 1: " + str(parent.player1Score) +"\n Player 2: " + str(parent.player2Score)
        self.score_label.setText(score_text)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class EnterPlayerIds(QDialog):
    def __init__(self, parent):
        super(EnterPlayerIds,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowTitle("Enter player IDs")
        
        QBtn = QDialogButtonBox.Ok

        self.ID_label = QLabel()
        ID_text = "Enter the name for the respective players:"
        self.ID_label.setText(ID_text)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ID_label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    ### Setup GUI ###
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    func.set_theme(app)
    window = MainWindow()
    sys.exit(app.exec_())
