from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db
<<<<<<< HEAD
app.config.from_object('config.DevelopmentConfig')
=======
>>>>>>> 96e00611caec713d507b77a91e32d88fa48babee

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()