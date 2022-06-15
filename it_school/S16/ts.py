import time
# de la timestamp
some_ts = 1655225061.9471025

ts_struct = time.gmtime(some_ts)

print(ts_struct.tm_hour)
print(ts_struct.tm_min)

print(time.strftime("%m/%d/%Y"))