# Manga Backup Converter
Allows to convert backups from Tachiyomi to Komikku and vice versa.

**This program is still in very early stage! At the time this program only allows converting from Tachiyomi to Komikku**

## How to use
After installing the dependencies, you can run
```bash
python3 main.py TACHIYOMI_BACKUP.proto ./OUT_DIR
```

You have to copy the resulting folder to the Komikku config ($HOME/.local/share/Komikku)

**MAKE SURE TO COPY EVERYTING INSIDE, INCLUDING THE EMPTY FOLDERS**

After copying it, start Komikku and hit the "Refresh library" button inside the three dots

## Known issues
* Categories are not working properly, some mangas get into the wrong category

## TODO
* Add support for more sources
* Blacklist sources not accepted
* Allow Komikku -> Tachiyomi conversions
* Allow to merge database with already existing one
