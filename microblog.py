from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# To run the app, add this in the terminal so flask knows 
# what file to run so it can start this application
# export FLASK_APP=microblog.py