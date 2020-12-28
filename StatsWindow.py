import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon
import GameConfig


class StatsWindow(QWidget):

    def __init__(self, lightMode):
        super().__init__()
        self.setWindowTitle('Statistics')
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setGeometry(600, 600, 600, 600)
        self.lightMode = lightMode
        self.backgroundChange()

        self.VLayout = QVBoxLayout()
        self.VLayout.addSpacing(20)

        self.HTextLayout = QHBoxLayout()
        title = QLabel('Statistics')
        title.setStyleSheet("color: #fed330;"
                            "font-style: bold;"
                            "font-size: 20pt")
        self.HTextLayout.addWidget(title)
        self.HTextLayout.setAlignment(Qt.AlignHCenter)
        self.VLayout.addLayout(self.HTextLayout)

        self.HLayout1 = QHBoxLayout()
        self.HLayout1.addSpacing(50)

        self.HLayout2 = QHBoxLayout()
        self.HLayout2.addSpacing(50)

        self.HLayout3 = QHBoxLayout()
        self.HLayout3.addSpacing(50)

        self.HLayout4 = QHBoxLayout()
        self.HLayout4.addSpacing(50)

        self.HLayout5 = QHBoxLayout()
        self.HLayout5.addSpacing(50)

        self.HLayout6 = QHBoxLayout()
        self.HLayout6.addSpacing(50)

        self.HLayout7 = QHBoxLayout()
        self.HLayout7.addSpacing(50)

        self.HLayout8 = QHBoxLayout()
        self.HLayout8.addSpacing(50)

        self.displayData()
        self.center()
        self.show()

    def backgroundChange(self):
        """Change the background color of the game"""
        if self.lightMode:
            self.setStyleSheet("background-color:rgb(22, 22, 22);"
                               "color: #eb3b5a;"
                               "font-size: 15pt")
        else:
            self.setStyleSheet("background-color:white;"
                               "color: #eb3b5a;"
                               "font-size: 15pt")

    def center(self):
        """align window center"""
        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def displayData(self):
        """Display data in the statistics window"""
        # get data from stats.ini file with string format
        config = GameConfig.GameConfig()
        played = config.readData('game_stats.ini', 'Statictics', 'played_games', 'str')
        bot = config.readData('game_stats.ini', 'Statictics', 'bot_wins', 'str')
        player = config.readData('game_stats.ini', 'Statictics', 'player', 'str')
        player1 = config.readData('game_stats.ini', 'Statictics', 'player1_wins', 'str')
        player2 = config.readData('game_stats.ini', 'Statictics', 'player2_wins', 'str')
        bot1 = config.readData('game_stats.ini', 'Statictics', 'bot1_wins', 'str')
        bot2 = config.readData('game_stats.ini', 'Statictics', 'bot2_wins', 'str')
        tie = config.readData('game_stats.ini', 'Statictics', 'tie', 'str')
        #  QLabel texts

        playedGames = QLabel('Played Games:')
        playedGamesNumber = QLabel(played)
        botWins = QLabel('Bot Wins:')
        botWinsNumber = QLabel(bot)
        playerWins = QLabel('Player Wins:')
        playerNumber = QLabel(player)
        player1Wins = QLabel('Player 1 Wins:')
        player1WinsNumber = QLabel(player1)
        player2Wins = QLabel('Player 2 Wins:')
        player2WinsNumber = QLabel(player2)
        bot1Wins = QLabel('Bot 1 Wins:')
        bot1WinsNumber = QLabel(bot1)
        bot2Wins = QLabel('Bot 2 Wins:')
        bot2WinsNumber = QLabel(bot2)
        tieGames = QLabel('Tie Games:')
        tieGamesNumber = QLabel(tie)

        #  add texts to layout

        self.HLayout1.addWidget(playedGames)
        self.HLayout1.addWidget(playedGamesNumber)

        self.VLayout.addLayout(self.HLayout1)

        self.HLayout2.addWidget(botWins)
        self.HLayout2.addWidget(botWinsNumber)

        self.VLayout.addLayout(self.HLayout2)

        self.HLayout3.addWidget(playerWins)
        self.HLayout3.addWidget(playerNumber)

        self.VLayout.addLayout(self.HLayout3)

        self.HLayout4.addWidget(player1Wins)
        self.HLayout4.addWidget(player1WinsNumber)

        self.VLayout.addLayout(self.HLayout4)

        self.HLayout5.addWidget(player2Wins)
        self.HLayout5.addWidget(player2WinsNumber)

        self.VLayout.addLayout(self.HLayout5)

        self.HLayout6.addWidget(bot1Wins)
        self.HLayout6.addWidget(bot1WinsNumber)

        self.VLayout.addLayout(self.HLayout6)

        self.HLayout7.addWidget(bot2Wins)
        self.HLayout7.addWidget(bot2WinsNumber)

        self.VLayout.addLayout(self.HLayout7)

        self.HLayout8.addWidget(tieGames)
        self.HLayout8.addWidget(tieGamesNumber)

        self.VLayout.addLayout(self.HLayout8)

        self.setLayout(self.VLayout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StatsWindow()
    sys.exit(app.exec_())
