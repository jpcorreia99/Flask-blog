from flask import Flask, render_template

app = Flask(__name__)  # __name__ referencia o ficheiro

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1',
        'author': 'Aaron'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2'
    }
]


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


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=all_posts)


# http://127.0.0.1:5000/home/users/john/posts/1

if __name__ == "__main__":
    app.run(debug=True)  # atcually shows the errors and not just the codes

# Nota: ps -fA | grep python e kill do pid para terminar outros flasks
