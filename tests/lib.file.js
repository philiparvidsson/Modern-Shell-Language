include('assert.js')
include('file.js')

FILE_NAME = 'file.txt'
FILE_TEXT = 'hello 123 abc'

f = file(FILE_NAME, 'a')
assert.isFalse(f.exists(), "file used in test should not exist yet")
f.write(FILE_TEXT)
assert.isTrue(f.exists(), "File.write seems to have failed")
assert.equal(f.read(), FILE_TEXT, "File.write or File.read failed")
f.delete()
assert.isFalse(f.exists(), "file should not exist anymore")
