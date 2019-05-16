
from flask_script import Manager, Server
from app import app, db
from models import User

manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    d = dict(app=app,db=db)
    d.update({
        "User":User
    })
    return  d

if __name__ == "__main__":
    manager.run()