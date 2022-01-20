from os.path import isfile
from os import remove
class Helpers:
    @staticmethod
    def clearOutput(path: str):
        if isfile(path + '/komikku.db'):
            remove(path + '/komikku.db')
