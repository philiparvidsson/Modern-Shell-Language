function other_func(s) {
    // Variables can also point to functions!
    print = console.log
    print(s)

    // Functions can return values!
    return 'world'
}

function main() {
    // This is a function!

    // Variables in functions are local to their scope...
    a = 'foo'

    // ...but can be accessed by inner functions:
    b = function () {
        return a // returns 'foo'
    }

    // Functions can call other functions.
    s = other_func('hello')

    console.log(s)
}

// The line below would result in an error since a is inside main()!
//console.log(a)

// This is where we invoke the main function.
main()
