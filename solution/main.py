from flask import Flask
from flask_cors import CORS
from task_controller import task_bp
from admin_controller import admin_bp

app = Flask(__name__)
CORS(app)

#Attention, on pourrait passer url_prefix en paramètre mais ça ne fonctionne pas avec CORS
#Il faudrait alors ajouter une preflight, voir app.before_request dans la doc de Flask
app.register_blueprint(task_bp) 
app.register_blueprint(admin_bp)

@app.get('/') 
def hello_world():
  return {"message": "Hello World"}
