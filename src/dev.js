a = 'C:\Users\Philip\Documents\New folder\qwe.txt'
if (file.exists(a)) {
    file.delete(a)
    console.log('file deleted')
}
else {
    console.log('no such file')
}
