import sys

from PyQt5.QtWidgets import QWidget, QApplication
from GameMenu import MenuInterface
from GameConfig import GameConfig


class BootStrap(QWidget):
    """The bootStrap class is the one who is responsible to open the menu interface class with default arguments"""

    def __init__(self):
        super().__init__()
        try:  # if the file exists he will get the values saved in it
            config = GameConfig()
            darkMode = config.readData('game_config.ini', 'Game values', 'dark_mode', 'bool')
            botLevel = config.readData('game_config.ini', 'Game values', 'bot_level', 'int')
            soundVolume = config.readData('game_config.ini', 'Game values', 'sound_volume', 'int')
            self.menuUi = MenuInterface(darkMode, soundVolume, botLevel)  # send the default values of data
            self.menuUi.show()
        except:  # If the file is missing he will create it with default values
            config = GameConfig()
            config.writeValuesData(True, 50, 2)
            darkMode = config.readData('game_config.ini', 'Game values', 'dark_mode', 'bool')
            botLevel = config.readData('game_config.ini', 'Game values', 'bot_level', 'int')
            soundVolume = config.readData('game_config.ini', 'Game values', 'sound_volume', 'int')
            self.menuUi = MenuInterface(darkMode, soundVolume, botLevel)  # send the default values of data
            self.menuUi.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    boot = BootStrap()
    sys.exit(app.exec_())
