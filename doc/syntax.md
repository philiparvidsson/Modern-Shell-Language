# Syntax

The syntax is based on JavaScript to provide a familiar environment, make porting already-existing programs less of a hassle and to provide a simple syntax that is easily understandable.

## Assignment

The most basic operations are variable assignments. mshl tries to 'infer' types in the sense that it can tell integer and string variables apart most of the time. Also, semicolons after statements are almost always optional in mshl, the exception being after the return keyword when there is no return expression.

```javascript
/* Numbers */
a = 10
b = 0x10
c = 10b // Binary numbers are supported!

/* Strings */
x = "a string"
y = 'another string'
```

## Integer Operations

Integer operations are various ways of working with integers. mshl does not place a restriction on the magnitude of integers used in scripts, although, for the sake of portability, you should take care to stick inside signed 32-bit ranges.

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

## String Operations

Strings are a basic and native literal type in mshl, just like integers. Instead of numbers, they contain a piece of text. Strings are not restricted in any way by mshl, but different output targets might have varying limits on string length, encoding etc.

```javascript
a = 'foo'
b = 'bar'

c = a+b // Concatenation
```

## Boolean Operations

Boolean logic in mshl is also native and internally use integer operations. For example, the value true is exactly 1, and the value false is 0. Anything non-zero, however, is considered to be true during evaluation of boolean expressions.

```javascript
a = true   // 1
b = false // 0

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

## Conditional Statements

Conditional statements build syntactic sugar on boolean operations to provide a more natural and intuitive way to perform operations only when certain conditions are met.

```javascript
include('stdio.js')

function foo() { println('foo'); return false }
function bar() { println('bar'); return true }

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

## Loops

Performing the same operation over and over a given number of times requires its own syntax construct, namely loops. For-loop and while-loops work under the same principles—do the same thing over and over until a certain condition no longer holds.

```javascript
include('stdio.js')

/* While-loop */
a = 0
while (a++ < 10) {
    println(a) // Prints 1 through 10.
}

/* For-loop */
for (i=1; i <= 10; i++) {
    println(i) // Prints 1 through 10.
}
```

## Functions

Functions provide a way to batch a series of statements together and perform a certain task. During a function call, the function has its own [scope](https://en.wikipedia.org/wiki/Scope_(computer_science)). If this scope is referenced by further nested function calls, it is stored as a [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)).

Functions also have the ability to carry properties, and thus can be used as arrays, dictionaries or objects. More on this below!

```javascript
include('stdio.js')

function my_func(s) {
    println(s)
}

my_func('hello world')

// Anonymous functions are supported too!
log_fn = function (s) { println(s) }
log_fn('hello again')
```

## Arrays

Arrays are native, although loosely typed, objects in mshl. They can be used as regular arrays, mutable dictionaries or as objects with properties. Below, we use an array in the most intuitive way. See the [examples](../examples) for more information on how arrays (and other features of mshl) can be used.

```javascript
include('stdio.js')

function print_all(a) {
    i = 0
    s = ''
    while (i < a.length) {
        s += (a[i] + ' and ')
        i++
    }
    println(s)
}

print_all(['one', 'two', 'three'])
```

## Objects

In mshl, we can use array declarations or function definitions as objects, depending on the intent.

```javascript
include('stdio.js')

function show_fruit_info(f) {
    println('the', f.name, 'is', f.taste)
}

fruit = [] // Array declarations can be used as objects!
fruit.name = 'apple'
fruit.taste = 'sweet'

show_fruit_info(fruit)

// Objects can have functions!
fruit.eat = function (s) { println('wow, what a', s, 'apple') }
fruit.eat('crunchy')
```

## Built-in Functions

### include()

The `include()` function is a built-in compile-time function that includes another mshl source file by inserting it into the source file with the `include()`-statement, where the statement was encountered.

```javascript
/**
 * include(s) - Includes the specified file for use in the current source file.
 *
 * Examples:
 */

// a.js:
MY_STRING = 'hello world'

// b.js:
include('stdio.js') // needed for println()

include('a.js')

println(MY_STRING)
```

### raw()

The `raw()` function is, again, a built-in compile-time function. It provides a way to inject code directly into the compiled code, at the point where the function is used.

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
