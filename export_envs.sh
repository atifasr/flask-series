#bash
# just to automate mundane stuff!


source test-env/bin/activate

export FLASK_APP=$HOME/Documents/Video_series/flask_series/FLASK_CRUD/run.py
export FLASK_ENV=development
export DEBUG=True

flask run