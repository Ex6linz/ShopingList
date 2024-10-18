# Zawartość shopping_list_routes.py
from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from utils.db import get_db
from models.shopping_item import ShoppingItem

shopping_list_bp = Blueprint('shopping_list', __name__)


@shopping_list_bp.route('/shopping-list', methods=['GET'])
def get_shopping_list():
    db: Session = next(get_db())
    items = db.query(ShoppingItem).all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'quantity': item.quantity,
        'purchased': item.purchased
    } for item in items])


@shopping_list_bp.route('/shopping-list', methods=['POST'])
def add_shopping_item():
    db: Session = next(get_db())
    data = request.get_json()
    new_item = ShoppingItem(
        name=data['name'],
        quantity=data['quantity'],
        purchased=data.get('purchased', False)
    )
    db.add(new_item)
    db.commit()
    return jsonify({'message': 'Item added successfully', 'item': {
        'id': new_item.id,
        'name': new_item.name,
        'quantity': new_item.quantity,
        'purchased': new_item.purchased
    }}), 201


@shopping_list_bp.route('/shopping-list/<int:item_id>', methods=['PUT'])
def update_shopping_item(item_id):
    db: Session = next(get_db())
    data = request.get_json()
    item = db.query(ShoppingItem).filter(ShoppingItem.id == item_id).first()
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    item.name = data.get('name', item.name)
    item.quantity = data.get('quantity', item.quantity)
    item.purchased = data.get('purchased', item.purchased)
    db.commit()
    return jsonify({'message': 'Item updated successfully'})


@shopping_list_bp.route('/shopping-list/<int:item_id>', methods=['DELETE'])
def delete_shopping_item(item_id):
    db: Session = next(get_db())
    item = db.query(ShoppingItem).filter(ShoppingItem.id == item_id).first()
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    db.delete(item)
    db.commit()
    return jsonify({'message': 'Item deleted successfully'})