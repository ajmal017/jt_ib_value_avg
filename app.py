import threading
import sys
from time import sleep
from lib.ib_api import IBApi

app = IBApi()

def run():
    app.run()

def main():
    try:
        print("Connecting...")
        app.connect("127.0.0.1", 7497, clientId=0)
        api_thread = threading.Thread(target=run, daemon=True)
        api_thread.start()
        sleep(1)

    except KeyboardInterrupt:
        print("Disconnecting on exit")
        app.disconnect()
        sys.exit()

if __name__ == "__main__":
    print(main())