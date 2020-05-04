import requests

# this require requests module to be installed
# pip3 install requests
import time

api_url = "http://localhost:5005/escritorio/"
sleep_time = 5

def turn_light_on():
    print("on")

def turn_light_off():
        print("off")

def run():
    previous_state = False
    while True:
        state = requests.get(api_url).json()
        if (state['lights'] == True and previous_state == False):
            turn_light_on()
            previous_state = True
        if (state['lights'] == False and previous_state == True):
            turn_light_off()
            previous_state = False
        time.sleep(sleep_time)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        pass
