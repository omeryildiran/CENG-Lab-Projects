In this lab, you are asked to implement a function called find_extremities. The function definition is as follows:

find_extremities(big_list, mode)

big_list: A list containing lists of strings that represents integers, e.g. [lst1, lst2, ...] and lst1 = ["10", "85", ...].
mode: A string. Either "max" or "min".
The function should return a list containing:

A list (say return_list) that either contains maximum or minimum (as specified by the mode argument) element as integers from each list (lst1, lst2, ...) inside big_list.
A float that is the average of the integers in the return_list that you should return.
Notes:

Mode argument ("max" or "min") determines whether you should select maximum or minimum values from each list.
There will be at least one list inside of big_list and that list will have at least 1 element (i.e. no argument such as [[]]).
Warnings:

Your function should receive its data via its parameters only. Your submitted solution must NOT use any input() function.
Your function should return its results. Your submitted solution must NOT print anything.
Any return value that doesn't conform to the expected output type will be graded as zero.
The order of integers in the return_list does not matter as long as all the (necessary) integers are included in the list.
When using the emulator given with the link at the bottom, due to a small problem the result of a division can be shown as integer instead of a float (this happens only when the remainder is 0, e.g. 6/2.0 is shown as 3 instead of 3.0 still numerically correct) but this wont affect your grades since it is only a visual problem in emulator. Make sure that you use correct data types when performing the arithmetic operations and your result will be correct.