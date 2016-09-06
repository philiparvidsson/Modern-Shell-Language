# Codename Crutch
Crutch is a compiler for a JavaScript-like language. It compiles to Windows Batch (more targets will be provided in the future!) files. This gives you the freedom of modern syntax and language functionality, allowing you to write much more complex programs that run on Windows without requiring the end user to install any piece of software.

# Syntax
The syntax is based on JavaScript to provide a familiar environment, make porting less of a hassle and stick to a simple syntax that is easy for anyone to understand.

## Assignment
```javascript

/* Numbers */
a = 10
b = 0x10
c = 10b // Binary numbers are supported!

/* Strings */
x = "a string"
y = 'another string'
```

## Integer operations
```javascript
a = 7
b = 5

// Basic
a++ // Increment
b-- // Decrement

// Arithmetic
c = a+b // Addition
d = a-b // Subtraction
e = a*b // Multiplication
f = a/b // Division 

// Binary
g = a&b // And
h = a|b // Or
i = a^b // Xor
j = a<<b // Left-shift
k = a>>b // Right-shift
```

## String operations
```javascript
a = "foo"
b = "bar"

c=a+b // Concatenation
```

## Input/output
```javascript

a = readline("What's your name?") // Ask user for input
console.log(a) // Print the input back to the console.
```

## Loops
```javascript
// While-loops:
a = 0
while ((a++) < 10) {
    console.log(a) // Prints 1 through 10.
}

// For-loops:
// NOT YET SUPPORTED!

## Functions
Crutch naturally supports functions.
```javascript
function my_func(s) {
    console.log(s)
}

my_func('hello world!')

// Anonymous functions are supported too!
log_fn = function (s) { console.log(s) }
log_fn('hello again!')
```

## Arrays
Crutch has support for arrays.
```javascript
function print_all(a) {
    i = 0
    s = ''
    while (i < a.__length__) {
        s += (a[i] + ' and ')
        i++
    }
    console.log(s)
}

print_all(['one', 'two', 'three'])
```

## Objects
Crutch also supports objects!
```javascript
function show_fruit_info(f) {
    console.log('the', f.name, 'is', f.taste)
}

fruit = [] // Array declarations can be used as objects!
fruit.name = 'apple'
fruit.taste = 'sweet'

show_fruit_info(fruit)
```
