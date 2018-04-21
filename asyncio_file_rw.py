import asyncio
import concurrent.futures
# Class which performs asynchronous file read and write operations using async.Queue
class AsyncReadWrite():
    def __init__(self, rf, wf):
        self.queue = asyncio.Queue()
        try:
            self.rf = open(rf)
            self.wf = open(wf, "w")
        except IOError:
            raise
    
    # Coroutine to read content asynchronously from a file
    async def file_read(self, loop):
        while True:
            print("read")
            line = await loop.run_in_executor(None, self.rf.readline)
            if line == "":
                await self.queue.put(line)
                break
            await self.queue.put(line)
            
    # Coroutine to write content asynchronously into a file
    async def file_write(self, loop):
        while True:
            print("write")
            line = await self.queue.get()
            if line == "":
                return
            else:
                await loop.run_in_executor(None, self.wf.write, line)
            
    def run(self):
        loop = asyncio.get_event_loop()
        tasks = [self.file_write(loop), self.file_read(loop)]
        loop.run_until_complete(asyncio.gather(*tasks))
        
    def close(self):
        self.rf.close()
        self.wf.close()

def main():
    rf = "{}".format(input("Enter name of read file : "))
    wf = "{}".format(input("Enter name of write file : "))
    #rf = "readfile.txt"
    #wf = "writefile.txt"
    try:
        rw = AsyncReadWrite(rf, wf)
    except IOError as error:
        print("Error opening file: {0}".format(error))
    else:
        rw.run()
        rw.close()
        
if __name__ == "__main__":
    main()

    
    
