
Error checking is more efficient than error correction, if an error is found, we just ask to send that data again


## Logic for error checking

In most error checking algorithms, we add some ***Redundant*** bits to the data.
so for example,

10111 can be sent as 10111 0 with the last bit as the redundant bit or a parity bit 

we can then use this parity bit to determine the error

## Hamming Distance

hamming distance is the difference in bits between 2 binary strings

so *d(101, 100) = 1* since only 1 bit is different
P.S ->  the size of the strings has to be same for comparison, add 0's infront to make them equal in size.

hamming distance can be calculated by doing an *XOR operation on the strings and then count the number of 1's in the result*

(XOR = dono different = 1, dono same = 0)

