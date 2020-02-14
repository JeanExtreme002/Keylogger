from terminal import Terminal
import json
import os
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        host = sys.argv[1]
        
    else:
        with open(os.path.join("config","config.json")) as file:
            data = json.loads(file.read())
            host = data.get("host", "localhost")
            
    terminal = Terminal(host = host)
    terminal.run()