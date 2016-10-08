include('stdio.js')

// This is a kind of constructor function for the base class. You can
// think of it as the abstract super class initializer function.
function animal(kind) {
    // We don't have to use the variable name 'this', but it
    // illustrates the intent of this function very well.
    this = []

    // Here, we add a 'kind' property to the object,
    this.kind = kind

    // This is a kind of instance method. We can reference any outer
    // variable through closures so we could use 'this' inside it.
    // Take a look at the instance methods in cow() and animal()
    this.say = function () {
        println('hello from base class')
    }

    return this
}

// The cow constructor creates a cow object derived from the animal class.
function cow(name) {
    this = animal('cow')

    this.name = name

    super_say = this.say

    this.say = function (s) {
        super_say() // <-- This is where we call the super class say() function!
        println(this.name, 'the cow moos', s, "because he's a", this.kind)
    }

    return this
}

// The duck constructor creates a duck object derived from the animal class.
function duck(name) {
    this = animal('duck')

    this.name = name

    this.say = function (s) {
        println(this.name, 'the duck quacks', s, "because she's a duck")
    }

    return this
}

// Let's create two derived instances.
charlie = cow('charlie')
anna = duck('anna')

// And then invoke their methods.
charlie.say('hello world')
anna.say('good morning')
