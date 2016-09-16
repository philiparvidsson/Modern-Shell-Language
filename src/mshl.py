#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import os
import sys

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

conf = None
num_errors = 0

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

AUTHORS = [
    'Philip Arvidsson <contact@philiparvidsson.com>',
]

VERSION = '0.42'

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Config(object):
    def __init__(self, opts):
        self.include_dirs = [ os.path.join(os.getcwd(), '../lib') ]

        self.options = {
            '--max-errors': '10',
            # FIXME: Pick default target depending on platform.
            '--target': 'bat'
        }

        for opt in opts:
            i = opt.find('=')
            if i >= 0:
                key   = opt[:i]
                value = opt[i+1:]
            else:
                key   = opt
                value = True

            if key == '--inc-dir':
                self.include_dirs.append(value)
                continue

            self.options[key] = value

    def flag(self, s):
        return s in self.options

    def option(self, s):
        if s not in self.options:
            return False

        return self.options[s]

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def find_include_file(s):
    if os.path.isfile(s):
        return s

    for path in conf.include_dirs:
        t = os.path.join(path, s)
        if os.path.isfile(t):
            return t

def trace(*args):
    if not args:
        print
    else:
        print ' '.join(args)

def error(s, t=None):
    if t:
        trace('error in ' + '<file>' + '({}:{})'.format(t.row, t.column) + ':', s)
    else:
        trace('error in ' + '<file>' + ':', s)

    global num_errors
    num_errors += 1
    if num_errors > int(conf.option('--max-errors')):
        fatal('too many errors, aborting...')

def fatal(s, t=None):
    if t:
        trace('fatal error in ' + '<file>' + '({}:{})'.format(t.row, t.column) + ':', s)
    else:
        trace('fatal error in ' + '<file>' + ':', s)

    sys.exit()

def warning(s, t=None):
    if conf.flag('--warn-err'):
        error(s, t)
        return

    if conf.flag('--no-warn'):
        return

    if t:
        trace('warning in ' + '<file>' + '({}:{})'.format(t.row, t.column) + ':', s)
    else:
        trace('warning in ' + '<file>' + ':', s)
