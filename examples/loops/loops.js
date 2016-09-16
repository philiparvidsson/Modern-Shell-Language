include('stdio.js')

// Loops are useful for repeating operations:
for (i = 1; i <= 10; i++)
    println(i) // Prints 1 through 10.

// There are also while-loops that keep repeating until a condition is met:
i = 1
while (i < 20) {
    println(i) // Prints odd numbers 1 through 19.
    i += 2
}

// Of course, loops can also be nested:
counter = 0
for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
        counter++
    }
}

println('looped', counter, 'times')

// We can also abort loops by breaking out of them:
for (i = 0; i < 1000; i++) {
    println('hi')

    // We break when i equals 2, so we only print
    // 'hi' three times.
    if (i == 2) break
}

// Use the continue keyword to jump to the start of them:
for (i = 0; i < 1000; i++) {
    // This loop will only print 'hello' once since we skip all
    // iterations except the last one.
    if (i < 999) continue

    println('hello')
}
