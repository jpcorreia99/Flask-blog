from flask import Flask

app = Flask(__name__)  # __name__ referencia o ficheiro


@app.route("/home/users/<string:name>/posts/<int:post_id>")  # permide criar urls dinâmicos
def hello(name, post_id):
    return "Hello, " + name + ", the id of this post is " + str(post_id)


# esta página apenas permite gets, não posts
# se colocar POST não ia conseguir aceder à página
@app.route("/onlyget", methods=['GET'])
def get_req():
    return 'You can only get this webpage'


# http://127.0.0.1:5000/home/users/john/posts/1

if __name__ == "__main__":
    app.run(debug=True)  # atcually shows the errors and not just the codes

# Nota: ps -fA | grep python e kill do pid para terminar outros flasks
