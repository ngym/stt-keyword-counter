"""This program is a joke program written by Shota Nagayama
https://github.com/ngym
based on
https://github.com/ibm-dev/watson-streaming-stt/

This program counts how many times a keyword appears
in the input English speech. This could help to know
your or someone's habit in speaking English.
"""

import os
import websocket
import base64
import json

from transcribe import get_auth, parse_args, on_error, on_open

FINALS = []
count = 0
keyword = "you know"

def on_message(self, msg):
    """Print and 'say' the keyword if the keyword is found in the
    established result.
    """
    """
    While we are processing any non trivial stream of speech Watson
    will start chunking results into bits of transcripts that it
    considers "final", and start on a new stretch. It's not always
    clear why it does this. However, it means that as we are
    processing text, any time we see a final chunk, we need to save it
    off for later.
    """
    data = json.loads(msg)
    if "results" in data:
        if data["results"][0]["final"]:
            FINALS.append(data)
            count_ = data['results'][0]['alternatives'][0]['transcript'].count(
                keyword)
            for _ in range(count_):
                print("%s!" % keyword)
                os.system('say %s' % keyword)
            global count
            count += count_

def on_close(ws):
    """Upon close, print the complete and final transcript."""
    transcript = "".join([x['results'][0]['alternatives'][0]['transcript']
                          for x in FINALS])
    print(transcript)
    print("%d \"%s\" have been found!!" % (count, keyword))
    
def main():
    # Connect to websocket interfaces
    headers = {}
    userpass = ":".join(get_auth())
    headers["Authorization"] = "Basic " + base64.b64encode(
        userpass.encode()).decode()
    url = ("wss://stream.watsonplatform.net//speech-to-text/api/v1/recognize"
           "?model=en-US_BroadbandModel")

    ws = websocket.WebSocketApp(url,
                                header=headers,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.args = parse_args()
    # This gives control over the WebSocketApp. This is a blocking
    # call, so it won't return until the ws.close() gets called (after
    # 6 seconds in the dedicated thread).
    ws.run_forever()

if __name__ == "__main__":
    main()


    

