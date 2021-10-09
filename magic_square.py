from scipy.optimize import brute
import random
from sys import stdout
import numpy as np

def _is_multiple_of(number1, number2=4):
    return (number1 % number2) == 0
def _is_odd(number):
    return not _is_multiple_of(number,2)
def _ending_number(order,starting_number=1,increment=1):
    return (increment*(order*order-1))+starting_number
def magic_sum(order,starting_number=1,increment=1):
    m = order*order
    mc = int(m/2*(2*starting_number+(m-1)*increment)/order)
    return mc
def _magic_sum(magic_square):
    if _is_magic_square_new(magic_square):
        return sum(magic_square[0])
    print("Not a magic square")
    exit()
def _is_even_order(magic_square):
    return len(magic_square)==len(magic_square[0])
def _is_magic_square_new(magic_square):
    """ TDOD not working yet """
    order = len(magic_square)
    sum_rows = list(sum(list(iter(magic_square))))
    sum_columns = [sum(col) for col in zip(*magic_square)] #zip(*magic_square)  # this is a beautiful idiom! Learn it!
    diagonals = list(zip(*[(magic_square[i][i], magic_square[-i-1][i]) for i in range(order)]))
    return sum_rows.count(sum_rows[0])==len(sum_rows) == sum_columns.count(sum_columns[0])==len(sum_columns) and \
            sum(diagonals[0])==sum(diagonals[1])
def is_magic_square(magic_square):
    """
        Check if matrix is a magic square
        @param magic_square - ordered matrix to be analyzed if magic or not
        @return - True  if magic square False otherwise
    """
    if not _is_even_order(magic_square):
        return False
    order = len(magic_square[0])
    sum_list = []
    sum_list.extend([sum(rows) for rows in magic_square])
    sum_cols = []
    for col in range(order):
        sum_list.append(sum(row[col] for row in magic_square))
    result1, result2 = (0,0)
    for i in range(0,order):
        result1 +=magic_square[i,i]
    sum_list.append(result1)      
    for i in range(order-1,-1,-1):
        result2 +=magic_square[i,i]
    sum_list.append(result2)
    magic_sum = set(sum_list)
    if len(magic_sum)>1 and magic_sum != result1:
        return False
    return True
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
    if not _is_odd(order):
        print("Number:"+str(order)+" is not add")
        exit()
    magic_square = np.zeros((order,order), dtype=int)
    ending_number = _ending_number(order,starting_number,increment)
    n = starting_number
    i, j = 0, order//2
    
    while n <= ending_number:
        magic_square[i, j] = n
        n += increment
        newi, newj = (i-1) % order, (j+1) % order
        if magic_square[newi, newj]:
            i += 1
        else:
            i, j = newi, newj
    sum_of_magic_square = magic_sum(order,starting_number,increment)
    if number_of_shuffles!=0:
        magic_square = shuffle(magic_square, number_of_shuffles)
    return magic_square
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
    if not _is_multiple_of(order, 4):
        print("Number:"+str(order)+" is not multiple of FOUR")
        exit()
    ir = 0
    row_start = 0
    row_end = row_start + order - 1
    column_start = 0
    column_end = column_start + order - 1
    ending_number = _ending_number(order, starting_number,increment)
    magic_square = np.zeros((order,order), dtype=int)
    for row in range(row_start,row_end+1):# For r = row_start To row_end
        ir = ir + 1
        ic = 0
        i = (row - row_start + 1) % 4
        if i == 0:
            i = 4
        for column in range(column_start,column_end+1): #For c = column_start To column_end
            ic = ic + 1
            ncr = ((((ir - 1) * order) + (ic - 1)) * increment) + starting_number
            j = (column - column_start + 1) % 4
            if j == 0:
                j = 4
            if (i == j) or (i + j == 5):
                magic_square[row,column] = ncr
            else:
                magic_square[row,column] = ending_number + starting_number - ncr
    sum_of_magic_square = magic_sum(order,starting_number,increment)
    if number_of_shuffles!=0:
        magic_square = shuffle(magic_square, number_of_shuffles)
    return magic_square
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
    if _is_odd(order) or _is_multiple_of(order, 4):
        print("Number:"+str(order)+" should be even and not multiple of 4")
        exit()
    magic_square = np.zeros((order,order), dtype=int)
    z = order // 2
    b = z * z * increment
    c = 2 * b
    d = 3 * b
    inner_odd_square = odd(z,starting_number,increment) # build_oms(z)
    for j in range(0, z):
        for i in range(0, z):
            a = inner_odd_square[i,j]
            magic_square[i,j] = a
            magic_square[i + z,j + z] = a + b
            magic_square[i + z,j] = a + c
            magic_square[i,j + z] = a + d
    lc = z // 2
    rc = lc
    swap_cells = lambda i,j,lc,order,rc : (not (i == 0 and j == lc)) and ( (i < lc) or (i > order - rc) or ( (i == lc) and (j == lc) ) )
    for j in range(0, z):
         for i in range(0, order):
              if swap_cells(i,j,lc,order,rc):
                  magic_square[i,j], magic_square[i,j+z] = magic_square[i,j+z],magic_square[i,j]
    sum_of_magic_square = magic_sum(order,starting_number,increment)
    if number_of_shuffles!=0:
        magic_square = shuffle(magic_square, number_of_shuffles)
    return magic_square
def _subtract_from_max(magic_square,increment=1):
    last_number = np.max(magic_square)
    magic_square = np.array([last_number+increment-x for x in magic_square])
    return magic_square
def shuffle(magic_square,number_of_shuffles=1):
    """
    Shuffle the given matrix without changing its determinant
    @param magic_square: the matrix to shuffled 
    @param number_of_shuffles: Default = 1 - shuffle once row and column
                               Any number up to "order" - shuffle that many times 
                               None => shuffled random number of times
    @return shuffled magic square
    """
    if number_of_shuffles==None:
        order = len(magic_square)
        number_of_shuffles = random.randrange(1,order)
    number_of_shuffles = min(order-1,number_of_shuffles)
    for shuffles in range(number_of_shuffles):
        rand_row_col_1 = random.randrange(order)
        rand_row_col_2 = random.randrange(order)
        magic_square[:,[rand_row_col_1,rand_row_col_2]] = magic_square[:,[rand_row_col_2,rand_row_col_1]]
        magic_square[[rand_row_col_1,rand_row_col_2],:] = magic_square[[rand_row_col_2,rand_row_col_1],:]
    return magic_square
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
    if _is_odd(order):
        magic_square= odd(order,starting_number,increment) # build_oms(N)
    elif _is_multiple_of(order,4):
        magic_square = multiples_of_four(order,starting_number,increment)#, start_number, increment)
    else:
        magic_square = even_non_multiples_of_four(order,starting_number,increment)
    sum_of_magic_square = magic_sum(order, starting_number, increment)
    if number_of_shuffles!=0:
        magic_square = shuffle(magic_square, number_of_shuffles)
    return magic_square, sum_of_magic_square
def _is_perfect(magic_square):
    order = len(magic_square)
    if not _is_multiple_of(order, 4):
        print("Order",order,' should be multiple of FOUR')
        return False
    z = order // 2
    inner_matrix_sums = []
    inner_matrix_sums.append( sum([ magic_square[i,j] for j in range(0, z) for i in range(0, z) ]))
    inner_matrix_sums.append( sum([ magic_square[i + z,j + z] for j in range(0, z) for i in range(0, z) ]))
    inner_matrix_sums.append( sum([ magic_square[i + z,j] for j in range(0, z) for i in range(0, z) ]))
    inner_matrix_sums.append( sum([ magic_square[i,j + z] for j in range(0, z) for i in range(0, z) ]))
    return inner_matrix_sums.count(inner_matrix_sums[0])==len(inner_matrix_sums)
def _is_most_perfect(magic_square):
    order = len(magic_square)
    magic_sum = order // 4
    slice_length = 2
    slice = sum(list([ magic_square[i:i+slice_length,j:j+slice_length] for i in range(0,order,slice_length) for j in range(0,order,slice_length)]))
    print('slice\n',slice)
    magic_sum = _magic_sum(magic_square)
    return magic_sum*magic_sum == slice[0,0]
def multiples_of_four_new(order,starting_number=1,increment=1,number_of_shuffles=0):
    """
    @param order: order of the magic square (IN MULTIPLES OF FOUR)
    @param starting_number: Starting number to be used to generate the magic square. Default=1
    @param increment: Number increment to be used to generate the magic square. Default=1
    @param number_of_shuffles: Default = 0 - do not shuffle the generated magic square
                               Any number upto order - 1 shuffle that many times 
                               None => shuffled random number of times
    @return magic square
    """
    if order < 4 or order%4: return False    #only allow even squares 4n, n>0

    c, cms, magic_square = starting_number, order*order*increment + starting_number, [[0]*order for i in range(order)]
    print(magic_square)
    for i in range(order):
        for j in range(order):
            magic_square[i][j] = cms-c if i%4 == j%4 or (i+j)%4 == (order-1)%4 else c
            c += increment
    print(magic_square)
def _magic_minimize_brute(x:int,sum,n):
    error = abs(sum-n*(2*x[0]+(n*n-1)*x[1])//2)
    return error    
def generate_for_given_sum_and_order(sum,order=3):
    """
    Generate a magic square closest to given order and sum
    @param sum:     sum of the to-be generated magic square
    @param order:   order of the to-be generated magic square
    @return    closes possible magic square
    """
    magic_square=[]
    min_sum = magic_sum(order,1,1)
    if sum < min_sum: #sum % order !=0 or 
        print('Requested sum ',sum,'should be more than or equal to',min_sum,'for order',order,'in steps of',order)
        sum = min_sum
    ranges = (slice(1, 100, 1),) * 2
    starting_number,increment = brute(_magic_minimize_brute,ranges, args=[sum,order], disp=True, finish=None)
    magic_square,actual_sum = generate(order,starting_number,increment)
    return magic_square,starting_number,increment,actual_sum
if __name__ == "__main__":
    order = 12
    magic_const = 700
    #import time
    #start_time = time.process_time()
    magic_square,starting_number,increment,actual_sum = generate_for_given_sum_and_order(magic_const,order)
    #end_time=time.process_time()
    #print("processing time",end_time-start_time,'seconds')
    if actual_sum !=0:
        print('magic square of order',order,' has sum',actual_sum,'with starting number,increment',(starting_number,increment),"\n",magic_square)
    
    exit()
    order  = 6
    starting_number = 2
    increment = 2
    ending_number = _ending_number(order, starting_number, increment)
    number_of_shuffles = 0
    #import timeit
    #print(timeit.timeit("generate(order,starting_number,increment,number_of_shuffles)", setup="from __main__ import generate,order,starting_number,increment,number_of_shuffles",number=1000))
    magic_square,magic_const = generate(order,starting_number,increment,number_of_shuffles)
    print('magic square of order',order,' has sum',magic_const,'with ending number',ending_number,"\n",magic_square)
    print('is_magic_square',is_magic_square(magic_square))
    #exit()
    
    order  = 7
    starting_number = 3
    increment = 3
    ending_number = _ending_number(order, starting_number, increment)
    number_of_shuffles = 0
    magic_square,magic_const = generate(order,starting_number,increment,number_of_shuffles)
    
    print('magic square of order',order,' has sum',magic_const,'with ending number',ending_number,"\n",magic_square)
    print('is_magic_square',is_magic_square(magic_square))

    order  = 8
    starting_number = 4
    increment = 4
    ending_number = _ending_number(order, starting_number, increment)
    number_of_shuffles = 0
    magic_square,magic_const = generate(order,starting_number,increment,number_of_shuffles)
    
    print('magic square of order',order,' has sum',magic_const,'with ending number',ending_number,"\n",magic_square)
    print('is_magic_square',is_magic_square(magic_square))
