import os
from flask_script import Manager

from app import create_app, db

env = os.getenv("FLASK_ENV") or "prod"
print(f"Active environment: * {env} *")
app = create_app(env)

manager = Manager(app)
app.app_context().push()


@manager.command
def run():
    app.run()


@manager.command
def init_db():
    db.create_all()

@manager.command
def drop_all():
    db.drop_all()


if __name__ == "__main__":
    manager.run()