# magic_square
```
def is_magic_square(magic_square):
    """
        Check if matrix is a magic square
        @param magic_square - ordered matrix to be analyzed if magic or not
        @return - True  if magic square False otherwise
    """
def odd(order,starting_number=1,increment=1,number_of_shuffles=0):
    """
    @param order: ODD order of the magic square
    @param starting_number: Starting number to be used to generate the magic square. Default=1
    @param increment: Number increment to be used to generate the magic square. Default=1
    @param number_of_shuffles: Default = 0 - do not shuffle the generated magic square
                               Any number upto order - 1 shuffle that many times 
                               None => shuffled random number of times
    @return magic square
    """
def multiples_of_four(order,starting_number=1,increment=1,number_of_shuffles=0):
    """
    @param order: order of the magic square (IN MULTIPLES OF FOUR)
    @param starting_number: Starting number to be used to generate the magic square. Default=1
    @param increment: Number increment to be used to generate the magic square. Default=1
    @param number_of_shuffles: Default = 0 - do not shuffle the generated magic square
                               Any number upto order - 1 shuffle that many times 
                               None => shuffled random number of times
    @return magic square
    """
def even_non_multiples_of_four(order,starting_number=1,increment=1,number_of_shuffles=0):
    """
    @param order: EVEN order of the magic square (BUT NOT MULTPLES OF FOUR)
    @param starting_number: Starting number to be used to generate the magic square. Default=1
    @param increment: Number increment to be used to generate the magic square. Default=1
    @param number_of_shuffles: Default = 0 - do not shuffle the generated magic square
                               Any number upto order - 1 shuffle that many times 
                               None => shuffled random number of times
    @return magic square
    """
def shuffle(magic_square,number_of_shuffles=1):
    """
    Shuffle the given matrix without changing its determinant
    @param magic_square: the matrix to shuffled 
    @param number_of_shuffles: Default = 1 - shuffle once row and column
                               Any number up to "order" - shuffle that many times 
                               None => shuffled random number of times
    @return shuffled magic square
    """
def generate(order,starting_number=1,increment=1,number_of_shuffles=0):
    """
    @param order: order of the magic square
    @param starting_number: Starting number to be used to generate the magic square. Default=1
    @param increment: Number increment to be used to generate the magic square. Default=1
    @param number_of_shuffles: Default = 0 - do not shuffle the generated magic square
                               Any number upto order - shuffle that many times 
                               None => shuffled random number of times
    @return magic square
    """
```
## Example
```
    order  = 6
    starting_number = 2
    increment = 2
    ending_number = _ending_number(order, starting_number, increment)
    number_of_shuffles = 0
    magic_square,magic_const = generate(order,starting_number,increment,number_of_shuffles)
```
