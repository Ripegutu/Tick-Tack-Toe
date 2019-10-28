from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
import functions as func
import random
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("Main Menu")

        self.gameParameters()
        self.initUI()
        
    def gameParameters(self):
        self.player1_score = 0
        self.player2_score = 0

        self.player1_name = "Player 1"
        self.player2_name = "Player 2"

        self.squares_to_win = 3

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
        QMessageBox.about(self, "About Tick Tack Toe", text)

class DisplayScores(QDialog):
    def __init__(self, parent):
        super(DisplayScores,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowTitle("Score View")
        
        QBtn = QDialogButtonBox.Ok

        self.score_label = QLabel()
        score_text = f"The score is currently:\n {parent.player1_name}: {parent.player1_score}\n {parent.player2_name}: {parent.player2_score}"
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
        self.player1.setPlaceholderText(parent.player1_name)
        self.player2.setPlaceholderText(parent.player2_name)

        self.layout = QFormLayout()
        self.layout.addRow(self.ID_label)
        self.layout.addRow(self.player1_label, self.player1)
        self.layout.addRow(self.player2_label, self.player2)
        self.layout.addRow(self.ok_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(lambda x: self.okPressed(parent))

    def okPressed(self, parent):
        if self.player1.text() != "":
            parent.player1_name = self.player1.text()
        if self.player2.text() != "":
            parent.player2_name = self.player2.text()
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
        self.h1layout.addWidget(self.horizontal_size)
        self.h1layout.addWidget(QLabel("x"))
        self.h1layout.addWidget(self.vertical_size)

        self.spacing = QLabel(" ")
            
        self.square_description = QLabel("Number of Squares: [Horizontal, Vertical]")
        
        self.h2layout = QHBoxLayout()
        self.horizontal_squares = QLineEdit()
        self.vertical_squares = QLineEdit()
        self.horizontal_squares.setPlaceholderText(str(parent.number_of_squares[0]))
        self.vertical_squares.setPlaceholderText(str(parent.number_of_squares[1]))
        self.h2layout.addWidget(self.horizontal_squares)
        self.h2layout.addWidget(QLabel("x"))
        self.h2layout.addWidget(self.vertical_squares)
        
        self.win_label = QLabel("No of squares to win:",self)
        self.win_line_edit = QLineEdit()
        self.win_line_edit.setPlaceholderText(str(parent.squares_to_win))


        self.ok_button = QPushButton("OK", self)

        self.layout = QFormLayout()
        self.layout.addRow(self.size_description)
        self.layout.addRow(self.h1layout)
        self.layout.addRow(self.spacing)
        self.layout.addRow(self.square_description)
        self.layout.addRow(self.h2layout)
        self.layout.addRow(self.spacing)
        self.layout.addRow(self.win_label, self.win_line_edit)
        self.layout.addRow(self.ok_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(lambda x:self.okPressed(parent))

    def okPressed(self,parent):
        if self.horizontal_size.text() != "":
            try:
                parent.game_window_size[0] = int(self.horizontal_size.text())
            except:
                pass
        
        if self.vertical_size.text() != "":
            try:
                parent.game_window_size[1] = int(self.vertical_size.text())
            except:
                pass
        
        if self.horizontal_squares.text() != "":
            try:
                parent.number_of_squares[0] = int(self.horizontal_squares.text())
            except:
                pass
        
        if self.vertical_squares.text() != "":
            try:
                parent.number_of_squares[1] = int(self.vertical_squares.text())
            except:
                pass
        if self.win_line_edit.text != "":
            try:
                parent.squares_to_win = int(self.win_line_edit.text())
            except:
                pass
        self.accept()

class StartGame(QMainWindow):
    def __init__(self,parent):
        super(StartGame,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setMinimumSize(QSize(parent.game_window_size[0]+1, parent.game_window_size[1] + 30))
        self.setWindowTitle("Tic Tac Toe")
        self.squares_to_win = parent.squares_to_win
        self.game_winner = None
        self.player1_score, self.player2_score = parent.player1_score, parent.player2_score
        self.parent = parent
        
        self.boardAndGameData(parent)
        self.initUI()

    def boardAndGameData(self, parent):
        self.horizontal_lines = parent.number_of_squares[1]
        self.horizontal_size = parent.game_window_size[0]
        self.vertical_lines = parent.number_of_squares[0]
        self.vertical_size = parent.game_window_size[1]
        self.board_size = [["" for x in range(self.vertical_lines)] for y in range(self.horizontal_lines)]
        self.no_of_squares = len(self.board_size) * len(self.board_size[0])
        self.player1 = parent.player1_name
        self.player2 = parent.player2_name
        self.active_player = random.choice([parent.player1_name, parent.player2_name])

    def initUI(self):
        self.start_label = self.active_player + " will start the game, Good Luck!"
        self.next_move = QLabel(self.start_label, self)
        self.next_move.setFixedSize(400,30)
        self.next_move.move(10,self.vertical_size)
        self.game_label = QLabel("", self)

        self.show()

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        self.makeBoard(qp)
        self.paintXO(qp)

        qp.end()
    
    def makeBoard(self, qp):
        pen = QPen(Qt.gray, 1, Qt.SolidLine)
        qp.setPen(pen)

        self.horizontal_space = (self.frameGeometry().width()-3)/self.vertical_lines
        self.vertical_space = (self.frameGeometry().height()-69)/self.horizontal_lines
        self.next_move.move(10,self.frameGeometry().height()-69)
        # Horizontal lines
        for i in range(self.horizontal_lines + 1):
            qp.drawLine(0, i * self.vertical_space, self.frameGeometry().width(), i * self.vertical_space)
        # Vertical lines
        for i in range(self.vertical_lines + 1):
            qp.drawLine(i * self.horizontal_space, 0, i * self.horizontal_space, self.frameGeometry().height() - 69)

    def mousePressEvent(self, QMouseEvent):
        self.click = [QMouseEvent.x(), QMouseEvent.y()]

        if 0 < self.click[0] < self.frameGeometry().width() and 0 < self.click[1] < (self.frameGeometry().height()-69): 
            
            for hor_line in range(self.horizontal_lines):
                for ver_line in range(self.vertical_lines):
                    self.xmin = ver_line * self.horizontal_space
                    self.xmax = (ver_line + 1) * self.horizontal_space
                    self.ymin = hor_line * self.vertical_space
                    self.ymax = (1 + hor_line) * self.vertical_space
                    if self.xmin < self.click[0] < self.xmax and self.ymin < self.click[1] < self.ymax:
                        if self.board_size[hor_line][ver_line] == "":
                            if self.active_player == self.player1:
                                self.board_size[hor_line][ver_line] = "X"
                            else: 
                                self.board_size[hor_line][ver_line] = "O"

                            if self.active_player == self.player1:
                                self.active_player = self.player2
                            else:
                                self.active_player = self.player1

                            self.label = self.active_player + " to move!"
                            self.next_move.setText(self.label)
                            self.repaint()

                            self.winnerLines()
                            self.decideWinner()
                            
                        else: 
                            self.next_move.setText(self.label + " But try a different square!")

    def winnerLines(self):
        xy = np.asarray(self.board_size)
        diags = ([xy[::-1,:].diagonal(i) for i in range(-xy.shape[0]+1, xy.shape[1])])
        diags.extend(xy.diagonal(i) for i in range(xy.shape[1]-1,-xy.shape[0],-1))
        self.diagonal_winner_list = [n.tolist() for n in diags  if len(n.tolist()) >= self.squares_to_win]
        self.horizontal_winner_list = [x for x in self.board_size]
        self.vertical_winner_list = [x.tolist() for x in xy.T]
        self.winner_list = [x for x in self.horizontal_winner_list + self.vertical_winner_list + self.diagonal_winner_list]

    def decideWinner(self):
        
        prev_square = None
        winner_count = 0
        draw_count = 0
        for col in self.winner_list:
            for i, square in enumerate(col):
                

                if i == 0:
                    winner_count = 1
                    prev_square = square
                else:
                    if prev_square == square and square != "":
                        winner_count += 1
                    else: 
                        winner_count = 1
                        prev_square = square
                
                if winner_count == self.squares_to_win:
                    if square == "X":
                        self.winner_text = f"{self.player1} is the winner!"
                        self.game_winner = self.player1
                    else:
                        self.winner_text = f"{self.player2} is the winner!"
                        self.game_winner = self.player2

                    self.close()
                    
            winner_count = 0
        for col in self.board_size:
            for square in col:
                if square != "":
                    draw_count += 1

        if draw_count == self.no_of_squares and self.game_winner == None:
            self.winner_text = "The Game ends with a draw!"
            self.game_winner = "No"
            self.close()

    def paintXO(self, qp):
        pen = QPen(Qt.gray, 2, Qt.SolidLine)
        qp.setPen(pen)
        for col_no, col in enumerate(self.board_size):
            for row_no, square in enumerate(col):
                if square == "X":
                    qp.drawLine(self.horizontal_space * row_no, self.vertical_space * col_no, self.horizontal_space * (row_no + 1), self.vertical_space * (col_no + 1))
                    qp.drawLine(self.horizontal_space * (row_no + 1), self.vertical_space * col_no, self.horizontal_space * row_no, self.vertical_space * (col_no+ 1))
        
                elif square == "O":
                    qp.drawEllipse(self.horizontal_space * row_no, self.vertical_space * col_no, self.horizontal_space, self.vertical_space)

    def closeEvent(self,e):
        if self.game_winner == None:
            answer = QMessageBox.question(self, None, "You are about to exit\nThe current game will be lost.",
            QMessageBox.Ok | QMessageBox.Cancel)
            if answer & QMessageBox.Ok:
                return
            elif answer & QMessageBox.Cancel:
                e.ignore()
        else:
            answer = QMessageBox.question(self, None, f"{self.winner_text}\nDo you want to play a new game?",
            QMessageBox.Ok | QMessageBox.Discard)

            if self.game_winner == self.player1:
                self.parent.player1_score = self.parent.player1_score + 1
            elif self.game_winner == self.player2:
                self.parent.player2_score = self.parent.player2_score + 1

            if answer & QMessageBox.Ok:
                self.board_size = [["" for x in range(self.vertical_lines)] for y in range(self.horizontal_lines)]
                self.game_winner = None
                e.ignore()
                self.repaint()
            elif answer & QMessageBox.Discard:
                return

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    func.set_theme(app)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
