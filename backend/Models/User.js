const {Schema, model} = require("mongoose")

const User = new Schema({
    email: {type: String, required: true},
    name: {type: String, required: true},
    password: {type: String, required: true},
    create_date: {type: Date, required: true}
})

module.exports = model('User', User)