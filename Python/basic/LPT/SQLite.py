#!/usr/bin/env python

##################################################
# {Description}
##################################################
# {License_info}
##################################################
# Author: {hubert_hao}
# Copyright: Copyright {2019}, {project_name}
# Credits: [{credit_list}]
# License: {license}
# Version: {mayor}.{minor}.{rel}
# Maintainer: {maintainer}
# Email: {contact_email}
# Status: {dev_status}
##################################################

import sqlite3
import os


class SQLiteDB(object):
    """SQLite3 DB Wrapper Class
    provides CRUD operation
    """

    def __init__(self, dbfile):
        data_dir = os.path.join(os.getcwd(), "data")
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        self.__db = sqlite3.connect(os.path.join(data_dir, dbfile))

    def __del__(self):
        self.__db.close()

    def _exec_write(self, commands, data = tuple()):
        try:
            cursor = self.__db.cursor()
            cursor.execute(commands, data)
        except Exception as e:
            self.__db.close()
            raise e
        else:
            self.__db.commit()

    def create(self, table_name="test_table", fields=("id NUMERIC", "desc TEXT")):
        commands = f"""
        CREATE TABLE IF NOT EXISTS {table_name}({", ".join(fields)})
        """
        # print(commands)
        self._exec_write(commands)

    def read(self, table_name, query):
        commands = f"""
        SELECT {", ".join(query["fields"])} FROM {table_name}
        WHERE {query["conditions"]}
        """
        # print(commands)
        cursor = self.__db.cursor()
        cursor.execute(commands)
        return cursor.fetchall()

    def update(self, table_name, primary_key, rows):
        for record in rows:
            fields = record.keys()
            values = tuple(record[key] for key in fields)
            update_fields = list(filter(lambda x: x != primary_key, fields))
            update_values = tuple(record[key] for key in update_fields)

            substituestr1 = "?, "*len(update_fields)+"?"

            substituestr2 = ", ".join([key+"=(?)" for key in update_fields])

            vals = (*values, *update_values)

            # print(vals)

            commands = f"""
                INSERT INTO {table_name}({", ".join(fields)}) 
                VALUES({substituestr1}) 
                ON CONFLICT({primary_key}) 
                DO UPDATE SET {substituestr2}                        
                """

            # print(commands)
            self._exec_write(commands, vals)

    def delete(self, table_name, query=""):
        if query:
            commands = f"""
                DELETE FROM {table_name} WHERE {query["conditions"]}
                """
        else:
            commands = f"""
            DROP TABLE IF EXISTS {table_name}
            """
        self._exec_write(commands)


if __name__ == '__main__':
    table = {
        "table_name": "books",
        "fields": ("name TEXT PRIMARY KEY", "author TEXT", "read NUMERIC")
    }

    data = [
        {"name": "book1",
         "author": "author1",
         "read": 1},
        {"name": "book2",
         "author": "updateauthor",
         "read": 0}]

    query = {
        "fields": ["name", "author", "read"],
        "conditions": "read = 0"
    }

    mydb = SQLiteDB("test.db")

    mydb.create(**table)

    mydb.update("books", "name", data)
    mydb.update("books", "name", [{"name":"newbook", "author": "harry"}])

    print(mydb.read("books", query))

    mydb.delete("books", {"conditions": "name='boo1'"})

    # mydb.create()
    # mydb.delete("test_table")