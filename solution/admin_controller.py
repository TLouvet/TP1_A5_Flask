
from flask import Blueprint, abort

admin_bp = Blueprint('admin', __name__)

@admin_bp.get("/admin")
def get_admin():
  abort(401)