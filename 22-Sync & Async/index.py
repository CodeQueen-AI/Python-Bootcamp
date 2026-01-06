import time
import asyncio

# Synchronous: Tasks execute one after another, each waits for the previous to finish
def sync_task1():
    time.sleep(2)  # simulate delay of 2 seconds
    print("Synchronous Task 1 done")

def sync_task2():
    time.sleep(2)
    print("Synchronous Task 2 done")

print("Synchronous Execution Starts:")
sync_task1() 
sync_task2() 

# Asynchronous: Tasks can run at the same time without waiting for each other
async def async_task1():
    await asyncio.sleep(2)  # simulate delay
    print("Asynchronous Task 1 done")

async def async_task2():
    await asyncio.sleep(2)
    print("Asynchronous Task 2 done")

async def main():
    # asyncio.gather runs multiple async tasks concurrently
    await asyncio.gather(async_task1(), async_task2())

print("Asynchronous Execution Starts:")
asyncio.run(main())  # total time ≈ 2 seconds
print("All asynchronous tasks completed\n")