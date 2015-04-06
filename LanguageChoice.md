# Introduction #

Langauge and framework choice is important design decision, which needs to be justified.


# Details #

There were a number of options available;

## Simple HTML ##

Plain HTML and CSS files in a hierarchical directory structure

  * Pros
    * Would be very easy to do
  * Cons
    * Content is static
    * No database means no search

Plain HTML is simply too simple to fulfil even the most basic specification. We need some kind of program logic and a database to fulfil the specification.

## PHP + SQL ##

  * Pros
    * Some experience from G51WPS last year
    * Common technology means it is well supported
  * Cons
    * Low level control means making large systems is complicated and difficult

We could use a web framework to reduce the difficulty in making complex systems

## Ruby on Rails ##

A web framework based on the Ruby Language

  * Pros
    * Increased code reuse
    * Makes programming complex websites simpler
  * Cons
    * Abstraction may mean sacrificing fine control even when it would be useful
    * None of us know Ruby

## Django ##

A web framework based on the Python Language

  * Pros
    * Rob has experience developing with Django
    * Python is a nice language to learn and use, with a focus on simplicity and ease of use
    * A variety of third party plugins coincide with our site's functionality, saving a lot of work by maximising code reuse
  * Cons
    * Requires learning a new language

Of all of the options available, Django seems to best suit our needs.