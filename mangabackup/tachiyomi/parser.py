from mangabackup.tachiyomi.models.Backup_pb2 import Backup
from google.protobuf.json_format import MessageToJson
import json

class TachiyomiParser:
    data: dict
    def __init__(self, path: str):
        backup = Backup()
        with open(path, 'rb') as f:
            backup.ParseFromString(f.read())
            self.data = json.loads(MessageToJson(backup))
    
    def getData(self)-> dict:
        return self.data
