# Introduction #

I really hardly know anything about this, when you work out how to do things that we should know, add it in here.


# Details #

In windows you can use [winedt](http://www.winedt.com/), Chris recommends TeXWorks.

In linux use tex-live and the `pdflatex` command

In mac, idk.

## Example Document ##

here is an example file, as found [here](http://amath.colorado.edu/documentation/LaTeX/basics/example.html)

```
\documentclass[12pt]{article}

\newcommand{\piRsquare}{\pi r^2}		% This is my own macro !!!

\title{My Sample \LaTeX{} Document}			% used by \maketitle
\author{\L\"{a}rs  Schl{\oe}ff\d{o}ng\"{e}n, }		% used by \maketitle
\date{July 14, 2005}					% used by \maketitle

\begin{document}
\maketitle						% automatic title!

I typed this file with a plain text editor.
(I used \textbf{pico} and \textbf{emacs}.)
End
	of
		paragraph.

This is my second paragraph.
The area of a circle is $\pi r^2$; again, that is $\piRsquare$.
My score on the last exam\footnote{May 23} was $95 \pm 5$.

\section{Formulae; inline vs. displayed}

I insert an inline formula by surrounding it with a pair of
single \$ symbols;  what is $x = 3 \times 5$?
For a \emph{displayed} formula, use double-\$
before and after --- include no blank lines!
$$\mu^{\alpha+3} + (\alpha^{\beta}+\theta_{\gamma}+\delta+\zeta)$$

\subsection{Numbered formulae}

Use the \emph{equation} environment to get numbered formulae, e.g.,
\begin{equation}
	y_{i+1} = x_{i}^{2n} - \sqrt{5}x_{i-1}^{n} + \sqrt{x_{i-2}^7} -1
\end{equation}

\begin{equation}
	\frac{\partial u}{\partial t} + \nabla^{4}u + \nabla^{2}u +
        \frac12    |\nabla u|^{2}~ =~ c^2
\end{equation}

\section{Acknowledgments}

Thanks to my buddies {\AE}schyulus and Chlo\"{e},
who helped me define the macro \verb9\piRsquare9
which is $\piRsquare$.
The end.

\end{document}             % End of document.
```

## Including Code Files ##

If you want to show some code in a fixed with font, use the verbatim environment;

```
\begin{verbatim}
def square(i):
  return i**2
\end{verbatim}
```

If you want to include another file, use `input`. This is cool because you can have different chapters in different files and have them all imported into the main file

```
\input{filename.tex}
```

But because `verbatim` interprets text verbatim, doing

```
\begin{verbatim}
\input{mycode.py}
\end{verbatim}
```

will just put `\input{mycode.py}` into the document in a fixed width font, rather than inserting the actual contents of mycode.py, so we need to use the `alltt` environment

```
\usepackage{alltt}

\begin{alltt}
\input{mycode.py}
\end{alltt}
```

which will do the right thing
