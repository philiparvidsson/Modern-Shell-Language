// FIXME: remove this later
include('stdio.js')

/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

function string(s) {
    this = []

    /*---------------------------------------
     * FIELDS
     *-------------------------------------*/

    this.__value = s

    /*---------------------------------------
     * METHODS
     *-------------------------------------*/

    this.concat = function (s) {
        return string(this.str() + s)
    }

    this.indexOf = function (s) {
        println('String.indexOf not implemented')
        return 0
    }

    this.length = function () {
        println('String.length not implemented')
        return 5
    }

    this.str = function () {
        return this.__value
    }

    this.substr = function () {
        println('String.substr not implemented')
        return 'very long'
    }

    return this
}
