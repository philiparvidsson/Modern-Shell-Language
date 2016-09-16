# Frequently Asked Questions

## Why mshl?

Shell scripting is still an important aspect of automating tasks on computer systems. It is used widely in the industry on everything from Windows servers to Linux workstations. Certain tasks are common to both platforms, but they do not yet share sufficient ground that the scripts can be reused easily on both platforms. MSHL makes this easy by providing a common language that compiles to several platforms, all without requiring the end user to install extra software.

## Why are my integer additions treated as string concatenations?

You might encounter a situation where an addition of two integer variables is treated as a concatenation of two strings. Although we try to continuously improve type inference in mshl, the dynamic and loosely typed nature of shell scripting makes this problematic, especially if performance is considered. To resolve the situation, simply cast one or both of the involved variables to an integer by multiplying it with one:

```javascript
/* ... */

x = 1*a + 1*b
```
