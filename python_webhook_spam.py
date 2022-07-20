import time; import requests;
value = int(0)
print("renember this is a webhook spammer not a dm spammer")
exits = input("press anything to continue\ntype exit if you want to close this program\n")
if exits : "exit" ; exit()
print("\ntype what you want to spam")
content_ = input() ##getting important info.
print("\n paste webhook link here")
webtoken = input()
##this is a webhook spammer, if u see this thank you for downloading this #gamer4life.
def message(): ##this is message function.
    value = value + int(1)
    print("sent", value, "times")
    payload = {
        'content':content_ 
    }
    requests.post(webtoken, data=payload)
    time.sleep(2) ##without this it would crash.
for i in range(42069): ##how many messages to send :).
    message ##using the function we created.
##thats the end. 