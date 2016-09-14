// this file is just for experimenting with raw statements and creating
// built-ins in smaragd directly

String = function (s) {
    this = []

    this.value = s

    this.length = function () {
        return 'very long'
    }

    return this
}

String.concat = function (a, b) {
    return a.value+b.value
}
