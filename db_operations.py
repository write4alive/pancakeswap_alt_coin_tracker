import sqlite3
from sql_query import create_table_token_list, insert_token_list, drop_token_list, select_token_list, truncate_table_token_list

conn = sqlite3.connect('pancakeswawp.db')

def db_init():
    """
    Creating sqlite database for alt coins
    """

    # Create table
    conn.execute(drop_token_list)
    conn.execute(create_table_token_list)
    conn.commit()

def insert(values : list):
    """
    Insert data into table token list
    """

    cur = conn.cursor()
    cur.execute(insert_token_list,(values))
    conn.commit()

def select() -> list:
    """
    Select data from token list
    """
    data = conn.execute(select_token_list).fetchall()
    return data

def truncate():
    """
    Truncate table token list
    """
    conn.execute(truncate_table_token_list)
    conn.commit()
    