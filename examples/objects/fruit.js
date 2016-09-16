include('stdio.js')

// This example shows the use of closures in Smaragd.

// Let's define a constructor function.
function fruit(name) {
    // Create an empty array - they can be used as anonymous objects!
    // We call it this to make the functions/methods more clear.
    this = []

    // Add a name property with the specified value.
    this.name = name

    // The peel function works like an instance method.
    this.peel = function (how) {
        println('i peel the', this.name, how)
    }

    // Return the newly created objects.
    return this
}

// Create one apple and one orange.
apple = fruit('apple')
orange = fruit('orange')

// Let's peel them!
apple.peel('with a knife')
orange.peel('with my fingers')
