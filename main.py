import asyncio
import sys
import os
import hashlib


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{sys.stdout.buffer.write(stdout)}')
    if stderr:
        print(f'[stderr]\n{sys.stdout.buffer.write(stderr)}')


#    print(datetime.now())

string = 'git clone --depth=1 --branch=master\
 https://gitea.radium.group/radium/project-configuration.git '


async def main():
    await asyncio.gather(
        run(string + 'temp1'),
        run(string + 'temp2'),
        run(string + 'temp3'))


# print(datetime.now())
asyncio.run(main())

counter = 0


def sha256(element: str) -> int:
    if os.path.isfile(element):
        out = ''
        print('\nNEW')
        with open(element, 'r') as e:
            line = e.read()
            print('\n', line)
            out = hashlib.sha256(line.encode('utf-8')).hexdigest()
        print(out)
    else:
        #        print(element)
        for el in os.listdir(element):
            if (el != '.git'):
                el = element + "/" + el
                sha256(el)


# get list of dir and files
dirs = os.listdir('.')

for dir in dirs:
    if 'temp' in dir:
        sha256(dir)
