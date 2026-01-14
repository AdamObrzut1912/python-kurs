import datetime
import time
import random


start_time = time.perf_counter()
time.sleep(random.randint(1,5))
end_time = time.perf_counter()
result = end_time-start_time
print(f"czas nad projektem to {result}")

if result > 3:
    print("poświęcono dużo czasu")
else:
    print("krótki czas pracy")


