from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
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
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):  # método que dá print cada ver que um post é criado
        return "Blog post " + str(self.id)


# para gerar a db, abrir o python e escrever 'from databases import db'
# db.create_all()
# para adicionar coisas à db
# from databases import BlogPost
# BlogPost.query.all() - devolve todas as entradas
#  db.session.add(BlogPost(title='Blog Post 1',content='Content of blog post 1', author='Aaron'))
# BlogPost.query.all() o que aparece é a string devolvida pelo método __repr__
# db.session.add(BlogPost(title='Another Blog Post',content='Content of blog post 2', author='Aaron'))
# irá aparcer [Blog Post 1, Blog Post 2]
# posso obter apenas uma entrada fazendo BlogPost.query.all()[indice do post].campo_a_verificar
# BlogPost.query.all()[2].author


# para ler:
# from database_to_frontend import db, BlogPost
# BlogPost.query.all()[i].field
# BlogPost.query.filter_by(title='a').all()
# BlogPost.query.get(1) # id

# para apagar
# from database_to_frontend import db, BlogPost
# db.session.delete(BlogPost.query.get(2))
# db.session.commit()


@app.route("/")
def index():  # também corre html
    return render_template('index.html')  # configurar o templates directory, verificar que usei o jinja2 para
    # extendar o base html


@app.route("/home/users/<string:name>/posts/<int:post_id>")  # permide criar urls dinâmicos
def hello(name, post_id):
    return "Hello, " + name + ", the id of this post is " + str(post_id)


# esta página apenas permite gets, não posts
# se colocar POST não ia conseguir aceder à página
@app.route("/onlyget", methods=['GET'])
def get_req():
    return 'You can only get this webpage'


@app.route("/posts", methods=['GET', 'POST'])  # para poder inserir na bd
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()  # para guardar permanentemente na bd e não só na sessão
        return redirect('/posts')
    else:  # é um get
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()  # só query.all também servia
        return render_template('posts.html', posts=all_posts)


@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


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


# http://127.0.0.1:5000/home/users/john/posts/1

if __name__ == "__main__":
    app.run(debug=True)  # atcually shows the errors and not just the codes

# Nota: ps -fA | grep python e kill do pid para terminar outros flasks
