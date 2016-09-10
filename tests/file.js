include('inc/testing.js')

test.name = 'file operations test'

s = file.read('file.txt')
assert.areEqual(s, 'hello world', 'file contents read incorrectly')
