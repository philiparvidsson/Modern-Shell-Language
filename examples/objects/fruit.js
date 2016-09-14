// This example shows the use of closures in Smaragd.

// Let's define a constructor function.
function fruit(name) {
    // Create an empty array - they can be used as anonymous objects!
    // We call it this to make the functions/methods more clear.
    this = []

    // Add a name property with the specified value.
    this.name = name

    this.peel = function (how) {
        console.log('i peel the', this.name, how)
    }

    return this
}

// Create one apple and one orange.
apple  = fruit('apple')
orange = fruit('orange')

// Then peel them!
apple.peel('with a knife')
orange.peel('with my fingers')
