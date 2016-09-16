/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Provides an array object for handling collections of items.
 */
function array() {
    this = []

    /*------------------------------------------------
     * METHODS
     *----------------------------------------------*/

    /**
     * Inserts a new element in the array, at the specified indexx.
     *
     * @param e The element to insert.
     * @param i The index in the array at which to insert the element.
     */
    this.insert = function (e, i) {
        if (i >= this.length) {
            this.push(e)
            return;
        }

        if (i < 0) i = 0

        for (n = this.length; n > i; n--) {
            this[n] = this[n-1]
        }

        this[i] = e
        this.length = 1*this.length + 1
    }

    /**
     * Returns true if the array is empty.
     *
     * @returns True if the array is empty.
     */
    this.isEmpty = function () {
        return (this.length == 0)
    }

    /**
     * Removes the last element from the array and returns it.
     *
     * @returns The last element in the array.
     */
    this.pop = function () {
        if (this.length == 0) return;

        i = 1*this.length-1
        e = this[i]
        this[i] = 0
        this.length = i

        return e
    }

    /**
     * Adds a new element to the end of the array.
     *
     * @param e The element to add to the end of the array.
     */
    this.push = function (e) {
        n = 1*this.length
        this[n] = e
        this.length = n + 1
    }

    /**
     * Removes the element at the specified index and returns it.
     *
     * @param i The index of the element to remove.
     */
    this.removeAt = function (i) {
        if (i < 0 || i >= this.length) return;

        e = this[i]
        this.length = 1*this.length - 1

        for (n = i; n < this.length; n++) {
            this[n] = this[1*n+1]
        }

        return e
    }

    return this
}
