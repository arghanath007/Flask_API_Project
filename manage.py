import os
import unittest


from flask_migrate import Migrate
# from flask_script import Manager

from app.main import create_app, db
from app.main.model.user import User

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

# For Flask Version 1.0

# manager = Manager(app)

migrate = Migrate(app, db)

# manager.add_command('db', MigrateCommand)

# @manager.command
# def run():
#     app.run()

# @manager.command
# def test():
#     """Runs the unit tests."""
#     tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1

# if __name__ == '__main__':
#     manager.run()