from configparser import ConfigParser

config = ConfigParser()
config['Game values'] = {
        'Dark_mode': True,
        'Bot_level': 2,
        'Sound_volume': 50,
        'Game_mode': 'PlayerVSBot'
    }


with open('game_config.ini', 'w') as output_file:
    config.write(output_file)
