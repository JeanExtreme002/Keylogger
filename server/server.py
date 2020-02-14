from app import server
import os

if __name__ == "__main__":

    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 5000))

    server.run(host = host, port = port, debug = False)

