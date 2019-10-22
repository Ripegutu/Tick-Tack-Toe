from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
import functions as func


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("Main Menu")

        self.gameParameters()
        self.initUI()
        
    def gameParameters(self):
        self.player1Score = 0
        self.player2Score = 0

        self.player1Name = "Player 1"
        self.player2Name = "Player 2"

        # [Horizontal, Vertical]
        self.number_of_squares = [3, 3]

        self.game_window_size = [300, 300]

    def initUI(self):
        ###Main Menu##
        main_menu = QVBoxLayout()
        start_game = QPushButton("Start a Game")
        main_menu.addWidget(start_game)
        enter_player_ids = QPushButton("Enter Player Ids")
        main_menu.addWidget(enter_player_ids)
        change_board_parameters = QPushButton("Change Board Parameters")
        main_menu.addWidget(change_board_parameters)
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
        change_board_parameters.clicked.connect(self.changeGameParameters)
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
        self.startGame_window = StartGame(self)
    
    def enterPlayerIds(self):
        enterPlayerIds_dlg = EnterPlayerIds(self)
        enterPlayerIds_dlg.exec_()

    def changeGameParameters(self):
        changeGameParameters_dlg = ChangeGameParameters(self)
        changeGameParameters_dlg.exec_()

    def viewScore(self, s):
        viewScore_dlg = DisplayScores(self)
        viewScore_dlg.exec_()

    def closeEvent(self,e):
        answer = QMessageBox.question(self, None, "You are about to leave the game.",
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
        score_text = f"The score is currently:\n {parent.player1Name}: {parent.player1Score}\n {parent.player2Name}: {parent.player2Score}"
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

        self.ok_button = QPushButton("OK", self)

        self.ID_label = QLabel()
        ID_text = "Enter player IDs"
        self.ID_label.setText(ID_text)

        self.player1_label = QLabel()
        self.player1_label.setText("Player 1:")
        self.player2_label = QLabel()
        self.player2_label.setText("Player 2:")

        self.player1 = QLineEdit()
        self.player2 = QLineEdit()  
        self.player1.setPlaceholderText(parent.player1Name)
        self.player2.setPlaceholderText(parent.player2Name)

        self.layout = QFormLayout()
        self.layout.addRow(self.ID_label)
        self.layout.addRow(self.player1_label, self.player1)
        self.layout.addRow(self.player2_label, self.player2)
        self.layout.addRow(self.ok_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(lambda x: self.okPressed(parent))

    def okPressed(self, parent):
        if self.player1.text() != "":
            parent.player1Name = self.player1.text()
        if self.player2.text() != "":
            parent.player2Name = self.player2.text()
        print("Ids successfully changes!")
        self.accept()

class ChangeGameParameters(QDialog):
    def __init(self, parent):
        super(ChangeGameParameters, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Change Game Parameters")

class StartGame(QMainWindow):
    def __init__(self,parent):
        super(StartGame,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setMinimumSize(QSize(300+1, 300 + 30))
        self.setWindowTitle("Tic Tac Toe")
        
        self.initUI()
    
    def initUI(self):
        self.next_move = QLabel("Player x to move", self)
        self.next_move.move(10,300)

        self.show()

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        self.makeBoard(qp)
        qp.end()
    
    def makeBoard(self,qp):
        pen = QPen(Qt.gray, 1, Qt.SolidLine)

        qp.setPen(pen)
        # Horizontal
        qp.drawLine(0, 0, 300, 0)
        qp.drawLine(0, 100, 300, 100)
        qp.drawLine(0, 200, 300, 200)
        qp.drawLine(0, 300, 300, 300)
        # Vertical
        qp.drawLine(0, 0, 0, 300)
        qp.drawLine(100, 0, 100, 300)
        qp.drawLine(200, 0, 200, 300)
        qp.drawLine(300, 0, 300, 300)

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())

    def closeEvent(self,e):
        answer = QMessageBox.question(self, None, "You are about to exit\nThe current game will be lost.",
        QMessageBox.Ok | QMessageBox.Cancel)
        if answer & QMessageBox.Ok:
            return
        elif answer & QMessageBox.Cancel:
            e.ignore()

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    func.set_theme(app)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()