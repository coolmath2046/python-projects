import time
ops = 0
runtime = 5
starttime = time.process_time()
while True:
    ops += 1
    if time.process_time() - starttime > runtime:
        break

print('Your speed is ' + str(ops/runtime) + ' operations per second.')
