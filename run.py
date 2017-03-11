from models.database_setup import SQLAlchemyService

from flask import Flask
import pymongo

from api_cmds.routes import routes

app = Flask(__name__)
app.secret_key = 'development-key'

# Setup connectivity with MongoDB
mongo_client = pymongo.MongoClient('mongodb', 27017)

# Setup database connectivity with Postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres/location_based_service'
SQLAlchemyService().instantiate_sql_alchemy()
SQLAlchemyService().initialize_db(app)

# Register all the url routes
for route in routes:
    app.register_blueprint(route)

if __name__ == "__main__":
    # Run flask app in debug bug on localhost
    app.run(host="0.0.0.0", port=8000, debug=True)
