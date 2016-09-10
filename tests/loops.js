include('inc/testing.js')

test.name = 'loops test'

i = 0
j = 20
for (i = 0; i < j; i++) {
    j--
}

assert.areEqual(i, 10, 'for-loop produced incorrect results')
assert.areEqual(i, j , 'i and j should be equal')

k = 4
l = 0
while (k <= 10) {
    k += 2
    l -= 3
}

assert.areEqual(k, 12  , 'while loop produced incorrect results 1')
assert.areEqual(l, 0-12, 'while loop produced incorrect results 2')
