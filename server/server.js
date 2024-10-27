const express = require("express");
const cors = require("cors");
const fs = require("fs");
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
    try{
        console.log('POST parameters received are:', req.body);
        let data = JSON.stringify(req.body, null, 2);
        fs.appendFile('./file.txt', data, (err) => {
            if (err) throw err;
            console.log('Data written to file');
        });
        res.status(200).send("Data Recieved");
    } catch (error) {
        console.error('Error handling POST request:', error);
        res.status(500).send("Internal Server Error");
    }
    }); 

// Serve an HTML file if needed (optional)
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Start the server on port 8080
app.listen(8080, () => {
    console.log("Server started on port 8080");
});
