# CONFIG
import configparser
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE staging_events
    (
        artist varchar(256),
        auth varchar(256),
        firstname varchar(256),
        gender varchar(1),
        iteminsession int4,
        lastname varchar(256),
        length numeric(18,0),
        level varchar(256),
        location varchar(256),
        method varchar(20),
        page varchar(20),
        registration numeric(18,0),
        sessionid int4,
        song varchar(256),
        status int4,
        ts int8,
        userAgent varchar(256),
        userId int4
    );
""")

staging_songs_table_create = ("""
    CREATE TABLE staging_songs
    (
    num_songs INTEGER,
    artist_id TEXT,
    artist_latitude NUMERIC, 
    artist_longitude NUMERIC,
    artist_location TEXT,
    artist_name VARCHAR(MAX),
    song_id TEXT,
    title TEXT,
    duration NUMERIC, 
    year INT
    );
""")

# STAGING TABLES

staging_events_copy = ("""
    COPY {} FROM {}
    IAM_ROLE '{}'
    JSON {};
""").format(
    'staging_events',
    config['S3']['LOG_DATA'],
    config['IAM_ROLE']['ARN'],
    config['S3']['LOG_JSONPATH']
)

staging_songs_copy = ("""
    COPY {} FROM {}
    IAM_ROLE '{}'
    JSON 'auto';
""").format(
    'staging_songs',
    config['S3']['SONG_DATA'],
    config['IAM_ROLE']['ARN']
)

# FINAL TABLES


# QUERY LISTS

create_table_queries = [staging_events_table_create,staging_songs_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy,staging_songs_copy]
