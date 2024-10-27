const express = require("express");
const cors = require("cors");

const app = express();

// Middleware to parse JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// CORS options
const corsOptions = {
    origin: ["http://localhost:5173"],
};
app.use(cors(corsOptions));

// POST request handler
app.post("/info", (req, res) => {
    console.log('POST parameters received are:', req.body);
    res.status(200).send("Data received successfully");
});

// Serve an HTML file if needed (optional)
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Start the server on port 8080
app.listen(8080, () => {
    console.log("Server started on port 8080");
});
