function k() {
    obj = []

    obj.test_func = function qq() {
        return obj.value
    }

    return obj
}

l = k()

l.value = 444

console.log(l.test_func())
