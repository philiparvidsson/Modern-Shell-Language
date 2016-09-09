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
