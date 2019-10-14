import asyncio
import argparse
from asyncio import Queue
import aiohttp
import json
import re

storage = None

async def get_doc(name, session):
    async with session.get(
        'https://en.wikipedia.org/w/api.php?'
        'format=json&action=query&prop=extracts&exintro&explaintext&redirects=1'
        '&titles={}'.format(name),
        timeout=60 * 60
    ) as response:
        return await response.text()

async def process(queue, session):
    while True:
        name, docid = await queue.get()
        summary = ' '.join(name.split('_'))
        # try:
        #     doc = await get_doc(name, session)
        #     doc = json.loads(doc)
        #     pages = doc["query"]["pages"]
        #     key = list(pages.keys())[0]
        #     summary = re.sub('\s+', ' ', pages[key]["extract"].strip())
        # except Exception as e:
            # print(f'Failed with error: {e}, {doc}, {name}')
        # finally:
        queue.task_done()
        storage.write(docid + '\t' + summary + '\n')
        storage.flush()

async def run(loop, task_queue):
    async with aiohttp.ClientSession(loop=loop) as session:
        workers = [asyncio.Task(process(task_queue, session), loop=loop) for i in range(5)]
        await task_queue.join()
        for w in workers:
            w.cancel()

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest='input')
    parser.add_argument("--output", dest='output')
    return parser.parse_args()

def main():
    global storage
    args = _parse_args()
    task_queue = Queue()
    storage = open(args.output, 'w')

    empty = set()
    with open('/Users/asntr/Projects/university/course_work/end2end_neural_el/data/entities/empty.list', 'r') as src:
        for line in src:
            empty.add(line.strip())

    with open(args.input, 'r') as src:
        for line in src:
            [docid, name] = line.strip().split()
            if docid in empty:
                task_queue.put_nowait((name, docid))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop, task_queue))
    storage.close()

if __name__ == '__main__':
    main()
