// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/myapp', { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/api/data', async (req, res) => {
  // Fetch data from MongoDB and send it as a response
});

app.listen(5000, () => console.log('Server is running on port 5000'));