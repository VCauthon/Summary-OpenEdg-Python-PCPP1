import configparser
import os


class CreateConfig:
    
    def __init__(self, path_config_file: str):
        self.production = configparser.ConfigParser()
        self.develop = configparser.ConfigParser()
        self.__parse_file(path_config_file)

    def __parse_file(self, path_config_file:str) -> None:

        parser = configparser.ConfigParser()
        parser.read(path_config_file)

        for section in parser.sections():

            values = parser[section]
            env = values.pop('env')

            if env == 'prod':
                self.production[section] = values
            elif env == 'dev':
                self.develop[section] = values

    @staticmethod
    def create_config(name: str, config: configparser.ConfigParser) -> None:
        with open(name, mode='+w') as file:
            config.write(file)


if __name__ == "__main__":
    
    os.chdir(os.path.dirname(__file__))

    config_generator = CreateConfig('../persistance/mess.ini')
    config_generator.create_config('../persistance/prod_config.ini', config_generator.production)
    config_generator.create_config('../persistance/dev_config.ini', config_generator.develop)
