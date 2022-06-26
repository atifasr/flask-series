

from app.crud.controller import index
from app import app

app.add_url_rule("/","index",index,methods=["GET"])
