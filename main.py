import argparse
from mangabackup.Helpers import Helpers
from mangabackup.tachiyomi.parser import TachiyomiParser
from mangabackup.komikku.writer import KomikkuWriter

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert manga reader backup formats')
    parser.add_argument('input', help='Tachiyomi .proto path')
    parser.add_argument('output', help='Output path')

    args = parser.parse_args()

    Helpers.clearOutput(args.output)

    tachiyomi = TachiyomiParser(args.input)
    data = tachiyomi.getData()
    komikku = KomikkuWriter(args.output, data)
    komikku.write()
    print("DONE! Please check your output folder")
