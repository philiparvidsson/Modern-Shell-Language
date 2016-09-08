#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import sys

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

conf = None

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

AUTHORS = [
    'Philip Arvidsson <contact@philiparvidsson.com>',
    'Mattias Eriksson <pls enter mail>'
]

VERSION = '0.1'

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Config(object):
    def __init__(self, opts):
        self.num_errors = 0

        self.options = {
            '--max-errors': '10',
            # FIXME: Pick default target depending on platform. When we have bash, heh.
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

def error(s, t=None):
    if t:
        print conf.srcfile + '({}:{})'.format(t.row, t.column) + ':', s
    else:
        print conf.srcfile + ':', s

    conf.num_errors += 1
    if conf.num_errors > int(conf.option('--max-errors')):
        print 'error: too many errors, aborting...'
        sys.exit()

def fatal(s, t=None):
    print '!!fatal error!!'
    if t:
        print conf.srcfile + '({}:{})'.format(t.row, t.column) + ':', s
    else:
        print conf.srcfile + ':', s
    sys.exit()

def warning(s, t=None):
    if conf.flag('--warn-err'):
        error(s, t)
        return

    if conf.flag('--no-warn'):
        return

    print '[warning]', s
    if t:
        print conf.srcfile + '({}:{})'.format(t.row, t.column) + ':', s
    else:
        print conf.srcfile + ':', s
