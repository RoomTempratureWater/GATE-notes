- Data words are organised in a table (row and columns) (2D matrix)
- For each row and column, one parity check bit is calculated
- It guarantees to correct **one-bit** errors and **detect upto 3 bit errors**


Ex below: lets assume we are sending 4 datawords of 7 bits each

|               |     |
| ------------- | --- |
| 1 0 1 1 0 1 0 | 0   |
| 1 1 1 1 1 0 1 | 0   |
| 1 0 1 0 0 0 1 | 1   |
| 1 0 1 1 0 1 1 | 1   |
| 0 1 0 1 1 0 1 | 0   |
we are making each datawords even (like [[CN/Simple Parity Check Code|Simple Parity Check Code]])


Disadvantage of this is that error can obviously also be in the parity bits and therefore it isn't used much in  computer networks nowadays