// Arrays contain elements:
a = [123, 456, 789]

for (i = 0; i < a.length; i++)
    console.log(a[i])

// Arrays can also be nested:
b = [['a', 'b', 'c'],
     [ 1 ,  2 ,  3 ],
     ['x',  5 , 'z']]

for (i = 0; i < b.length; i++)
    for (j = 0; j < b[i].length; j++)
        console.log(b[i][j])

// Arrays are also dictionaries!
c = []
c['foo'] = 'hello world'
console.log(c['foo'])

// Dictionary values can also be accessed like this:
console.log(c.foo)

// Arrays are mutable:
d = [10, 20, 30]
d[d.length] = 40
d.length = 1*d.length+1
console.log[d[2]]

for (i = 0; i < d.length; i++)
    console.log(d[i])
