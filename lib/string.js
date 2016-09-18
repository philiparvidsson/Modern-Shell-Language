/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Provides a string object for performing string manipulation operations.
 *
 * @param s The initial string contents.
 *
 * @returns A string object.
 */
function string(s) {
    s2 = (s == undefined) ? '' : s

    this = []

    /*---------------------------------------
     * FIELDS
     *-------------------------------------*/

    this.__string__ = s2

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

    /**
     * Retrieves the character at the specified index
     *
     * @param i The index of the character to retrieve.
     *
     * @returns The character at the specified index.
     */
    this.charAt = function (i) {
        return substr(this.__string__, i, 1)
    }

    /**
     * Concatenates one string with another. This function returns a copy and
     * does not mutate the original string.
     *
     * @param s The string to append to the end. Can be a string or a string
     *          object.
     *
     * @returns A string object.
     */
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

    /**
     * Returns the indext of the specified substring in this string, starting at
     * the specified index.
     *
     * @param s The string to look for.
     * @param i Optional. The index to start at.
     *
     * @returns The index of the substring in the string, or -1 if it could not
     *          be found.
     */
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

    /**
     * Calculates the length of the string and returns it.
     *
     * @returns THe length of the string, in number of characters.
     */
    this.length = function () {
        return length(this.__string__)
    }

    /**
     * Retrieves the native string that the string object wraps.
     *
     * @returns The native string that the string object wraps.
     */
    this.str = function () {
        return this.__string__
    }

    /**
     * Retrieves a substring of the string, spanning n characters and starting
     * index i.
     *
     * @param i The starting index of the substring
     * @param n The length of the substring to retrieve.
     *
     * @returns A string object containing the substring.
     */
    this.substr = function (i, n) {
        return string(substr(this.__string__, i, n))
    }

    return this
}
