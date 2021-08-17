#!/usr/bin/env python3
""" Personal data
"""
from typing import List
import logging
import re
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format 
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ Regex-ing
    """
    for field in fields:
        message = re.sub(field + '=.*?' + separator, field + '=' +
                         redaction + separator, message)
    return message

def get_logger() -> logging.Logger:
    """ Get logger
    """
    log = logging.getLoger("user_data")
    log.setLevel(loggin.INFO)
    log.propagate = False
    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(sh)
    return log

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Database SQL
    """
    username_db = getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password_db = getenv('PERSONAL_DATA_DB_PASSWORD', ' ')
    host_db = getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    name_db = getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connection.MySQLConnection(user=username_db,
                                                      password=password_db,
                                                      host=host_db,
                                                      database=name_db)

def main() -> None:
    """ Main
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    num_fields = len(cursor.description)
    fields_names = [i[0] for i in cursor.description]
    log = get_logger()

    for row in cursor:
        message = ''
        for item in range(num_fields):
            message += fields_name[item] + '=' + str(row[item]) + ';'
        log.info(message)
    cursor.close()
    db.close()
    

if __name__ == "__main__":
    main()
