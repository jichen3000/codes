import sqlite3

def create_simple():
    conn = sqlite3.connect('example.db')

    # c = conn.cursor()
    with conn as c:

        # Create table
        c.execute('''CREATE TABLE stocks
                     (date text, trans text, symbol text, qty real, price real, PRIMARY KEY(symbol, price))''')

        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        # conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
    conn.close()

def get_schema(table_name):
    conn = sqlite3.connect('example.db')

    # Columns in the result set include the column name, data type, 
    # whether or not the column can be NULL, and the default value for the column,
    # wheter or not 
    for row in conn.execute("pragma table_info('{0}')".format(table_name)).fetchall():
        print row
    conn.close()

def column_timestamp():
    db = sqlite3.connect('example.db', detect_types=sqlite3.PARSE_DECLTYPES)
    c = db.cursor()
    c.execute('create table foo (bar integer, baz timestamp)')
    db.close
if __name__ == '__main__':
    # get_schema("stocks")
    # create_simple()
    column_timestamp()

