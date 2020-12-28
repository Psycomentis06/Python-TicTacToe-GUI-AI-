from configparser import ConfigParser

config = ConfigParser()
config.read('game_config.ini')

print(config['Game values'].get('dark_mode'))  # Gets as string
print(config['Game values'].getint('bot_level'))
print(config['Game values'].getint('sound_volume'))
print(config['Game values'].get('game_mode'))
