from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drawings.db'
db = SQLAlchemy(app)

# Drawing model
class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shape_type = db.Column(db.String(50), nullable=False)
    coordinates = db.Column(db.String(255), nullable=False)
    dimensions = db.Column(db.String(255))
    annotations = db.Column(db.String(255))

# API endpoints
@app.route('/drawings', methods=['POST'])
def create_drawing():
    data = request.json

    new_drawing = Drawing(
        shape_type=data['shape_type'],
        coordinates=data['coordinates'],
        dimensions=data.get('dimensions', ''),
        annotations=data.get('annotations', '')
    )

    db.session.add(new_drawing)
    db.session.commit()

    return jsonify({'message': 'Drawing created successfully'}), 201

@app.route('/drawings/<int:drawing_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_drawing(drawing_id):
    drawing = Drawing.query.get_or_404(drawing_id)

    if request.method == 'GET':
        return jsonify({
            'id': drawing.id,
            'shape_type': drawing.shape_type,
            'coordinates': drawing.coordinates,
            'dimensions': drawing.dimensions,
            'annotations': drawing.annotations
        })

    elif request.method == 'PUT':
        data = request.json

        drawing.shape_type = data.get('shape_type', drawing.shape_type)
        drawing.coordinates = data.get('coordinates', drawing.coordinates)
        drawing.dimensions = data.get('dimensions', drawing.dimensions)
        drawing.annotations = data.get('annotations', drawing.annotations)

        db.session.commit()

        return jsonify({'message': 'Drawing updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(drawing)
        db.session.commit()

        return jsonify({'message': 'Drawing deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
