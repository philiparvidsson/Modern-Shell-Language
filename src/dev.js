i = 0;
while (i < 5) {
  print(i + " ");
  i = i + 1;
}

// Fibonacci
n = 0;
i = 0;
j = 1;
while (n < 40) {
  k = i + j;
  i = j;
  j = k;
  n = n + 1;
}
