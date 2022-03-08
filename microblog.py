from distutils.log import debug
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# To run the app, add this in the terminal so flask knows 
# what file to run so it can start this application
# export FLASK_APP=microblog.py