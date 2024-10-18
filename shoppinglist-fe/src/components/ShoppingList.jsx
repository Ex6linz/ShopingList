import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Button, List, ListItem, Box } from '@mui/material';
import ShoppingItem from './ShoppingItem';

function ShoppingList() {
    const [items, setItems] = useState([]);
    const [newItem, setNewItem] = useState({ name: '', quantity: 1 });

    useEffect(() => {
        fetchItems();
    }, []);

    const fetchItems = async () => {
        try {
            const response = await axios.get('http://localhost:30500/shopping-list');
            setItems(response.data);
        } catch (error) {
            console.error('Error fetching shopping list', error);
        }
    };

    const handleAddItem = async () => {
        try {
            const response = await axios.post('http://localhost:30500/shopping-list', newItem);
            setItems([...items, response.data.item]);
            setNewItem({ name: '', quantity: 1 });
        } catch (error) {
            console.error('Error adding item', error);
        }
    };

    const handleDeleteItem = async (id) => {
        try {
            await axios.delete(`http://localhost:30500/shopping-list/${id}`);
            setItems(items.filter(item => item.id !== id));
        } catch (error) {
            console.error('Error deleting item', error);
        }
    };

    return (
        <Box sx={{ mt: 3 }}>
            <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
                <TextField
                    label="Item name"
                    value={newItem.name}
                    onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
                />
                <TextField
                    label="Quantity"
                    type="number"
                    value={newItem.quantity}
                    onChange={(e) => setNewItem({ ...newItem, quantity: e.target.value })}
                />
                <Button variant="contained" onClick={handleAddItem}>
                    Add Item
                </Button>
            </Box>
            <List>
                {items.map(item => (
                    <ShoppingItem
                        key={item.id}
                        item={item}
                        onDelete={() => handleDeleteItem(item.id)}
                    />
                ))}
            </List>
        </Box>
    );
}

export default ShoppingList;