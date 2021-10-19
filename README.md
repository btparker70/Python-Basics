# Python-Basics
the basics of python courses by Mosh
1. there are multiple variations of python based in other languages
  - CPython in C
  - Jython in java
  - IronPython in C#
  - Pypy in a subset of python
  - you can execute their respective code in these formats
2. How python code is executed:
  - C code needs to go through a compiler and this compiler is different for both mac and pc because it needs to compile into different machine languages
  - java compiler doesn't compile java into machine code it compiles into java bytecode, which then goes through java virtual machine and at run time converts the instruction into machine code
    - this works for windows, mac etc
  - python -> CPython compiler -> Python ByteCode -> Python virtual machine
  -> machine code
  - if you're using Jython, it compiles to java bytecode!
3. Dynamic language
  - python is a dynamic language, that means that variables don't need to be preassigned/declared their type like in C
  - Python is an Object oriented language
  - The types of variables are determined at run time as opposed to compile time!
4. memory location
  - id(x) will show where something is stored on the memory!
  - integers are immutable
    - if you update a variable, it won't change the variable stored at the original location. it will create a new reference to the updated variable
  - lists are mutable, so they dont change memory address when they are mutated!
  - primative types :strings, ints, booleans  are immutable!
5. Strings are iterable
6. ranges return a range object
  - it's an instance of a class called 'range'
  - range functions return a range object
  - they are itnerable so we can use them in loops
  - they take a small amount of memory
7. stacks
  - LIFO: last in - first out
8. sets are unordered and cannoy be accessed by index.
