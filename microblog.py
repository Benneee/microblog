from distutils.log import debug
from app import app
from config import Config

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

# To run the app, add this in the terminal so flask knows 
# what file to run so it can start this application
# export FLASK_APP=microblog.py