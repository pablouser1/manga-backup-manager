import sqlite3
import json
from pathlib import Path
from mangabackup.komikku import servers

class KomikkuWriter:
    db: sqlite3.Connection
    cur: sqlite3.Cursor
    path: str
    data: dict

    def __init__(self, path: str, data: dict):
        self.db = sqlite3.connect(f'{path}/komikku.db')
        self.cur = self.db.cursor()
        with open('./create_komikku.sql') as f:
            self.cur.executescript(f.read())
        self.path = path
        self.data = data
    
    def write(self):
        """
        Convert Tachiyomi to Komikku
        """
        mangas_komikku = []
        chapters_komikku = []
        categories_mangas_association = []

        mangas = self.data['backupManga']
        categories = self.data['backupCategories']
        sources = self.data['backupSources']

        categories_komikku = list(map(lambda category: (category['name'],), categories))
        for manga_index, manga in enumerate(mangas):
            allowed_servers = list(filter(lambda source: source['sourceId'] == manga['source'] and source['name'].lower() in servers, sources))
            if allowed_servers:
                # Source is allowed, continue
                server_id = allowed_servers[0]['name'].lower()
                url = None
                slug_manga = manga['url'].strip('/').split('/')[-1]
                Path(f'{self.path}/{server_id}/{manga["title"]}').mkdir(parents=True, exist_ok=True)
                # Mangas
                mangas_komikku.append((
                    slug_manga, url, server_id, manga['title'], json.dumps([manga['author']]), json.dumps([]),
                    json.dumps(manga['genre']) if 'genre' in manga else None,
                    manga['description'], 'complete', None, None, None, None, None, None
                ))
                # Categories
                for category in manga['categories']:
                    categories_mangas_association.append((category + 1, manga_index + 1))
    
        # --- INSERT TO DB ---
        # Mangas
        self.cur.executemany("""
            INSERT INTO "main"."mangas" ("slug", "url", "server_id", "name", "authors", "scanlators", "genres", "synopsis",
            "status", "background_color", "borders_crop", "page_numbering", "reading_mode", "scaling", "sort_order", "last_read", "last_update")
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'), STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'));
            """, mangas_komikku)
        # Categories
        self.cur.executemany('INSERT INTO "main"."categories" ("label") VALUES (?)', categories_komikku)
        # Categories manga relationship
        self.cur.executemany('INSERT INTO "main"."categories_mangas_association" ("category_id", "manga_id") VALUES (?, ?)', categories_mangas_association)
        self.db.commit()
        self.db.close()
