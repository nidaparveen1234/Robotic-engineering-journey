1.	First, we set a list.
	2.	We set k equal to our rotation value.
	3.	We set n equal to the length of the list.
	4.	If k is greater than n, or if k modulo n is required, then we do
k = k - n (or effectively reduce k).
	5.	Since k is now set properly, we will do rotation k times.
	6.	We have already created a right rotation logic, so this will go to that logic.
	7.	In each rotation, the last element will move to the first position.
	8.	This process repeats until all k rotations are completed.
	9.	Finally, we print the rotated list.
	10.	If k is not greater than n, we do the normal rotation directly.
