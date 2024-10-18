import unittest
from flask import Flask
from routes.shopping_list_routes import shopping_list_bp
from utils.db import Base, engine, get_db
from sqlalchemy.orm import sessionmaker
from models.shopping_item import ShoppingItem


class ShoppingListTestCase(unittest.TestCase):
    def setUp(self):

        self.app = Flask(__name__)
        self.app.register_blueprint(shopping_list_bp)
        self.client = self.app.test_client()


        Base.metadata.create_all(bind=engine)
        self.db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

    def tearDown(self):

        Base.metadata.drop_all(bind=engine)
        self.db.close()

    def test_add_shopping_item(self):
        response = self.client.post('/shopping-list', json={
            'name': 'Milk',
            'quantity': 2
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Item added successfully', response.get_data(as_text=True))

    def test_get_shopping_list(self):

        item = ShoppingItem(name='Bread', quantity=1)
        self.db.add(item)
        self.db.commit()

        response = self.client.get('/shopping-list')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bread', response.get_data(as_text=True))

    def test_update_shopping_item(self):

        item = ShoppingItem(name='Eggs', quantity=12)
        self.db.add(item)
        self.db.commit()

        response = self.client.put(f'/shopping-list/{item.id}', json={
            'quantity': 6
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item updated successfully', response.get_data(as_text=True))

    def test_delete_shopping_item(self):

        item = ShoppingItem(name='Butter', quantity=1)
        self.db.add(item)
        self.db.commit()

        response = self.client.delete(f'/shopping-list/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item deleted successfully', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()