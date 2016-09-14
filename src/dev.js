/*a = []

a.push = function (w) {
    a[1*a.length] = w
    a.length = 1*a.length+1
}


a.push('abc')
a.push('123')

for (i = 0; i < a.length; i++) console.log(a[i])
*/
include ('../lib/array.js')

a = Array()
a.push('hej')
a.push('bosse')

for (i = 0; i < a.length; i++) {
    console.log(a[i])
    process.sleep(1)
}
