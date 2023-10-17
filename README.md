# Lab 05 - Functions, Recursion, Higher-order Functions

In this lab, we'll learn how to create functions (including non-recursive and recursive, as well as higher-order functions).

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab05-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will write the `lab05.py` file so that it meets the requirements described in the following sections.  This file has no basic code to start, and it will be up to you to write all of the code for this lab.

#### Part 1

Write a function called `is_vowel` that takes a single argument, a string (`character`) that should contain only a single character.  This function will return  (not to be confused with _print_) `True`, if that character is a vowel, and `False` otherwise.  We'll just consider `a`, `e`, `i`, `o`, and `u` to be vowels for this example.

Example calls to this function, and the return value, are given below:

```python
is_vowel('t')   # returns False
is_vowel('o')   # returns True
is_vowel('u')   # returns True
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 2

Write a function called `count_vowels_iter` that takes a single argument, `sentence`, and returns an integer representing how many vowels are in the `sentence`.  Your function will use a for loop to iterate through each of the letters in `sentence`.  You should use the `is_vowel` function to determine if a given character is a vowel.  Example calls to this function, and the return value, are given below:

```python
count_vowels_iter('this is a sentence')   # returns 6
count_vowels_iter('loud')                 # returns 2
count_vowels_iter('rebel')                # returns 2
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 3

Write a function called `count_vowels_rec` that takes a single argument, `sentence`, and returns an integer representing how many vowels (we'll just consider `a`, `e`, `i`, `o`, and `u` to be vowels for this example) are in the `sentence`.  This function will be identical in function to the `count_vowels_iter` function from part 1.  However, your function will use recursion to go through each of the letters in `sentence`.  

_**Hint:** Each recursive call takes only a single string as its argument.  It will check the first character of that string.  If that character is a vowel, it will count the vowels in the rest of the string recursively (with the first character removed) and add one to it before returning.  If the character is not a vowel, it will count the vowels in the rest of the string recursively, and return that count unmodified._

Example trace:
```
count_vowels_rec('rebel')
 = count_vowels_rec('ebel')          # since 'r' is not a vowel
 = 1 + count_vowels_rec('bel')       # adding 1 since 'e' is a vowel
 = 1 + count_vowels_rec('el')        # since 'b' is not a vowel
 = 1 + (1 + count_vowels_rec('l'))   # adding 1 since 'e' is a vowel
 = 1 + (1 + count_vowels_rec(''))    # since '1' is not a vowel
 = 1 + (1 + 0)                     # since there are zero vowels in an empty string
 = 2
```

Example calls to this function, and the resulting value, are given below:

```python
count_vowels_rec('this is a sentence')   # returns 6
count_vowels_rec('loud')                 # returns 2
count_vowels_rec('rebel')                # returns 2
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 4

Write a function, `my_reduce`, that takes a list of values (`values`, of any type), a starting value (`start_val`), and a binary (two-argument) function (`op`) as its arguments. The function will return a single value such that, starting with `start_val`, the value is combined with each value from the input list (`values`) using the `op` function.

This function should work by initializing the result value (`current_value`) to `start_val`, then
using a loop over the values of the input list (`values`). For each value in `values`, calculate
`op(current_value, value)`, which becomes the new `current_value`. Finally, when the loop
has completed, return `current_value`.

Example calls to this function, and the resulting value, are given below:

```python
values = [1,2,3,4,5]
sum_of_values = my_reduce(values, 0, lambda x,y: x + y)
# sum_of_values should be 15
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._



## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 05 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
