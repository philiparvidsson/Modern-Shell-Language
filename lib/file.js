/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Provides a file object for delete, reading from and writing to files.
 *
 * @param name      The name of the file.
 * @param writeMode The file access mode. Specify 'w' for overwrite mode or 'a'
 *                  for append mode.
 */
function file(name, writeMode) {
    this = []

    /*---------------------------------------
     * FIELDS
     *-------------------------------------*/

    this._writeMode = writeMode

    this.name = name

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

    /**
     * Reads the contents of the file.
     *
     * @returns The contents of the file.
     */
    this.read = function () {
        return read(this.name)
    }

    /**
     * Writes text to the file.
     *
     * @param text The text to write to the file.
     */
    this.write = function (text) {
             if (this._writeMode == 'a') append(this.name, text)
        else if (this._writeMode == 'w') write (this.name, text)
    }

    return this
}
