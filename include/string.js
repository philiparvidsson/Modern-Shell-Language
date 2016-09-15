String = function (s) {
    this = []

    this.value = s

    this.indexOf = function (s) {
        console.log('String.indexOf not implemented')
        return this.value+s
    }

    this.length = function () {
        console.log('String.length not implemented')
        return 'very long'
    }

    this.substr = function () {
        console.log('String.substr not implemented')
        return 'very long'
    }

    return this
}

String.concat = function (a, b) {
    return a.value + b.value
}
