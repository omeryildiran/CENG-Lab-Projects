VENDING MACHINE (VM)

You are to implement a program that simulates a vending machine (VM). Your program will read three pieces of data in the following order:

A dictionary, representing the current stock of the VM. The keys of the dictionary are item names (as strings) and the prices as integers. You can assume the stock is limitless for the items in the VM. E.g.:

{"chocolate": 2, "spring_water": 1, "energy_drink": 7}

A list of strings, representing the items requested by the customer. Repeating an item's name means requesting a second from that item, e.g.:

["energy_drink", "chips", "chocolate", "chocolate"]

If a requested item is not in the VM, your VM should ignore it.

An integer, representing the amount of money inserted by the customer.

After these three inputs, your VM should calculate the total price of the items requested and should print one of the following:

"Change:X" if the money inserted is higher than the total price of the requested items. The integer X is the amount of money that the customer needs to get back.

"Insert:X" if the money inserted is less than the total price of the requested items. The integer X is the amount of extra money that the customer needs to insert.

"Done", if the inserted money and the total price of the requested items are equal to each other.