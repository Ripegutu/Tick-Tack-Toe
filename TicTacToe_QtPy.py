from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
import functions as func
import random

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

        self.game_window_size = [600, 600]

    def initUI(self):
        ###Main Menu##
        main_menu = QVBoxLayout()
        start_game = QPushButton("Start a Game")
        main_menu.addWidget(start_game)
        enter_player_ids = QPushButton("Enter Player Ids")
        main_menu.addWidget(enter_player_ids)
        change_board_parameters = QPushButton("Board Parameters")
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
    def __init__(self, parent):
        super(ChangeGameParameters, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowTitle("Change Game Parameters")

        self.size_description = QLabel("Board Size: [Horizontal, Vertical]")

        self.h1layout =QHBoxLayout()
        self.horizontal_size = QLineEdit()
        self.vertical_size = QLineEdit()
        self.horizontal_size.setPlaceholderText(str(parent.game_window_size[0]))
        self.vertical_size.setPlaceholderText(str(parent.game_window_size[1]))
        self.x_label = QLabel("x")
        self.h1layout.addWidget(self.horizontal_size)
        self.h1layout.addWidget(self.x_label)
        self.h1layout.addWidget(self.vertical_size)

        self.spacing = QLabel(" ")
            
        self.square_description = QLabel("Number of Squares: [Horizontal, Vertical]")
        
        self.h2layout = QHBoxLayout()
        self.horizontal_squares = QLineEdit()
        self.vertical_squares = QLineEdit()
        self.horizontal_squares.setPlaceholderText(str(parent.number_of_squares[0]))
        self.vertical_squares.setPlaceholderText(str(parent.number_of_squares[1]))
        self.h2layout.addWidget(self.horizontal_squares)
        self.h2layout.addWidget(self.x_label)
        self.h2layout.addWidget(self.vertical_squares)
        

        self.ok_button = QPushButton("OK", self)

        self.layout = QFormLayout()
        self.layout.addRow(self.size_description)
        self.layout.addRow(self.h1layout)
        self.layout.addRow(self.spacing)
        self.layout.addRow(self.square_description)
        self.layout.addRow(self.h2layout)
        self.layout.addRow(self.ok_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(lambda x:self.okPressed(parent))

    def okPressed(self,parent):
        if self.horizontal_size.text() != "":
            parent.game_window_size[0] = int(self.horizontal_size.text())
        
        if self.vertical_size.text() != "":
            parent.game_window_size[1] = int(self.vertical_size.text())
        
        if self.horizontal_squares.text() != "":
            parent.number_of_squares[0] = int(self.horizontal_squares.text())
        
        if self.vertical_squares.text() != "":
            parent.number_of_squares[1] = int(self.vertical_squares.text())
        self.accept()

class StartGame(QMainWindow):
    def __init__(self,parent):
        super(StartGame,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setMinimumSize(QSize(parent.game_window_size[0]+1, parent.game_window_size[1] + 30))
        self.setWindowTitle("Tic Tac Toe")
        
        self.boardAndGameData(parent)
        self.initUI()

    def boardAndGameData(self, parent):
        self.horizontal_lines = parent.number_of_squares[0]
        self.horizontal_size = parent.game_window_size[0]
        self.horizontal_space = self.horizontal_size/self.horizontal_lines
        self.vertical_lines = parent.number_of_squares[1]
        self.vertical_size = parent.game_window_size[1]
        self.vertical_space = self.vertical_size/self.vertical_lines
        
        self.player1 = parent.player1Name
        self.player2 = parent.player2Name
        self.active_player = random.choice([parent.player1Name, parent.player2Name])
        
    def initUI(self):
        self.start_label = self.active_player + " will start the game, Good Luck!"
        self.next_move = QLabel(self.start_label, self)
        self.next_move.move(10,self.vertical_size)

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
        for i in range(self.horizontal_lines + 1):
            qp.drawLine(0, i * self.horizontal_space, self.horizontal_size, i * self.horizontal_space)

        # Vertical
        for i in range(self.vertical_lines + 1):
            qp.drawLine(i * self.vertical_space, 0, i * self.vertical_space, self.vertical_size)

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
        self.label = self.active_player + " to move!"
        self.next_move.setText(self.label)

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
