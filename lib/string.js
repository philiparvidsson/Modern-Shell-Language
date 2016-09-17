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

    this.__string__ = s

    /*---------------------------------------
     * FUNCTIONS
     *-------------------------------------*/

    concat = function () {
        /* Windows */
        raw('set %~1=%~4%~5', 'bat')
        raw('goto :eof'     , 'bat')
    }

    length = function () {
        /* Windows */
        raw('set n=0'                                                  , 'bat')
        raw('set s=%~4'                                                , 'bat')
        raw(':__string_length'                                         , 'bat')
        raw('if "!s:~%n%!" neq "" (set /a n+=1 & goto __string_length)', 'bat')
        raw('set %~1=!n!'                                              , 'bat')
        raw('goto :eof'                                                , 'bat')
    }

    substr = function () {
        /* Windows */
        raw('set s=%~4'           , 'bat')
        raw('set %~1=!s:~%~5,%~6!', 'bat')
        raw('goto :eof'           , 'bat')
    }

    /*---------------------------------------
     * METHODS
     *-------------------------------------*/

    this.charAt = function (i) {
        x = 1*i
        return substr(this.__string__, x, 1)
    }

    this.concat = function (s) {
        // Concat with nothing - return a copy.
        if (s == undefined) {
            return string(this.__string__)
        }

        // Concat with native string.
        if (s.__string__ == undefined) {
            return string(concat(this.__string__, s))
        }

        // Concat with string object.
        return string(concat(this.__string__, s.__string__))
    }

    this.indexOf = function (s, i) {
        a = (s.__string__ != undefined) ? s.str() : s
        j = (i != undefined) ? 1*i : 0

        m = length(a)
        n = this.length()
        for (k = j; k < n; k++) {
            if (substr(this.__string__, k, m) == a) {
                return k
            }
        }

        return -1
    }

    this.length = function () {
        return length(this.__string__)
    }

    this.str = function () {
        return this.__string__
    }

    this.substr = function (i, n) {
        return string(substr(this.__string__, i, n))
    }

    return this
}
