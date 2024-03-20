from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstFlask.db'
db = SQLAlchemy(app)


class FirstProjectFlask(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.Text,unique = True , nullable = False)
    date =db.Column(db.DateTime , default = datetime.now)
    
    def __repr__(self) :
        return f'FirstProjectFlask({self.id} - {self.content} - {self.date})'
    
    

@app.route('/')
def  home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)