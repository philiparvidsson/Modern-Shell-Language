# Smaragd
Smaragd is a compiler for a JavaScript-like language. It compiles to Windows Batch (more targets will be provided in the future!) files. This gives you the freedom of modern syntax and language functionality, allowing you to write much more complex programs that run on Windows without requiring the end user to install any piece of software.

## Syntax
The syntax is based on JavaScript to provide a familiar environment, make porting less of a hassle and to provide a simple syntax that is easily understandable.

### Assignment
The most basic operations are variable assignments. Smaragd tries to 'infer' types in the sense that it can tell integer and string variables apart for the most part. Also, semicolons after statements are always optional in Smaragd.

```javascript

/* Numbers */
a = 10
b = 0x10
c = 10b // Binary numbers are supported!

/* Strings */
x = "a string"
y = 'another string'
```

### Integer Operations
```javascript
a = 7
b = 5

/* Basic */
a++ // Post-increment
b-- // Post-decrement

/* Arithmetic */
c = a+b // Addition
d = a-b // Subtraction
e = a*b // Multiplication
f = a/b // Division

/* Binary */
g = a&b  // And
h = a|b  // Or
i = a^b  // Xor
j = a<<b // Left-shift
k = a>>b // Right-shift

// Most of the operations above also exist as assign-operations, i.e. a+=1, b<<=1 etc.
```

### String Operations
```javascript
a = 'foo'
b = 'bar'

c = a+b // Concatenation
```

### Boolean Operations
```javascript
a = true
b = false

c = a && b // Logical and
d = a || b // Logical or

e = 42
f = 42

g = e==f // true
h = e!=f // false
i = e<f  // false
j = e<=f // true
k = e>f  // false
l = e>=f // true

m = !true // not-operator
```

### Conditional Statements
```javascript
function foo() { console.log('foo'); return false }
function bar() { console.log('bar'); return true }

a = false

/* Regular if-then-else statements */
if (a) foo() else bar() // Braces can be omitted for single statements.

if (a) {
    foo()
}
else {
    bar()
}

/* Ternary operator */
fn = a ? foo : bar
fn()
// We could also do: a ? foo() : bar()

/* Short-circuiting */
foo() && bar() // Only prints 'foo' since foo() returns false!
foo() || bar() // Prints 'foo' and 'bar'
```

### Loops
```javascript
/* While-loop */
a = 0
while ((a++) < 10) {
    console.log(a) // Prints 1 through 10.
}

/* For-loop */
for (i=1; i <= 10; i++) {
    console.log(i) // Prints 1 through 10.
}
```

### Functions
Smaragd naturally supports functions.
```javascript
function my_func(s) {
    console.log(s)
}

my_func('hello world')

// Anonymous functions are supported too!
log_fn = function (s) { console.log(s) }
log_fn('hello again')
```

### Arrays
Smaragd has support for arrays.
```javascript
function print_all(a) {
    i = 0
    s = ''
    while (i < a.length) {
        s += (a[i] + ' and ')
        i++
    }
    console.log(s)
}

print_all(['one', 'two', 'three'])
```

### Objects
Smaragd also supports objects!
```javascript
function show_fruit_info(f) {
    console.log('the', f.name, 'is', f.taste)
}

fruit = [] // Array declarations can be used as objects!
fruit.name = 'apple'
fruit.taste = 'sweet'

show_fruit_info(fruit)

// Objects can have functions!
fruit.eat = function (s) { console.log('wow, what a', s, 'apple') }
fruit.eat('crunchy')
```

## Built-in Functions/Objects

### console
```javascript
/**
 * console.log(s) - Prints text to the console.
 *
 * Examples:
 */
console.log('hello', 'world') // Print 'hello world' to the console.
```

### file
```javascript
/**
 * file.delete(s) - Deletes the specified file if it exists. Returns true if the file existed.
 *
 * Examples:
 */
file.delete('myfile.txt')

/**
 * file.exists(s) - Returns true if the specified file exists.
 *
 * Examples:
 */
file.exists('myfile.txt') ? console.log('file exists') : console.log('no such file')

/**
 * file.read(s) - Reads the contents of the file with the specified name and returns it as a string.
 *
 * Examples:
 */
s = file.read('myfile.txt')
```

### include()
```javascript
/**
 * include(fileName) - Includes the specified file for use in the current source file.
 *
 * Examples:
 */

// a.js:
MY_STRING = 'hello world'

// b.js:
include('a.js')
console.log(MY_STRING)
```

### process
```javascript
/**
 * process.argv - Array containing the arguments passed to the program.
 *
 * Examples:
 */
for (i=0; i < process.argv.length; i++)
    console.log(process.argv[i])
    
/**
 * process.exit(code) - Exits the process.
 *
 * Examples:
 */
process.exit()  // Exit with process.exitCode
process.exit(1) // Exit with code one.

/**
 * process.exitCode - The exit code to use if no code is specified in the call to process.exit()
 *
 * Examples:
 */
process.exitCode = 1
process.exit() // Exit with code one
```

### readline()
```javascript
/**
 * readline(s) - Reads a line form the console.
 *
 * Examples:
 */
s = readline('Enter name') // Asks the user to input his or her name.
s = readline()             // Reads a line from the user without displaying a prompt.
```

### raw()
```javascript
/**
 * raw(s)   - Inserts the string s directly into the shell script.
 * raw(s,t) - Optionally, t specifies the target platform: 'bat', 'bash'
 *            If the platform does not match t, no changes are made.
 *
 * Examples:
 */
raw('echo This line will be inserted directly into any shell script')
raw('echo This one will only be inserted into batch files', 'bat')
```
