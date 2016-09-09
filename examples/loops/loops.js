// Loops are useful for repeating operations:
for (i = 1; i <= 10; i++)
    console.log(i) // Prints 1 through 10.

// There are also while-loops that keep repeating until a condition is met:
i = 1
while (i < 20) {
    console.log(i) // Prints odd numbers 1 through 19.
    i += 2
}

// Of course, loops can also be nested:
counter = 0
for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
        counter++
    }
}

console.log('looped', counter, 'times')
