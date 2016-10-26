from models.user import User
from models.database_setup import SQLAlchemyService

db = SQLAlchemyService().get_instance()


def register_user(first_name, last_name, email, password):
    """
    Creates a new user with the passed in data and saves it to the database
    """
    try:
        user = User(
            firstname=first_name,
            lastname=last_name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()
        return "Successfully added user to the database"
    except Exception as e:
        db.session.rollback()
        return e.message
