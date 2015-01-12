import json
import sqlite3
import os

def gen_create_table_sql(table_json):
    table_name = table_json['table_name']
    columns = table_json['columns']
    column_name_and_types = [column['column_name']+" "+column['data_type'] for column in columns]
    prime_key_names = [column['column_name'] for column in columns if column['is_prime_key']==1]

    prime_key_str = ""
    if len(prime_key_names) > 0:
        prime_key_str = ", PRIMARY KEY({0})".format(", ".join(prime_key_names))

    return "CREATE TABLE {0} ({1}{2})".format(table_name, ", ".join(column_name_and_types), prime_key_str)

def assemble_column_names_values_list(dataset):
    def get_parameters(record):
        names =  [name for name, value in record.items()]
        values =  ['\'{0}\''.format(value) if value else 'null' for name, value in record.items()]
        return (','.join(names), ','.join(values))
    return [get_parameters(record) for record in dataset]


def create_db(db_file_path, schema_path):
    schema_json = loads_json_from_file(schema_path)
    table_sql_list = [(table_json['table_name'], gen_create_table_sql(table_json)) 
        for table_json in schema_json]


    conn = sqlite3.connect(db_file_path)
    successful_talbe_names = []
    def exe_table_sql(table_name, table_sql):
        conn.execute(table_sql)
        return table_name

    with conn:
        successful_talbe_names = [exe_table_sql(table_name, table_sql) 
            for table_name, table_sql in table_sql_list]
    conn.close()
    return successful_talbe_names

def gen_table_sql_file(file_path, schema_path):
    schema_json = loads_json_from_file(schema_path)
    table_sql_list = [(table_json['table_name'], gen_create_table_sql(table_json)) 
        for table_json in schema_json]
    successful_talbe_names = []
    def write_table_sql(table_name, table_sql):
        the_file.write(str(table_sql)+";\n")
        return table_name
    with open(file_path, 'w') as the_file:
        successful_talbe_names = [write_table_sql(table_name, table_sql) 
            for table_name, table_sql in table_sql_list]
    return successful_talbe_names


def loads_json_from_file(file_path):
    with open(file_path) as the_file:
        schema_str = the_file.readlines()
    schema_str = "".join(schema_str).replace("\n","")
    return json.loads(schema_str)

def check_and_remove(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    return file_path


if __name__ == '__main__':
    from minitest import *

    schema_path = "schema.json"
    
    with test(loads_json_from_file):
        loads_json_from_file(schema_path).must_equal(
            [{u'table_name': u'bar', 
              u'columns': [
                {u'is_prime_key': 1, u'data_type': u'text', u'column_name': u'name'}, 
                {u'is_prime_key': 1, u'data_type': u'integer', u'column_name': u'no'}, 
                {u'is_prime_key': 0, u'data_type': u'text', u'column_name': u'content'}, 
                {u'is_prime_key': 0, u'data_type': u'timestamp', u'column_name': u'last_update'}]},
             {u'table_name': u'foo', 
              u'columns': [
                {u'is_prime_key': 0, u'data_type': u'text', u'column_name': u'content'}, 
                {u'is_prime_key': 0, u'data_type': u'timestamp', u'column_name': u'last_update'}]}])

    with test(gen_create_table_sql):
        table_schema = {u'table_name': u'bar', 
                        u'columns': [
                            {u'is_prime_key': 1, u'data_type': u'text', u'column_name': u'name'}, 
                            {u'is_prime_key': 1, u'data_type': u'integer', u'column_name': u'no'}, 
                            {u'is_prime_key': 0, u'data_type': u'text', u'column_name': u'content'}, 
                            {u'is_prime_key': 0, u'data_type': u'timestamp', u'column_name': u'last_update'}]}
        gen_create_table_sql(table_schema).must_equal(
            'CREATE TABLE bar (name text, no integer, content text, last_update timestamp, PRIMARY KEY(name, no))')

        table_schema = {u'table_name': u'foo', 
                        u'columns': [
                            {u'is_prime_key': 0, u'data_type': u'text', u'column_name': u'content'}, 
                            {u'is_prime_key': 0, u'data_type': u'timestamp', u'column_name': u'last_update'}]}
        gen_create_table_sql(table_schema).must_equal(
            'CREATE TABLE foo (content text, last_update timestamp)')

    with test(create_db):
        db_file_path='test.db'
        check_and_remove(db_file_path)
        table_names = create_db(db_file_path, schema_path)

        table_results = { 'bar':(u'table', u'bar', u'bar', 2, u'CREATE TABLE bar (name text, no integer, content text, last_update timestamp, PRIMARY KEY(name, no))'),
                          'foo':(u'table', u'foo', u'foo', 4, u'CREATE TABLE foo (content text, last_update timestamp)')}
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        for table_name in table_names:
            cursor.execute('SELECT * FROM sqlite_master where type="table" and name=?', (table_name,))
            cursor.fetchone().must_equal(table_results[table_name])
        conn.close()

    with test(gen_table_sql_file):
        sql_file_path = 'test.sql'
        check_and_remove(sql_file_path)
        # gen_table_sql_file(sql_file_path,schema_path).pp()

    with test(assemble_column_names_values_list):
        dataset = [
                {"name": "record_1",
                 "no":    1,                 
                 "content": None,
                 "last_update": "2014-09-27 14:30:01",
                },
                {"name": "record_2",
                 "no":    2,                 
                 "content": None,
                 "last_update": "2014-09-27 14:30:01",
                }
            ]
        assemble_column_names_values_list(dataset).must_equal(
            [('content,last_update,name,no',
              "null,'2014-09-27 14:30:01','record_1','1'"),
             ('content,last_update,name,no',
              "null,'2014-09-27 14:30:01','record_2','2'")])




