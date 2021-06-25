You are working for a flower shop and your company decided to open an online shop due to the Covid-19 pandemic. Your job is to implement a part of the online shopping software. Specifically;



- You will read 3 numbers one by one. First one will encode the flower name, second one will encode the color of the flower(s), third one will encode the amount of flowers.



- Encoding for the flower name is as such:

          • If the most significant digit (the leftmost digit) of the first number is 7, the requested flower is Rose,

          • if the most significant digit (the leftmost digit) of the first number is 8, the requested flower is Tulip,

          • otherwise the requested flower is Orchid.



- Encoding for the color is as such:

          • If the least significant digit (the rightmost digit) of the second number is 0, 1, 2 or 3 the color is White,

          • if the least significant digit (the rightmost digit) of the second number is 4, 5 or 6 the color is Pink,

          • if the least significant digit (the rightmost digit) of the second number is 7, 8 or 9 the color is Red.



- There is no actual encoding for the number of flowers. The third number will directly be the number of flowers ordered by the customer. However, there are such restrictions about flower amounts:

          • At most 100 Roses can be ordered at once. If more than 100 Roses are requested, the order is Invalid.

          • At most 50 Tulips can be ordered at once. If more than 50 Tulips are requested, the order is Invalid.

          • At most 30 Orchids can be ordered at once. If more than 30 Orchids are requested, the order is Invalid.



- At the end, you will print the order information as such:

          • If the order is invalid, you will print "Invalid!"

          • If the order is valid, you will print flower name, flower color and the amount without spaces. For example for 10 pink roses you will print "RosePink10". (Yes, flower name and the color will start with uppercase letters.)

