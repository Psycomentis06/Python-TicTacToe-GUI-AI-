import sys

from PyQt5.QtWidgets import QWidget, QApplication
from GameConfig import GameConfig
import GameFinishWindow


class SaveData(QWidget):
    """The save data class job is to save some data in the statics ini file"""

    def __init__(self, lightMode, volume, botLevel, gameMode, winner):
        super().__init__()
        self.lightMode = lightMode
        self.volume = volume
        self.botLevel = botLevel
        self.gameMode = gameMode
        self.winner = winner
        dataSet = GameConfig()
        try:  # if the file exists he will get the values saved in it
            config = GameConfig()
            playedGames = config.readData('game_stats.ini', 'Statictics', 'played_games', 'int')
            botWins = config.readData('game_stats.ini', 'Statictics', 'bot_wins', 'int')
            playerWins = config.readData('game_stats.ini', 'Statictics', 'player', 'int')
            player1Wins = config.readData('game_stats.ini', 'Statictics', 'player1_wins', 'int')
            player2Wins = config.readData('game_stats.ini', 'Statictics', 'player2_wins', 'int')
            bot1Wins = config.readData('game_stats.ini', 'Statictics', 'bot1_wins', 'int')
            bot2Wins = config.readData('game_stats.ini', 'Statictics', 'bot2_wins', 'int')
            tieGame = config.readData('game_stats.ini', 'Statictics', 'tie', 'int')

        except:  # If the file is missing he will create it with default values
            config = GameConfig()
            config.writeStaticsData(0, 0, 0, 0, 0, 0, 0, 0)
            playedGames = config.readData('game_stats.ini', 'Statictics', 'played_games', 'int')
            botWins = config.readData('game_stats.ini', 'Statictics', 'bot_wins', 'int')
            playerWins = config.readData('game_stats.ini', 'Statictics', 'player', 'int')
            player1Wins = config.readData('game_stats.ini', 'Statictics', 'player1_wins', 'int')
            player2Wins = config.readData('game_stats.ini', 'Statictics', 'player2_wins', 'int')
            bot1Wins = config.readData('game_stats.ini', 'Statictics', 'bot1_wins', 'int')
            bot2Wins = config.readData('game_stats.ini', 'Statictics', 'bot2_wins', 'int')
            tieGame = config.readData('game_stats.ini', 'Statictics', 'tie', 'int')
        playedGames += 1
        dataSet.setData('game_stats.ini', 'Statictics', 'played_games', str(playedGames))
        if self.winner == 'player1':
            player1Wins += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'player1_wins', str(player1Wins))
        elif self.winner == 'player2':
            player2Wins += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'player2_wins', str(player2Wins))
        elif self.winner == 'bot':
            botWins += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'bot_wins', str(botWins))
        elif self.winner == 'bot1':
            bot1Wins += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'bot1_wins', str(bot1Wins))
        elif self.winner == 'bot2':
            bot2Wins += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'bot2_wins', str(bot2Wins))
        elif self.winner == 'player':
            playerWins += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'player', str(playerWins))
        elif self.winner == 'tie':
            tieGame += 1
            dataSet.setData('game_stats.ini', 'Statictics', 'tie', str(tieGame))

        self.finishUi = GameFinishWindow.FinishWindow(self.lightMode, self.volume, self.botLevel, self.gameMode, self.winner)
        self.finishUi.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    boot = SaveData()
    sys.exit(app.exec_())
