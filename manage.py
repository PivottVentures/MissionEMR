from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db
app.config.from_object('config.ProductionConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(port=9000))

if __name__ == '__main__':
    manager.run()