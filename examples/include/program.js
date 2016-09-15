include('stdio.js')

// Include the data definitions file
include('data.js')

// MY_DATA is defined in data.js, but we can use it here since
// we included the file.
println('MY_DATA is', MY_DATA)

// We can also call functions in data.js as long as we include it.
s = data_func('world')

// And we can retrieve values from functions in other files.
println(s)
