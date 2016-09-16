/*----------------------------------------------------------
 * NAMESPACE
 *--------------------------------------------------------*/

/**
 * Provides process related functionality.
 */
process = function () {}

/*----------------------------------------------------------
 * FIELDS
 *--------------------------------------------------------*/

/**
 * Specifies the exit code to use if no argument is provided to the
 * process.exit() function.
 */
process.exitCode = 0

/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Starts a process by executing the specified executable with the specified
 * arguments. Waits for the process to exit before returning.
 *
 * @param exeName The name of the executable to start.
 * @param args The arguments to pass to the executable.
 */
process.exec = function (exeName, args) {
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
process.execSync = function (exeName, args) {

}

/**
 * Exits the current process with the specified exit code, or process.exitCode
 * if no exit code is specified.
 *
 * @param exitCode The exit code to use.
 */
process.exit = function (exitCode) {

}

/**
 * Sleeps the current process by waiting the specified number of seconds before
 * returning.
 *
 * @param seconds The number of seconds to wait before returning.
 */
process.sleep = function (seconds) {
    /* Windows */
    raw('choice /T %~4 /C X /D X /N >nul', 'bat')
}
