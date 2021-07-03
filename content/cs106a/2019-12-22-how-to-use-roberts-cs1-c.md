Title: How to use Roberts.CS1.C
Slug: how-to-use-roberts-cs1-c
Lang: en
Translation: true
Authors: xuehao
Date: 2019-12-22 00:24
Modified: 2021-06-30 7:04
Summary: Library source code for the Eric Roberts texts, The Art and Science of C: A Library-Based Approach and Programming Abstractions in C: A Second Course in Computer Science.
Category: 笔记
Tags: C Programming, Computer Science, Data Structures, Algorithms
Status: published

Library source code for the Eric Roberts texts, _The Art and Science of C: A Library-Based Approach_ and _Programming Abstractions in C: A Second Course in Computer Science_.

## 1. How to build the library?

Follow these steps to build a personal root system which don't need system permission and a static library called _libcs.a_ for the upper two books.

Download this repo to your folder.

```shell
$ git clone https://github.com/xuehao/Roberts.CS1.C.git
```

Switch to the folder _cslib_. Use _make_ to build the library.

```shell
$ cd Roberts.CS1.C && cd cslib
$ make
```

If succeed, you'll find a folder called _root_. Copy the _root_ folder to your home directory.

```shell
$ mv root ~
```

## 2. How to connect the library?

Package all the options for the compiler and the linker used while building the C program into the general _Makefile_.

```
CC = gcc
CFLAGS = -I${HOME}/root/include/cs -g -Wall -std=gnu11 -O3
LDLIBS = -L${HOME}/root/lib/ -lcs -lm
```

Use the general _Makefile_ in the _test-cslib_ folder to build the _house.c_ program and to see how to connect the library.

```shell
$ cd .. && cd test-cslib
$ make house
$ ./house
```

This will produce a data file called _graphics.ps_.
