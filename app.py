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

"""
Comments:

1. app.connect() creates a connection between the IB Gateway API and script
2. app.run() is REQUIRED to be called in order to start the connection
3. nextValidId is first overwritten function to get called in the IBApi file
4. Inside nextValidId, the start function is called
5. Most of the request functions are asynchronous, the data does not necessarily get returned immediately
6. To intercept the response from the API, the functions marked with @overwrite catch the response and handle it
"""