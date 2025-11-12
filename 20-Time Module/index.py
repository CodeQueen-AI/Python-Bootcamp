#time.sleep() – Pause/Delay
import time
print("Start")
time.sleep(2)  
print("End")

#time.time() – Epoch Time
import time
current_time = time.time()
print("Current time in seconds since epoch:", current_time)

#time.ctime() – Human-Readable Time
import time
readable_time = time.ctime()
print("Current readable time:", readable_time)

#time.localtime() – Tuple Format
import time
t = time.localtime()
print("Year:", t.tm_year)
print("Month:", t.tm_mon)
print("Day:", t.tm_mday)
print("Hour:", t.tm_hour)
print("Minute:", t.tm_min)
print("Second:", t.tm_sec)

#time.strftime() – Custom Format
import time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Current Time:", formatted_time)

#Loop + Delay
import time
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(0.5)
