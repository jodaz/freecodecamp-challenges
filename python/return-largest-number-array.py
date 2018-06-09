"""
Problem:
Return Largest Numbers in Arrays

Description:
Return an array consisting of the largest number from each provided sub-array. 
For simplicity, the provided array will contain exactly 4 sub-arrays.
Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].
"""

def largest_of_four( arr ):
    largestNums = []

    for i in range( len( arr )):
        num = None
        for j in range( len( arr[ i ])):
            if num == None or num < arr[i][j]:
                num = arr[i][j]
        largestNums.append( num )
    return largestNums

print( largest_of_four([ [4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1] ])) # should return an array.
print( largest_of_four([ [13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]] )) # should return [27,5,39,1001].
print( largest_of_four([ [4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1] ])) # should return [9, 35, 97, 1000000]
    