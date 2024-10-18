import React from 'react';
import { Container, Typography } from '@mui/material';
import ShoppingList from './components/ShoppingList';

function App() {
    return (
        <Container>
            <Typography variant="h3" component="h1" gutterBottom>
                Shopping List
            </Typography>
            <ShoppingList />
        </Container>
    );
}

export default App;