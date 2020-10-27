"""app.py"""
# pylint: disable=missing-docstring,too-few-public-methods,invalid-name
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app=Flask(__name__)

ENV='prod'

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Vandana@123@localhost/lexus'

else:
    app.debug=False
    app.config['SQlALCHEMY_DATABASE_URI']='postgres://zchnnklwxrwpvt:5d7069b7e3b187e49cfcb39b44c9fcae828643c63b8c77097c70d588b51233b1@ec2-23-20-70-32.compute-1.amazonaws.com:5432/da3vs81fp6jcod'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__='feedback'
    id=db.Column(db.Integer,primary_key=True)
    customer=db.Column(db.String(200), unique=True)
    dealer=db.Column(db.String(200))
    rating=db.Column(db.Integer)
    comments=db.Column(db.Text())

    def __init__(self,customer,dealer,rating,comments):
        self.customer=customer
        self.dealer=dealer
        self.rating=rating
        self.comments=comments 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST']) 
def submit():
    if request.method=='POST':
        customer=request.form['customer']
        dealer=request.form['dealer']
        rating=request.form['rating']
        comments=request.form['comments']
        print(customer,dealer,rating,comments)
        if customer=='' or dealer=='':
            return render_template('index.html',message="Please enter the required fields")
        if db.session.query(Feedback).filter(Feedback.customer==customer).count()==0:
            data=Feedback(customer,dealer,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer,dealer,rating,comments)
            return render_template('success.html')

        return render_template('index.html',message="You have already submitted feedback")

if __name__ == '__main__':
   
    app.run() 
