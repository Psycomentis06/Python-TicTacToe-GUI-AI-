from configparser import ConfigParser


class GameConfig:
    def __init__(self):
        pass

    def writeValuesData(self, darkMode, botLevel, soundVolume):
        """Write game values data into .ini file """
        config = ConfigParser()
        config['Game values'] = {
            'Dark_mode': darkMode,
            'Bot_level': botLevel,
            'Sound_volume': soundVolume,
        }

        with open('game_config.ini', 'w') as output_file:
            config.write(output_file)

    def writeStaticsData(self, gamesPlayed, botWins, playerWins, player1Wins, player2Wins, bot1Wins, bot2Wins, tieGames):
        config = ConfigParser()
        config['Statictics'] = {
            'Played_games': gamesPlayed,
            'Bot_wins': botWins,
            'Player': playerWins,
            'Player1_wins': player1Wins,
            'Player2_wins': player2Wins,
            'Bot1_wins': bot1Wins,
            'Bot2_wins': bot2Wins,
            'Tie': tieGames
        }

        print(config)
        with open('game_stats.ini', 'w') as output_file:
            config.write(output_file)

    def setData(self, fileName, sectionName, dataKey, dataValue):
        config = ConfigParser()
        config.read(fileName)
        dataVarible = config[sectionName]
        dataVarible[dataKey] = dataValue
        with open(fileName, 'w') as output_file:
            config.write(output_file)

    def readData(self, filepath, sectionName, dataKey, dataType):
        config = ConfigParser()
        config.read(filepath)

        if dataType == 'int':
            return config[sectionName].getint(dataKey)
        elif dataType == 'float':
            return config[sectionName].getfloat(dataKey)
        elif dataType == 'bool':
            return config[sectionName].getboolean(dataKey)
        else:
            return config[sectionName].get(dataKey)

# a = GameConfig()
# b = a.readData('game_config.ini', 'Game values', 'dark_mode', 'bool')
# print(b)
# a.writeValuesData(True, 1, 80, 'PlayerVSPlayer')
# a.writeStaticsData(92, 15, 50, 20)
# a.setData('game_stats.ini', 'Statictics', 'Bot_wins', '400')
# writeValuesData(True, 1, 80, 'PlayerVSPlayer')
# writeStaticsData(92, 15, 50, 20)
# setData('game_stats.ini', 'Statictics', 'Bot_wins', '400')
