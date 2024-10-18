import React from 'react';
import { ListItem, IconButton, Typography } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

function ShoppingItem({ item, onDelete }) {
    return (
        <ListItem
            secondaryAction={
                <IconButton edge="end" aria-label="delete" onClick={onDelete}>
                    <DeleteIcon />
                </IconButton>
            }
        >
            <Typography>
                {item.name} - Quantity: {item.quantity}
            </Typography>
        </ListItem>
    );
}

export default ShoppingItem;