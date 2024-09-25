import asyncio

async def async_write_to_file(filename, data, duration):
    # pass
    print(f"{filename}...")
    await asyncio.sleep(duration)
    with open(filename, 'w') as f:
        f.write(data)
async def run_async_tasks(primes):
    # pas
    filenames = ["files1.txt", "files2.txt", "files3.txt"]
    chunk_size = len(primes)//len(filenames)
    chunks = [primes[i:i + chunk_size] for i in range(0, len(primes), chunk_size)]

    # Create tasks to write chunks to files
    tasks = []
    for i in range(len(filenames)):
        filename = filenames[i]
        data = "\n".join(map(str, chunks[i]))
        task = asyncio.create_task(async_write_to_file(filename, data, 1))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print("Async task completed.")
