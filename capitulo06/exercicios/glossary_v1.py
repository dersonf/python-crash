#!/usr/bin/python3

glossario = {
    'c': 'C is a general-purpose, procedural computer programming language \
supporting structured programming, lexical variable scope, and recursion, \
with a static type system. By design, C provides constructs that map \
efficiently to typical machine instructions. It has found lasting use in \
applications previously coded in assembly language. Such applications include \
operating systems and various application software for computer architectures \
that range from supercomputers to PLCs and embedded systems.',
    'ruby': 'ruby é uma linguagem de programação interpretada multiparadigma, \
de tipagem dinâmica e forte, com gerenciamento de memória automático, \
originalmente planejada e desenvolvida no Japão em 1995, por Yukihiro "Matz" \
Matsumoto, para ser usada como linguagem de script. Matsumoto queria \
desenvolver uma linguagem de script que fosse mais poderosa do que Perl, e \
mais orientada a objetos do que Python.[4] Ruby suporta programação \
funcional, orientada a objetos, imperativa e reflexiva. Foi inspirada \
principalmente por Python, Perl, Smalltalk, Eiffel, Ada e Lisp, sendo muito \
similar em vários aspectos a Python. Ruby está entre as 10 linguagens mais \
populares, de acordo com uma pesquisa conduzida pela RedMonk.',
    'python': 'Python is an interpreted, high-level and general-purpose \
programming language. Created by Guido van Rossum and first released in 1991, \
Python\'s design philosophy emphasizes code readability with its notable use \
of significant whitespace. Its language constructs and object-oriented \
approach aim to help programmers write clear, logical code for small and \
large-scale projects.',
    'java': 'Java is a class-based, object-oriented programming language that \
is designed to have as few implementation dependencies as possible. It is a \
general-purpose programming language intended to let application developers \
write once, run anywhere (WORA),[17] meaning that compiled Java code can run \
on all platforms that support Java without the need for recompilation.[18] \
Java applications are typically compiled to bytecode that can run on any \
Java virtual machine (JVM) regardless of the underlying computer \
architecture. The syntax of Java is similar to C and C++, but it has fewer \
low-level facilities than either of them. As of 2019, Java was one of the \
most popular programming languages in use according to GitHub,[19][20] \
particularly for client-server web applications, with a reported 9 million \
 developers.',
    'go': 'Go é uma linguagem de programação criada pela Google e lançada em \
código livre em novembro de 2009. É uma linguagem compilada e focada em \
produtividade e programação concorrente,[5] baseada em trabalhos feitos no \
sistema operacional chamado Inferno.[6] O projeto inicial da linguagem foi \
feito em setembro de 2007 por Robert Griesemer, Rob Pike e Ken Thompson. \
Atualmente, há implementações para Windows, Linux, Mac OS X e FreeBSD.',
    }

for k, v in glossario.items():
    print(f"{k}: {v}\n")
