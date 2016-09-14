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
