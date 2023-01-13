#import libraries
import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop the tables
    :param cur: database cursor to execute the queries
    :param conn: conn to be used to commit and close the transaction
    :return: None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create the tables to be used in ETL process
    :param cur: database cursor to execute the queries
    :param conn: conn to be used to commit and close the transaction
    :return: None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Main strating point of the file
    """
    #read the config files
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    #create the connection to redshift database using the config files
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    #drop the tables and then create the tables
    drop_tables(cur, conn)
    print("Dropped tables")
    create_tables(cur, conn)
    print("Tables created")

    conn.close()


if __name__ == "__main__":
    main()