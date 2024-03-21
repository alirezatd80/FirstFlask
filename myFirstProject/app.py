from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
db = SQLAlchemy(app)


class FirstProjectFlask(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.Text,unique = True , nullable = False)
    date =db.Column(db.DateTime , default = datetime.now)
    
    def __repr__(self) :
        return f'myFirstProject({self.id} - {self.content} - {self.date})'
    
def addInDB(text):

    model1 = FirstProjectFlask(content = text)
    db.session.add(model1)
    db.session.commit()
    
        
with app.app_context():
    
       db.create_all()
   

@app.route('/')
def  home():
    
    return render_template('home.html')

@app.route('/about')
def about():
    
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)