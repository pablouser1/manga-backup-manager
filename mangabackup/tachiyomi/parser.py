from mangabackup.tachiyomi.models.Backup_pb2 import Backup
from google.protobuf.json_format import MessageToJson
import json
from types import SimpleNamespace

class TachiyomiParser:
    backup: Backup
    def __init__(self, path: str):
        self.backup = Backup()
        with open(path, 'rb') as f:
            self.backup.ParseFromString(f.read())
    
    def toJSON(self)-> dict:
        json_str = MessageToJson(self.backup)
        return json.loads(json_str)
