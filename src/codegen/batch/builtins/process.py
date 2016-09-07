#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.exit={0}.exit
goto {0}.exit_
:{0}.exit
goto :eof
:{0}.exit_

set {0}.exitCode=0
''')

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

var = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def emit_code(p):
    global var
    if not var:
        var = p.tempvar('string')
        var.name += '_process'
        p.emit(CODE.format(var.name), 'decl')

    p.scope.decl_var('process', 'variable').name = var.name
