include('assert.js')

i = 0
j = 20
for (i = 0; i < j; i++) {
    j--
}

assert.equal(i, 10, 'for-loop produced incorrect results')
assert.equal(i, j , 'i and j should be equal')

k = 4
l = 0
while (k <= 10) {
    k += 2
    l -= 3
}

assert.equal(k, 12  , 'while loop produced incorrect results 1')
assert.equal(l, 0-12, 'while loop produced incorrect results 2')

m = 10
while (m > 0) {
    m--
    if (m == 5) break
}

assert.equal(m, 5, 'break did not seem to work correctly 1')

for (n = 0; n < 10; n++) {
    if (n == 7) break
}

assert.equal(n, 7, 'break did not seem to work correctly 2')

o = 0
for (p = 0; p < 10; p++) {
    if (p == 3) break
    for (q = 0; q < 10; q++) {
        if (q == 7) break
        o++
    }
}

assert.equal(o, 21, 'break did not seem to work correctly 3')

r = 10
s = 0
while (r > 0) {
    r--
    if (r == 5) continue
    s++
}

assert.equal(s, 9, 'continue did not seem to work correctly 1')

t = 0
for (u = 0; u < 10; u++) {
    if (u == 0) continue
    if (u == 1) continue

    t++
}

assert.equal(t, 8, 'continue did not seem to work correctly 2')

u = 0
for (v = 0; v < 10; v++) {
    if (v == 3) continue
    for (w = 0; w < 10; w++) {
        if (w == 7 || v == 4) continue
        u++
    }
}

assert.equal(u, 72, 'continue did not seem to work correctly 3')
