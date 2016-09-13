function outer(x) {
    outer_var = x

    inner = function () {
        console.log('ass', outer_var)
    }

    return inner
}

q = outer('abc')
q()
