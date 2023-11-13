import subprocess
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from greenlet import getcurrent
from sqlalchemy.orm import scoped_session
from database import SessionLocal
from models import Flat


app = Flask(__name__)
Bootstrap(app)
app.session = scoped_session(SessionLocal, scopefunc=getcurrent)

@app.route('/scrape')
def scrape():
    """
    Endpoint for sraping flats from sreality.cz.
    ---
    parameters:

    responses:
      200:
        description: Success message
    """
    spider_name = 'flats'
    result_file = 'dump.json'
    response = subprocess.call(['scrapy', 'crawl', spider_name, '-o', result_file])
    return 'OK'

@app.route('/')
def get_all():
    """
    Endpoint for displaying list of flats from sreality.cz.
    ---
    parameters:

    responses:
      200:
        render_template: html template with list of flats
    """
    all_flats = list(app.session.query(Flat).all())
    return render_template('index.html', data=all_flats)

@app.route('/clear_db')
def clear_db():
    """
    Endpoint for removing all flats data from database.
    ---
    parameters:

    responses:
      200:
        description: Success message
    """
    # remove_all_data()
    deletion_result = app.session.query(Flat).delete()
    app.session.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

