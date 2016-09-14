function animal(kind) {
    this = []

    this.kind = kind

    this.say = function () {
        console.log('hello from base class')
    }

    return this
}

function cow(name) {
    this = animal('cow')

    this.name = name

    super_say = this.say

    this.say = function (s) {
        super_say() // <-- This is where we call the super class say() function!
        console.log(this.name, 'the cow moos', s, "because he's a", this.kind)
    }

    return this
}

function duck(name) {
    this = animal('duck')

    this.name = name

    this.say = function (s) {
        console.log(this.name, 'the duck quacks', s, "because she's a duck")
    }

    return this
}

charlie = cow('charlie')
anna = duck('anna')

charlie.say('hello world')
anna.say('good morning')
