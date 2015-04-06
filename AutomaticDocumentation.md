# Introduction #

A number of tools exist to generate documentation for large projects, they're all pretty similar, for example javadoc, doxygen and epydoc. They all examine the code and the comments in the code (which can be specially formatted) and generate HTML pages or PDF files of documentation.

Epydoc is the best choice for this project because it was designed for projects written in Python, and will generate UML class diagrams automatically.


# Details #

Right now a copy of the documentation is in the repository, this will change in future. The ideal system would have a server that serves the main site, which downloads the latest copy of the code from the repository whenever it is changed. Whenever the server downloads new code, it will generate new documentation for the new code, and, since it's html, serve it on the website so that we can easily browse it. Because the server generates the docs automatically, we don't need to install epydoc on our computers, and we don't need to know about how the documentation is processed, we just need to know how to make code that epydoc can make meaningful documentation from.

### Writing Code for automatic documentation ###

Basically just write normal code, and make use of python's docstrings

A string at the begining of a function (or a class or file) is a docstring, which will show up in the documentation.

```
def addnums(x,y):
  "Add 2 numbers together"
  return x + y
```

Epydoc also has a bunch of other stuff you can add to docstrings that it will parse, shown on [the epydoc page](http://epydoc.sourceforge.net/manual-epytext.html).
If we were being really thorough we could do;

```
def addnums(x,y):
  """Add 2 numbers together

    @type  x: number
    @param x: The first number
    @type  y: number
    @param y: The second number
    @rtype:   number
    @return:  The result of adding the numbers together M{x+y}.
  """

  return x + y
```

Which would make really extensive documentation.

#### Tests ####

We can also stick the unit tests in there too.

```
def addnums(x,y):
  """Add 2 numbers together

    >>> addnums(6,7)
    13
    >>> addnums(10,-5)
    5

    @type  x: number
    @param x: The first number
    @type  y: number
    @param y: The second number
    @rtype:   number
    @return:  The result of adding the numbers together M{x+y}.
  """

  return x + y
```

The code after `>>>` is run, and the result has to match the next line.