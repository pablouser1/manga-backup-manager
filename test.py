from mangabackup.tachiyomi.parser import TachiyomiParser
from mangabackup.komikku.writer import KomikkuWriter
from mangabackup.Helpers import Helpers

Helpers.clearOutput('./tests')
tachiyomi = TachiyomiParser('./data/tachiyomi_2022-01-20_10-05.proto')
data = tachiyomi.toJSON()
komikku = KomikkuWriter('./tests', data)
komikku.write()
print("DONE! Please check your output folder")
