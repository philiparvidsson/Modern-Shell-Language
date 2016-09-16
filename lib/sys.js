/*----------------------------------------------------------
 * GLOBALS
 *--------------------------------------------------------*/

/**
 * Specifies the exit code to use if no argument is provided to the exit()
 * function.
 */
__exitCode = 0

/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Returns the number of arguments passed to the program.
 *
 * @returns The number of arguments passed to the program.
 */
function argc() {
    /* Windows */
    // We have to rely somewhat on intricate details in the batch code
    // generation here.
    raw('set %~1=!__argv.length!', 'bat')
    raw('goto :eof'              , 'bat')
}

/**
 * Retrieves the program argument associated with the specified index.
 *
 * @param i The index of the program argument to retrieve.
 *
 * @returns The program argument associated with the specified index.
 */
function argv(i) {
    /* Windows */
    // We have to rely somewhat on intricate details in the batch code
    // generation here.
    raw('set %~1=!__argv.%~4!', 'bat')
    raw('goto :eof'           , 'bat')
}

/**
 * Starts a process by executing the specified executable with the specified
 * arguments. Waits for the process to exit before returning.
 *
 * @param exeName The name of the executable to start.
 * @param args The arguments to pass to the executable.
 */
function exec(exeName, args) {
    /* Windows */
    raw('set %~1=0'                           , 'bat')
    raw('set _proc="%~4"'                     , 'bat')
    raw(':__process_exec_rearg'               , 'bat')
    raw('if "%~5" neq "" ('                   , 'bat')
    raw('set __args=!__args! "%~5"'           , 'bat')
    raw('shift'                               , 'bat')
    raw('goto :__process_exec_rearg'          , 'bat')
    raw(')'                                   , 'bat')
    raw('if not defined __args ('             , 'bat')
    raw('start /min cmd /c "!_proc!"'         , 'bat')
    raw(') else ('                            , 'bat')
    raw('start /min cmd /c "!_proc!!__args!")', 'bat')
    raw(')'                                   , 'bat')
}

/**
 * Starts a process by executing the specified executable with the specified
 * arguments. Does not wait for the process to exit before returning.
 *
 * @param exeName The name of the executable to start.
 * @param args    The arguments to pass to the executable.
 */
function execSync(exeName, args) {

}

/**
 * Exits the current process with the specified exit code, or process.exitCode
 * if no exit code is specified.
 *
 * @param code The exit code to use.
 */
function exit(code) {
    /* Windows */
    raw('set __exitCode=%~4'          , 'bat')
    raw(':__process_unwind_stack'     , 'bat')
    raw('set x=%0'                    , 'bat')
    raw('set x=!x:~0,1!'              , 'bat')
    raw('if "!x!"==":" ('             , 'bat')
    raw('(goto) 2>nul & ('            , 'bat')
    raw('set __exitCode=%__exitCode%' , 'bat')
    raw('goto :__process_unwind_stack', 'bat')
    raw(')'                           , 'bat')
    raw(') else ('                    , 'bat')
    raw('exit /b !__exitCode!'        , 'bat')
    raw(')'                           , 'bat')
}

/**
 * Sleeps the current process by waiting the specified number of seconds before
 * returning.
 *
 * @param seconds The number of seconds to wait before returning.
 */
function sleep(seconds) {
    /* Windows */
    raw('choice /T %~4 /C X /D X /N >nul', 'bat')
}
