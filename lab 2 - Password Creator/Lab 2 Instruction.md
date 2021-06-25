#Lab 2

In this lab, we will perform simple string manipulation:

You will first read 3 username and password pairs, one by one. Let us call the usernames u1, u2, u3 and the passwords p1, p2 and p3. To be more specific, you will read them exactly in this order: u1, p1, u2, p2, u3, p3. Note that p1 is u1's password, p2 is u2's and p3 is u3's.

Then, you will read a username (let us call this uX) which is equal to one of the usernames (u1, u2, u3) you have read in the first step.

Afterwards, you are expected to create a new password using the selected username (uX) and its password (pX) as follows:

The first 4 characters ([0,3]) of the new password should be the last 4 characters of the corresponding username (uX).

You should get the last 5 characters of the password (pX) in reverse order and write the reversed string into the new password starting from the 4th index (i.e. indices 4,5,6,7,8 will have the reversed string).

Starting from the 9th index of the new string, append the square of the length of the password pX mod 100 (i.e., "len(pX)**2 % 100") to the end of the new password.

Print the new password on screen.