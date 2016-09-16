/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Outputs a line of text to the standard output.
 *
 * @param text The text to output.
 */
function print() {
    /* Windows */
    raw('set r=%1'                                         , 'bat')
    raw('set s='                                           , 'bat')
    raw(':__print'                                         , 'bat')
    raw('if "%~4" equ "" (goto __print_done)'              , 'bat')
    raw('set "s=%s%%~4"'                                   , 'bat')
    raw('shift'                                            , 'bat')
    raw('goto __print'                                     , 'bat')
    raw(':__print_done'                                    , 'bat')
    raw('if "%s%" neq "" (echo|set /p="%s%") else (echo.)' , 'bat')
    raw('set %r%=0'                                        , 'bat')
}

/**
 * Outputs a line of text to the standard output.
 *
 * @param text The text to output.
 */
function println() {
    /* Windows */
    raw('set r=%1'                                , 'bat')
    raw('set s='                                  , 'bat')
    raw(':__println'                              , 'bat')
    raw('if "%~4" equ "" (goto __println_done)'   , 'bat')
    raw('set "s=%s%%~4 "'                         , 'bat')
    raw('shift'                                   , 'bat')
    raw('goto __println'                          , 'bat')
    raw(':__println_done'                         , 'bat')
    raw('if "%s%" neq "" (echo %s%) else (echo.)' , 'bat')
    raw('set %r%=0'                               , 'bat')
}

/**
 * Reads a line of text from the user. Optionally displays a prompt.
 *
 * @param text The prompt text to display.
 *
 * @returns The line of text entered by the user.
 */
function userinput() {
    /* Windows */
    raw('set r=%1'                               , 'bat')
    raw('set s='                                 , 'bat')
    raw(':__readline_next'                       , 'bat')
    raw('if "%~4" equ "" (goto __readline_done)' , 'bat')
    raw('set "s=%s%%~4 "'                        , 'bat')
    raw('shift'                                  , 'bat')
    raw('goto __readline_next'                   , 'bat')
    raw(':__readline_done'                       , 'bat')
    raw('set /p t=%s%'                           , 'bat')
    raw('set %r%=%t%'                            , 'bat')
    raw('goto :eof'                              , 'bat')
}
