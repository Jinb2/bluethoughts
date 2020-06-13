from flask import render_template, url_for, redirect, flash, request
from bluethoughts import app, db
from bluethoughts.forms import PostForm
from bluethoughts.models import Post


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/submit/new', methods=['GET','POST'])
def submit():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(keywords=form.keywords.data,message=form.message.data,location=form.location.data)
        db.session.add(post)
        db.session.commit()
        flash('Your thought has been submitted','success')
        return redirect(url_for('explore'))
    return render_template('submit.html',form=form)


@app.route('/explore')
def explore():
    page = request.args.get('page', 1,type=int)
    posts = Post.query.paginate(page=page,per_page=25)
    return render_template('explore.html',posts=posts)



@app.errorhandler(404)
def error404(error):
    return render_template('404.html')

@app.errorhandler(500)
def error500(error):
    return render_template('500.html')

@app.errorhandler(403)
def error403(error):
    return render_template('403.html')
