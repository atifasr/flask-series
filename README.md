# Flask-series

# Clone changes
git clone -b master https://github.com/atifasr/flask-series.git

# Create Virtual env for linux 
virtualenv <env name>

# Activate environment
source <env name>/bin/activate


# Install Dependencies
pip install -r requirements.txt

# Export Envs
export FLASK_APP=run.py
export FLASK_ENV=development

#Run Application
flask run
