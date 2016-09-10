include('inc/testing.js')

test.name = 'file operations test'

FILE_NAME = 'file.txt'

assert.isTrue(file.exists(FILE_NAME), "file needed for test doesn't exist")

s = file.read(FILE_NAME)
assert.areEqual(s, 'hello world', 'file contents read incorrectly')
