from my_app import app, db
from models import BlogPost
from flask import Flask, render_template, request, redirect
from datetime import datetime
from sqlalchemy import desc


@app.route("/")
def index():  # também corre html
    return render_template('index.html')  # configurar o templates directory, verificar que usei o jinja2 para
    # extendar o base html


# página que apresenta os posts todos
@app.route("/posts")
def posts():
    all_posts = BlogPost.query.order_by(desc(BlogPost.date_posted)).all()  # só query.all também servia
    return render_template('posts.html', posts=all_posts)


# link que permite apagar um post
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


# página que permite criar um post
@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':  # se o form tiver sido preenchido
        post_title = request.form['title']
        post_author = request.form['author']
        post_content = request.form['content']
        post = BlogPost(title=post_title, content=post_content, author=post_author,
                        date_posted=datetime.now())
        print(post.date_posted)
        print(datetime.utcnow())
        print(post.content)
        db.session.add(post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')  # para apresentar o form a preencher


# página que permite atualizar um post
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])  # pois vamos postar novamente na bd
def update(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':  # se o form tiver sido preenchido
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)  # para apresentar o form a preencher
