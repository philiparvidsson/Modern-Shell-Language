/**
 * Outputs a line of text to the standard output.
 *
 * @param text The text to output.
 */
function println() {
    /* Windows */
    raw('set r=%1'                                , 'bat')
    raw('set s='                                  , 'bat')
    raw(':{0}_echo'                               , 'bat')
    raw('if "%~4" equ "" (goto :{0}_done)'        , 'bat')
    raw('set "s=%s%%~4 "'                         , 'bat')
    raw('shift'                                   , 'bat')
    raw('goto :{0}_echo'                          , 'bat')
    raw(':{0}_done'                               , 'bat')
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
function readline() {
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
