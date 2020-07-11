from my_app import db
from datetime import datetime


# Criar o model
class BlogPost(db.Model):  # herda do Model
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)  # chave primária
    title = db.Column(db.String(100), nullable=False)  # não pode ser Null
    content = db.Column(db.Text, nullable=False)  # text é string sem limite
    author = db.Column(db.String(10), nullable=False, default='N/A')  # é requirido ter valor mas se não tiver
    # preenche com um default
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):  # método que dá print cada ver que um post é criado
        return "Blog post " + str(self.id)
