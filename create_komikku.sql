-- categories definition

CREATE TABLE categories (
        id integer PRIMARY KEY,
        label text NOT NULL,
        UNIQUE (label)
    );


-- mangas definition

CREATE TABLE mangas (
        id integer PRIMARY KEY,
        slug text NOT NULL,
        url text, -- only used in case slug can't be used to forge the url
        server_id text NOT NULL,
        name text NOT NULL,
        authors json,
        scanlators json,
        genres json,
        synopsis text,
        status text,
        background_color text,
        borders_crop integer,
        page_numbering integer,
        reading_mode text,
        scaling text,
        sort_order text,
        last_read timestamp,
        last_update timestamp,
        UNIQUE (slug, server_id)
    );


-- categories_mangas_association definition

CREATE TABLE categories_mangas_association (
        category_id integer REFERENCES categories(id) ON DELETE CASCADE,
        manga_id integer REFERENCES mangas(id) ON DELETE CASCADE,
        UNIQUE (category_id, manga_id)
    );


-- chapters definition

CREATE TABLE chapters (
        id integer PRIMARY KEY,
        manga_id integer REFERENCES mangas(id) ON DELETE CASCADE,
        slug text NOT NULL,
        url text, -- only used in case slug can't be used to forge the url
        title text NOT NULL,
        scanlators json,
        pages json,
        scrambled integer,
        date date,
        rank integer NOT NULL,
        downloaded integer NOT NULL,
        recent integer NOT NULL,
        read integer NOT NULL,
        last_page_read_index integer, last_read timestamp,
        UNIQUE (slug, manga_id)
    );


-- downloads definition

CREATE TABLE downloads (
        id integer PRIMARY KEY,
        chapter_id integer REFERENCES chapters(id) ON DELETE CASCADE,
        status text NOT NULL,
        percent float NOT NULL,
        errors integer DEFAULT 0,
        date timestamp NOT NULL,
        UNIQUE (chapter_id)
    );
