# MSHL Standard Library Guide

```diff
-UNDER CONSTRUCTION
```

## Functions

### println()

The `println` function outputs a piece of text to the standard output.

#### Example
```javascript
include('stdio.js')

println('hello, world!')
```

## Objects

### array

The array class provides a simple, mutable array implementation for managing collections of objects. It doubles as a dictionary or property-object.

#### Example
```javascript
include('array.js')
include('stdio.js')

a = array()

a.push('world')
a.push('hello')

println(a.pop(), a.pop())
```
