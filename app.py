from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drawings.db'
db = SQLAlchemy(app)

# Define the Drawing model
class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
# API endpoints
@app.route('/drawings', methods=['POST'])
def create_drawing():
   
@app.route('/drawings/<int:drawing_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_drawing(drawing_id):
   .

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
