include('../lib/console.js')
include('../lib/file.js')

f = File('foo.txt', 'a')
println(f.exists())
f.write('hej')
println(f.exists())
println(f.read())
f.delete()
