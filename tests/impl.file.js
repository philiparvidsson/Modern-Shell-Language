include('inc/testing.js')

include('assert.js')
include('file.js')

test.name = 'file operations test'

FILE_NAME = 'file.txt'
FILE_TEXT = 'hello 123 abc'

file = File(FILE_NAME, 'a')
Assert.isFalse(file.exists(FILE_NAME), "file used in test should not exist yet")
file.write(FILE_TEXT)
Assert.isTrue(file.exists(FILE_NAME), "File.write seems to have failed")
Assert.equal(file.read(), FILE_TEXT, "File.write or File.read failed")
file.delete()
Assert.isFalse(file.exists(FILE_NAME), "file should not exist anymore")
