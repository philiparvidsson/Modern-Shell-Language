Array = function (x) {
    this = []

    this.pop = function () {
        i = 1*this.length-1
        x = this[i]
        this[i]=0
        this.length = i

        return x
    }

    this.push = function (x) {
        this[1*this.length] = x
        this.length = 1*this.length + 1
    }

    return this
}
