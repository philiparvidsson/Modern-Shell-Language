function File(name, writeMode) {
    this = []

    /*---------------------------------------
     * FIELDS
     *-------------------------------------*/

    this.name = name

    this._writeMode = writeMode

    /*---------------------------------------
     * FUNCTIONS
     *-------------------------------------*/

    append = function (_1, _2) {
        /* Windows */
        raw('echo %~5>>"%~4"', 'bat')
    }

    delete = function (_1) {
        /* Windows */
        raw('if exist "%~4" (', 'bat')
        raw('del "%~4"'       , 'bat')
        raw('set %~1=1'       , 'bat')
        raw(') else ('        , 'bat')
        raw('set %~1=0'       , 'bat')
        raw(')'               , 'bat')
        raw('goto :eof'       , 'bat')
    }

    exists = function (_1) {
        /* Windows */
        raw('if exist "%~4" (set %~1=1) else (set %~1=0)', 'bat')
        raw('goto :eof'                                  , 'bat')
    }

    read = function (_1) {
        /* Windows */
        raw('set lf=^'                                                        , 'bat')
        raw(''                                                                , 'bat')
        raw(''                                                                , 'bat')
        raw('set "r="'                                                        , 'bat')
        raw('for /f "usebackq delims=" %%s in ("%~4") do (set "r=!r!%%s!lf!")', 'bat')
        raw('set %1=%r%'                                                      , 'bat')
        raw('goto :eof'                                                       , 'bat')
    }

    write = function (_1, _2) {
        /* Windows */
        raw('echo %~5>"%~4"', 'bat')
    }

    /*---------------------------------------
     * METHODS
     *-------------------------------------*/

    /**
     * Deletes the file if it exists.
     *
     * @returns True if the file existed and was deleted.
     */
    this.delete = function () {
        return delete(this.name)
    }

    /**
     * Checks whether the file exists.
     *
     * @returns True if the file exists.
     */
    this.exists = function () {
        return exists(this.name)
    }

    this.read = function () {
        return read(this.name)
    }

    this.write = function (text) {
             if (this._writeMode == 'a') append(this.name, text)
        else if (this._writeMode == 'w') write (this.name, text)
    }

    return this
}
