import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Pinapayagan ang mga requests mula sa kahit anong network/device

# Database Configuration (SQLite)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------------------------------------------------
# Database Models
# -------------------------------------------------------------------

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.String(50), primary_key=True)
    user_role = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    turnover_location = db.Column(db.String(150), nullable=True)
    secret_question = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "userRole": self.user_role,
            "title": self.title,
            "type": self.type,
            "category": self.category,
            "location": self.location,
            "date": self.date,
            "description": self.description,
            "contact": self.contact,
            "turnoverLocation": self.turnover_location,
            "secretQuestion": self.secret_question
        }

class Claim(db.Model):
    __tablename__ = 'claims'
    
    claim_id = db.Column(db.String(50), primary_key=True)
    item_id = db.Column(db.String(50), db.ForeignKey('items.id'), nullable=False)
    item_title = db.Column(db.String(150), nullable=False)
    claimant_name = db.Column(db.String(100), nullable=False)
    claimant_contact = db.Column(db.String(100), nullable=False)
    claim_answer = db.Column(db.Text, nullable=True)
    submitted_at = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "claimId": self.claim_id,
            "itemId": self.item_id,
            "itemTitle": self.item_title,
            "claimantName": self.claimant_name,
            "claimantContact": self.claimant_contact,
            "claimAnswer": self.claim_answer,
            "submittedAt": self.submitted_at
        }

# Automatic DB Table Creation
with app.app_context():
    db.create_all()

# -------------------------------------------------------------------
# Routes & API Endpoints
# -------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.order_by(Item.created_at.desc()).all()
    return jsonify([item.to_dict() for item in items]), 200

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    new_item = Item(
        id=data.get('id'),
        user_role=data.get('userRole'),
        title=data.get('title'),
        type=data.get('type'),
        category=data.get('category'),
        location=data.get('location'),
        date=data.get('date'),
        description=data.get('description'),
        contact=data.get('contact'),
        turnover_location=data.get('turnoverLocation'),
        secret_question=data.get('secretQuestion')
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item registered successfully", "item": new_item.to_dict()}), 201

@app.route('/api/claims', methods=['GET'])
def get_claims():
    claims = Claim.query.all()
    return jsonify([claim.to_dict() for claim in claims]), 200

@app.route('/api/claims', methods=['POST'])
def create_claim():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    new_claim = Claim(
        claim_id=data.get('claimId'),
        item_id=data.get('itemId'),
        item_title=data.get('itemTitle'),
        claimant_name=data.get('claimantName'),
        claimantContact=data.get('claimantContact'),
        claim_answer=data.get('claimAnswer'),
        submitted_at=data.get('submittedAt')
    )
    db.session.add(new_claim)
    db.session.commit()
    return jsonify({"message": "Claim submitted successfully", "claim": new_claim.to_dict()}), 201

@app.route('/api/claims/<claim_id>/approve', methods=['POST'])
def approve_claim(claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify({"error": "Claim not found"}), 404

    item = Item.query.get(claim.item_id)
    if item:
        db.session.delete(item)
        
    Claim.query.filter_by(item_id=claim.item_id).delete()
    db.session.commit()
    return jsonify({"message": "Claim approved"}), 200

@app.route('/api/claims/<claim_id>/reject', methods=['DELETE'])
def reject_claim(claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify({"error": "Claim not found"}), 404

    db.session.delete(claim)
    db.session.commit()
    return jsonify({"message": "Claim rejected"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
