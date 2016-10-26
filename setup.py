from models.database_setup import SQLAlchemyService
from api_cmds.routes import about_page
from api_cmds.routes import index_page
from api_cmds.routes import sign_up_page
from flask import Flask


app = Flask(__name__)

# Setup database connectivity
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/location_based_service'
db = SQLAlchemyService().instantiate_sql_alchemy()
db.init_app(app)

# Register blueprint for index and about pages
app.register_blueprint(index_page)
app.register_blueprint(about_page)
app.register_blueprint(sign_up_page)

app.secret_key = 'development-key'

if __name__ == "__main__":
    # Run flask app in debug bug on localhost
    app.run(host="0.0.0.0", port=4000, debug=True)