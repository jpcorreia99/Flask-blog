from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime

app = Flask(__name__)  # __name__ referencia o ficheiro
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.dd'  # posso mudar isto facilmente sem ter de mudar o resto do código
# 3 / - relative path, 4/ absolute

db = SQLAlchemy(app)


# Criar o model
class BlogPost(db.Model):  # herda do Model
    id = db.Column(db.Integer, primary_key=True)  # chave primária
    title = db.Column(db.String(100), nullable=False)  # não pode ser Null
    content = db.Column(db.Text, nullable=False)  # text é string sem limite
    author = db.Column(db.String(10), nullable=False, default='N/A')  # é requirido ter valor mas se não tiver
    # preenche com um default
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):  # método que dá print cada ver que um post é criado
        return "Blog post " + str(self.id)


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


if __name__ == "__main__":
    app.run(debug=True)  # atcually shows the errors and not just the codes

# Nota: ps -fA | grep python e kill do pid para terminar outros flasks
