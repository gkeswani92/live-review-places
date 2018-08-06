from flask import Flask
from models.database_setup import SQLAlchemyService

from api_cmds.routes import about_page
from api_cmds.routes import home_page
from api_cmds.routes import index_page
from api_cmds.registration import login_page
from api_cmds.registration import sign_out_page
from api_cmds.registration import sign_up_page


app = Flask(__name__)

# Setup database connectivity
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/location_based_service'
SQLAlchemyService().instantiate_sql_alchemy()
SQLAlchemyService().initialize_db(app)

# Register blueprint for index and about pages
app.register_blueprint(index_page)
app.register_blueprint(about_page)
app.register_blueprint(sign_up_page)
app.register_blueprint(sign_out_page)
app.register_blueprint(home_page)
app.register_blueprint(login_page)

app.secret_key = 'development-key'

if __name__ == "__main__":
    # Run flask app in debug bug on localhost
    app.run(host="0.0.0.0", port=8000, debug=True)
