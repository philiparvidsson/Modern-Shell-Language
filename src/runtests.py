#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import os
import subprocess
import time

# Options used when compiling tests
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

    passing = []
    failing = []

    start_time = time.time()

    d = os.getcwd()
    for f in os.listdir(d):
        if not f.endswith('.js'):
            continue

        f2 = f[:-3]
        f = os.path.join(d, f)

        args = ['python', a]
        args.extend(OPTS)
        args.append(f)

        print 'running test:', f2
        if os.path.isfile(f + '.bat'):
            os.remove(f + '.bat')

        subprocess.call(args)

        if os.path.isfile(f + '.bat'):
            r = subprocess.call([f + '.bat', 'abc', '123'])
            if r != 0:
                failing.append(f2)
            else:
                passing.append(f2)
                os.remove(f + '.bat')
        else:
            failing.append(f2)
            print 'test {} failed to compile'.format(f2)

    end_time = time.time()
    secs = end_time - start_time

    print
    print 'ran {} tests in {:.2f} seconds'.format(len(passing)+len(failing), secs)
    print
    print 'results:'
    print

    if passing:
        print 'passing tests ({}):'.format(len(passing))
        print ' '.join(passing)
        print

    if failing:
        print 'failing tests ({})'.format(len(failing))
        print ' '.join(failing)
