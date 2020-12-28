import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QWidget, QMainWindow, QApplication, QDesktopWidget, QLabel, QVBoxLayout, \
    QHBoxLayout
from PyQt5 import QtCore, QtMultimedia
import GameInterface
import CPUVSPlayer
import StatsWindow


class FinishWindow(QMainWindow):

    def __init__(self, lightMode, volume, botLevel, gameMode, winner):
        """Constructor"""

        super().__init__()
        self.lightMode = lightMode
        self.volume = volume
        self.botLevel = botLevel
        self.gameMode = gameMode
        self.winner = winner
        print('************Finish Window**************')
        print('Game Mode: ', self.gameMode)
        print('Volume: ', self.volume)
        print('Light mode: ', self.lightMode)
        print('Bot level: ', self.botLevel)
        print('Bot level: ', self.winner)
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setGeometry(600, 600, 600, 600)
        QFontDatabase.addApplicationFont('assets/fonts/HALO____.ttf')
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setWindowTitle('Tic Tac Toe ')
        self.setStyleSheet("background-color:rgb(22, 22, 22);"
                           "color: white")
        self.menuWidget = QWidget()
        # self.menuWindow()
        self.VLayout = QVBoxLayout(self.menuWidget)
        self.VLayout.addSpacing(100)
        self.celebTextLayout = QHBoxLayout(self.menuWidget)
        self.celebTextLabel = QLabel('', self)
        self.celebTextLabel.setWordWrap(True)
        self.celebTextLabel.setStyleSheet("color: #fd9644;"
                                          "font-family: halo;"
                                          "font-size: 18pt;")
        self.celebTextLayout.addWidget(self.celebTextLabel)
        self.celebTextLayout.setAlignment(Qt.AlignCenter)
        self.VLayout.addLayout(self.celebTextLayout)
        self.menuWidget.setLayout(self.VLayout)
        self.setMenuWidget(self.menuWidget)
        self.createButtons('Replay', 220, 100, 180, 180, self.replay)
        self.createButtons('Statistics', 220, 100, 180, 280, self.statistics)
        self.createButtons('Exit', 220, 100, 180, 380, exit)

        self.celebration()
        self.center()
        self.show()

    def center(self):
        """align window center"""

        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def menuWindow(self):
        menuLayout = QVBoxLayout(self.menuWidget)
        menuLabel = QLabel(self)
        menuLabel.resize(680, 680)
        menuLabel.setAlignment(Qt.AlignCenter)
        menuLayout.addWidget(menuLabel)
        menuLabel.setStyleSheet("background-color:rgb(55,55,55)")

    def replay(self):
        if self.gameMode == 'Player VS Player':
            self.GameInter = GameInterface.GameInterface(self.lightMode, self.volume, self.botLevel, self.gameMode)
            self.GameInter.show()
            self.close()
        elif self.gameMode == 'Player VS Bot' or self.gameMode == 'Bot VS Bot':
            self.CPU = CPUVSPlayer.CPUVSPlayer(self.lightMode, self.volume, self.botLevel, self.gameMode)
            self.CPU.show()
            self.close()

    def statistics(self):
        print("Statistics")
        self.statsUi = StatsWindow.StatsWindow(self.lightMode)
        self.statsUi.show()

    def createButtons(self, title, resizeW, resizeH, moveX, moveY, functionName):
        button = QPushButton(title, self)
        button.clicked.connect(functionName)
        button.resize(resizeW, resizeH)
        button.move(moveX, moveY)
        button.setStyleSheet("background-color: none;"
                             "border-style: outset;"
                             "font: bold 14px;"
                             "cursor: pointer;"
                             "font-size:24pt;"
                             "color: rgb(0, 178, 62);"
                             "font-family: ubuntu mono")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def celebrationVoicePlayer(self, filePath):
        """Method for playing the celebration voice"""
        self.fullpath = QtCore.QDir.current().absoluteFilePath(filePath)
        self.media = QtCore.QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.setVolume(80)
        self.player.play()

    def randomSelect(self, liste):
        """Return a random index from a list based on length it will be used in the computerMove method"""
        listLength = len(liste)
        randomValue = random.randrange(0, listLength)
        return randomValue

    def celebration(self):
        #  **************************************celeb lists**************************
        #  player1 win
        player1WinText = 'Player N°1 won the game'
        player1WinVoice = 'assets/Celebration Voices/player1.wav'

        #  player2 win
        player2WinText = 'Player N°2 won the game'
        player2WinVoice = 'assets/Celebration Voices/player2.wav'

        #  bot win VS player (stupid level)
        stupidBotWinText = ['Noob', 'Looser even in stupid level', 'Please uninstall']
        stupidBotWinVoice = ['assets/Celebration Voices/noob.wav', 'assets/Celebration Voices/looser.wav',
                             'assets/Celebration Voices/unin.wav']

        #  bot win VS player (medium level)
        mediumBotWinText = ['GG easy game easy life', 'Easy peasy leamon squeezy', 'Easy game easy life']
        mediumBotWinVoice = ['assets/Celebration Voices/gg.wav', 'assets/Celebration Voices/easy.wav',
                             'assets/Celebration Voices/life.wav']

        #  bot win VS player (hard level)
        hardBotWinText = ['Never loose versus noobs like you', 'Like every time im tilted from noobs']
        hardBotWinVoice = ['assets/Celebration Voices/never.wav', 'assets/Celebration Voices/tilted.wav']

        #  bot win VS player (hard level)
        playerBeatBotText = ['Congrats you beated me', 'Nice one', 'GG well played']
        playerBeatBotVoice = ['assets/Celebration Voices/congrats.wav', 'assets/Celebration Voices/nice.wav',
                              'assets/Celebration Voices/wp.wav']

        # bot 1 win
        bot1WinText = 'Bot N°1 won'
        bot1WinVoice = 'assets/Celebration Voices/bot1.wav'

        # bot 2 win
        bot2WinText = 'Bot N°2 won'
        bot2WinVoice = 'assets/Celebration Voices/bot2.wav'

        # Tie
        tieGame = 'Tie Game'

        if self.winner == 'player':
            index = self.randomSelect(playerBeatBotText)
            print(index)
            self.celebTextLabel.setText('" ' + playerBeatBotText[index] + ' "! ')
            self.celebrationVoicePlayer(playerBeatBotVoice[index])
        elif self.winner == 'bot' and self.botLevel == 3:
            index = self.randomSelect(stupidBotWinText)
            print(index)
            self.celebTextLabel.setText('" ' + stupidBotWinText[index] + ' "! ')
            self.celebrationVoicePlayer(stupidBotWinVoice[index])
        elif self.winner == 'bot' and self.botLevel == 2:
            index = self.randomSelect(mediumBotWinText)
            print(index)
            self.celebTextLabel.setText('" ' + mediumBotWinText[index] + ' "! ')
            self.celebrationVoicePlayer(mediumBotWinVoice[index])
        elif self.winner == 'bot' and self.botLevel == 1:
            index = self.randomSelect(hardBotWinText)
            print(index)
            self.celebTextLabel.setText('" ' + hardBotWinText[index] + ' "! ')
            self.celebrationVoicePlayer(hardBotWinVoice[index])
        elif self.winner == 'bot1':
            self.celebTextLabel.setText('" ' + bot1WinText + ' "! ')
            self.celebrationVoicePlayer(bot1WinVoice)
        elif self.winner == 'bot2':
            self.celebTextLabel.setText('" ' + bot2WinText + ' "! ')
            self.celebrationVoicePlayer(bot2WinVoice)
        elif self.winner == 'tie':
            self.celebTextLabel.setText('" ' + tieGame + ' "! ')
        elif self.winner == 'player1':
            self.celebTextLabel.setText('" ' + player1WinText + ' "! ')
            self.celebrationVoicePlayer(player1WinVoice)
        elif self.winner == 'player2':
            self.celebTextLabel.setText('" ' + player2WinText + ' "! ')
            self.celebrationVoicePlayer(player2WinVoice)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MenuUi = FinishWindow()
    MenuUi.show()
    sys.exit(app.exec_())
