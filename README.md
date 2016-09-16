# Modern Shell Language <img align="right" src="img/mshl-logo.png">

**mshl** is a language for performing automated shell tasks. It's similar to JavaScript in its [syntax](doc/syntax.md) and compiles to Windows batch files (a bash target is planned!). This gives you the freedom of modern syntax and language functionality, allowing you to write much more complex programs that run on Windows and Linux **without requiring the end user to install any extra piece of software**.

## Getting Started

1. Download and install [Python 2.7.x](https://www.python.org/downloads/).
2. Write a program in mshl or download one of the [examples](examples).
3. Compile the program with mshlc by invoking it with Python (make sure you are in the correct directory first!): `python mshlc filename.js`

Depending on your platform, you will have a file named `<filename>.bat` in your current directory. It is the compiled shell script, ready to be deployed and executed on any system. The system that you deploy the program on will **not require any software installation**—a mere copy of the compiled script file is required.

### Prerequisities

* [Python 2.7.x](https://wiki.python.org/moin/BeginnersGuide/Download)

### Installing

#### Begin by downloading and installing [Python 2.7.x](https://www.python.org/downloads/).
On Linux, depending on your distribution, Python comes pre-installed. This means that you do not need to install anything for mshl to work. If you don't have Python (you can check by typing python in a terminal), you might be able to install it by typing `sudo apt-get install python`.

On Windows, you need to install Python manually. See [this link](https://wiki.python.org/moin/BeginnersGuide/Download) for more information.


#### Download the latest mshl release.
The latest mshl binary is always available from here. Download and save it to a directory on your computer.

#### Write a simple program in mshl.
To familiarize yourself with mshl, you can begin by writing a simple test program. You could also use one of the [example programs](examples), or the one below if you just want to try mshl out quickly:

```javascript
include('stdio.js')

s = userinput("what's your name? ")
println('hey, ', s, '... oh, and hello world')
```

Mshl is able to compile very complex programs, generating advanced shell scripts performing tasks unthinkable in hand-written shell scripts!

#### Compile your program.
Save your program in a file and compile it with mshlc by invoking it through Python. Let's say, for example, that you saved the example code above in a file named myprog.js. You can then compile it by invoking mshlc in the following way: `python mshlc myprog.js`

Make sure you have the mshlc binary in the current directory!

## Running the Tests

Run the tests by executing `python runtests.py` in the `src`directory. All tests in the `tests` directory will be built and run automatically, ending with a report of passing and failing tests, as well as how much time it took to run them.

## Deployment

### Deploying the compiler

Deploying the mshl compiler is a matter of downloading the mshl binary. The compiler is then invoked with Python by typing `python mshlc <srcfile>`, which will generate a shell script for the target platform.

### Deploying compiled programs

Programs compiled with mshlc are shell scripts that run on their target platforms without requiring the installation of any software. Simply transfer the compiled script to the target system and run it!

## Built With

* emacs - The best text editor out there! ;-)
* Python - A widely used high-level, general-purpose, interpreted, dynamic programming language.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/philiparvidsson/mshl/tags). 

## Authors

* **Philip Arvidsson** - *Initial work* - [philiparvidsson](https://github.com/philiparvidsson)
* **Mattias Eriksson** - *Complementary work* - [matteyas](https://github.com/matteyas)

See also the list of [contributors](https://github.com/philiparvidsson/mshl/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

