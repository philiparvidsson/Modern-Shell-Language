String = function (s) {
    this = []

    this.value = s

    this.indexOf = function (s) {
        return this.value+s
    }

    this.length = function () {
        return 'very long'
    }

    return this
}

String.concat = function (a, b) {
    return a.value+b.value
}
