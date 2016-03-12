from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Shell
from app.models import User, Role
from app import app, db

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.option('-n', '--name', help='Your name', dest='name')
def hello(name):
    print "hello", name

if __name__ == "__main__":
    manager.run()