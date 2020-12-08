from flask_login import LoginManager
from models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    print("Trying to login with: {}".format(user_id))
    return User.query.filter_by(login_id=user_id).first()
