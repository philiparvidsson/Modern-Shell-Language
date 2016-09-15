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

    this.write = function (s) {
        if (this._mode == 'a') {
            console.log('appending', s, 'to', this.name)
        }
        else if (this._mode == 'w') {
            console.log('writing', s, 'to', this.name)
        }
    }

    return this
}

File.delete = function (s) {
    /* Windows */
    raw('if exist "%~4" (', 'bat')
    raw('del "%~4"'       , 'bat')
    raw('set %~1=1'       , 'bat')
    raw(') else ('        , 'bat')
    raw('set %~1=0'       , 'bat')
    raw(')'               , 'bat')
    raw('goto :eof'       , 'bat')
}

File.exists = function (s) {
    /* Windows */
    raw('if exist "%~4" (set %~1=1) else (set %~1=0)', 'bat')
    raw('goto :eof'                                  , 'bat')
}
