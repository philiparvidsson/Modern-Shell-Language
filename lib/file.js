function File(name, mode) {
    this = []

    /*---------------------------------------
     * FIELDS
     *-------------------------------------*/

    this.name = name

    this._mode = mode

    /*---------------------------------------
     * METHODS
     *-------------------------------------*/

    this.read = function () {
        return 'contents of some file'
    }

    this.write = function (text) {
        if (this._mode == 'a') {
            console.log('appending', text, 'to', this.name)
        }
        else if (this._mode == 'w') {
            console.log('writing', text, 'to', this.name)
        }
    }

    return this
}

/**
 * Deletes a file if it exists.
 *
 * @param path The path and file name of the file to delete.
 *
 * @returns True if the specified existed and was deleted.
 */
File.delete = function (path) {
    /* Windows */
    raw('if exist "%~4" (', 'bat')
    raw('del "%~4"'       , 'bat')
    raw('set %~1=1'       , 'bat')
    raw(') else ('        , 'bat')
    raw('set %~1=0'       , 'bat')
    raw(')'               , 'bat')
    raw('goto :eof'       , 'bat')
}

/**
 * Checks whether a file exists.
 *
 * @param path The path and file name of the file to look for.
 *
 * @returns True if a file with the specified name exists.
 */
File.exists = function (path) {
    /* Windows */
    raw('if exist "%~4" (set %~1=1) else (set %~1=0)', 'bat')
    raw('goto :eof'                                  , 'bat')
}
