const {Schema, model} = require("mongoose")

const Storage = new Schema({
    // email: {type: String, required: true},
    name: {type: String, required: true},
    status: {type: Number, required: true, default: 0},
    create_date: {type: Date, required: true}
})

module.exports = model('Storage', Storage)