from flask import ( Blueprint, render_template )

bp = Blueprint('fact', __name__, url_prefix="/facts")

# new fact page
@bp.route('/new')
def new():
    return render_template('new.html')