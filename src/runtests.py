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

    passing = []
    failing = []

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
            failing.append(f2)
        else:
            passing.append(f2)
            os.remove(f + '.bat')

    print
    print 'ran {} tests'.format(len(passing)+len(failing))
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
