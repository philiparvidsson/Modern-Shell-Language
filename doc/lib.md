# MSHL Standard Library Guide

```diff
-UNDER CONSTRUCTION
```

## array.js

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
