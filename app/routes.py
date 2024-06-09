from flask import Blueprint, render_template, request, redirect, url_for
from .models import Comment
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/box/<int:box_id>', methods=['GET', 'POST'])
def box(box_id):
    if request.method == 'POST':
        content = request.form['content'] 
        comment = Comment(box_id=box_id, content=content)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.box', box_id=box_id))

    comments = Comment.query.filter_by(box_id=box_id).all()
    return render_template('box.html', box_id=box_id, comments=comments)
