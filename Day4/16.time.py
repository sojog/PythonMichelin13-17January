import time
import random

# Seconds from 1 January 1970
print(time.time())

# Stop for 1-5 seconds
wait_for_sec = random.randint(1, 5)
print("We wait for ", wait_for_sec)
time.sleep(wait_for_sec)

print(time.time())