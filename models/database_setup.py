from flask_sqlalchemy import SQLAlchemy


class SQLAlchemyService(object):
    def __init__(self):
        self.db = None

    def instantiate_sql_alchemy(self):
        """
            Instantiates a SQL Alchemy instance if one isn't already present
        """
        if not self.db:
            self.db = SQLAlchemy()
        return self.db

    def initialize_sql_alchemy(self):
        """
            Initializes the SQL Alchemy connection to the database
        """
        if not self.db:
            self.instantiate_sql_alchemy()
        self.db.init_app()

    def get_instance(self):
        """
            Getter method for the db instance
        """
        return self.db


