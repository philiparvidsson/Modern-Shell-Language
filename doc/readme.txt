�Batch 2.0�

I detta dokument sp�nar vi p� id�er till det spr�k vi ska designa som ska ers�tta batch. Tanken �r att skriva en transpilator som �vers�tter fr�n detta spr�k till batch-skript, eftersom batch �r s� uselt.



Namnf�rslag

Betch (Better Batch), Motch (Modern Batch), Crutch, Jatch (Java-like Batch?)


Spr�kspec.

Scopes:

...

Kommentar:
		
Vi kan antingen anv�nda m�svingar f�r scopes (som JavaScript) eller indentering (som Python). Philip f�redrar indentering eftersom m�svingar �r fula samt indentering tvingar fram en vettig kod. Tv�ng �r bra.


Kommentarer:

# Kommentar.

Kommentar:
	
Kanske d�lig id� med # som ledande tecken f�r kommentarer med tanke p� kommentarer som sp�nner �ver flera rader?


If-satser:

if expr:
    do_something()
elif expr2:
    do_something_2()
else:
    do_something_else()

Kommentar:
	
Po�ngl�st med on�diga nyckelord som then. 

While-loopar:

while expr:
    do_something()

Kommentar:
	
�

For-loopar:

for i in 1..10 step 2
    do_something()

Kommentar:
	
...

Funktioner och funktionsanrop:

func foo(arg1, arg2):
    x = foo(arg1)
    y = bar(arg2)
    return x+y

Kommentar:
	
...

Str�ngar:

s = �some string�

Kommentar:
	
Single- eller double-quotes, det �r fr�gan.

Inbyggda funktioner:

print:
	Skriver ut en text till console. Ex. print �hej�
