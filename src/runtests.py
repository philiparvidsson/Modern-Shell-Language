#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import os
import subprocess

OPTS = [
    '--no-logo',
    '--no-optim',
]

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == '__main__':
    d = os.getcwd()
    a = os.path.join(d, 'main.py')

    os.chdir('../tests')

    print 'compiling and running tests...'
    print

    d = os.getcwd()
    for f in os.listdir(d):
        if not f.endswith('.js'):
            continue

        f2 = f
        f = os.path.join(d, f)

        args = ['python', a]
        args.extend(OPTS)
        args.append(f)

        print 'running test:', f2
        subprocess.call(args)
        r = subprocess.call(f + '.bat')
        if r != 0:
            print
            print 'a test failed. please fix the issue and run the tests again'
            break

        os.remove(f + '.bat')
