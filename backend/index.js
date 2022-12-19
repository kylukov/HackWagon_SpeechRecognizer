const express = require('express');
const PORT = process.env.PORT || 5000;
const app = express();
const authRouter = require('./Routers/authrout')
const storageRouter = require('./Routers/storagerout')
const mongoose = require('mongoose')
const path = require("path")
const cors = require('cors');
const authmw = require('./Middlewares/authmw');

app.use(cors())
app.use(express.json())
app.use('/api/user', authRouter)
// app.use('/api/storage', [authmw], storageRouter)
app.use('/api/storage', storageRouter)
global.appRoot = path.resolve(__dirname);



const start = async () => {
    try {
        await mongoose.connect('mongodb://localhost:27017/hackwagon')
        app.listen(PORT, () => console.log('Server had been started! Port: ' + PORT))
    } catch(e) {
        console.log(e)
    }
}

start()