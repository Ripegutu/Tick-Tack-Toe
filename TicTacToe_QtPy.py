from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import functions as func


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        ###Main Menu##
        mainMenu = QVBoxLayout()
        l1 = QLabel()
        l1.setText("Main Menu")
        mainMenu.addWidget(l1)
        startGame = QPushButton("Start a Game")
        mainMenu.addWidget(startGame)
        enterPlayerIds = QPushButton("Enter Player Ids")
        mainMenu.addWidget(enterPlayerIds)
        viewScore = QPushButton("View Score")
        mainMenu.addWidget(viewScore)
        exitGame = QPushButton("Exit Game")
        mainMenu.addWidget(exitGame)
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(mainMenu)

        # Signals for "Main Menu" 
        startGame.clicked.connect(self.start_game)
        enterPlayerIds.clicked.connect(self.enter_player_ids)
        viewScore.clicked.connect(self.view_score)
        exitGame.clicked.connect(self.close)

        ##File menu#
        menu = self.menuBar()
        filemenu = menu.addMenu("&File")
        about = QAction("&About")
        filemenu.addAction(about)
        about.triggered.connect(display_about)
        close = QAction("&Close")
        close.triggered.connect(self.close)
        filemenu.addAction(close)

    def start_game(self):
        print("Start game pushed!")
    
    def enter_player_ids(self):
        print("Enter player IDs pushed!")
    
    def view_score(self):
        print("View score pushed!")

    def closeEvent(self,e):
        answer = QMessageBox.question(window, None, "You are about to leave the game.",
        QMessageBox.Ok | QMessageBox.Cancel)
        if answer & QMessageBox.Ok:
            return
        elif answer & QMessageBox.Cancel:
            e.ignore()


def display_about():
    text = "<center>" \
           "<h1>Tick Tack Toe</h1>" \
           "&#8291;" \
           "</center>" \
           "<p>This is a game of tic tac toe.  <br/>" \
           "Version 1.0.0.0<br/>" \
           "Copyright &copy; Ripegutu Inc.</p>"
    QMessageBox.about(window, "About Tick Tack Toe", text)


# def view_score(player1Score, player2Score):
#     text = "<center>" \
#             "<h1>Score</h1>" \
#             "&#8291;" \
#            "</center>" \
#            "<p>Player 1 score is: <br/>" \
#            "Player 2 score is: </p>" 
#     QMessageBox.Ok(window, "Game Score", text)




if __name__ == "__main__":
    ### Initiate Score of players ###
    player1Score = 0
    player2Score = 0

    ### Setup GUI ###
    app = QApplication(sys.argv)
    app.setApplicationName("Tic Tack Toe")
    app.setStyle("Fusion")
    func.set_theme(app)
    window = MainWindow()

    ### File menu ###
    # menu = window.menuBar().addMenu("&File")
    # about = QAction("&About")
    # about.triggered.connect(display_about)
    # menu.addAction(about)
    # close = QAction("&Close")
    # close.triggered.connect(window.close)
    # menu.addAction(close)



    ### Signals (MainMenu) ###
    # viewScore.clicked.connect(lambda x: window.show_score())

    window.show()
    sys.exit(app.exec_())