
class Array:
    # Assignment 3.3  

    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        self.shape = shape
        self.items = []
        for value in values:
            self.items.append(value)
  
        if not all(isinstance(item, (int, float, bool)) for item in self.items):
            raise ValueError("Not all elements in Array are the same type")
       

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        #1D array
        if (len(self.shape) == 1):
            return str(self.items)
        #2D array
        elif (len(self.shape) == 2):
            out = "["
            count = 0
            for i in range(self.shape[0]):
                arr = []
                for j in range(self.shape[1]):
                    arr.append(self.items[j + count])
                out += str(arr)
                count += j + 1
                if (i < self.shape[0] - 1):
                    out += ", "
            out += "]"
            return out
        #nD array
        else:
            return NotImplemented

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if not (isinstance(self.items[0], int) or isinstance(self.items[0], float)):
            return NotImplemented

        resultTuple = ()
        if (isinstance(other, Array)):
            if not len(other.items) == len(self.items):
                return NotImplemented
            else:
                for item1, item2 in zip(self.items, other.items):
                    result = item1 + item2
                    resultTuple = resultTuple + (result,)
                return self.__class__(self.shape, *resultTuple)

        elif (isinstance(other, int) or isinstance(other, float)):
            for item in self.items:
                result = item + other
                resultTuple = resultTuple + (result,)
            return self.__class__(self.shape, *resultTuple)

        else:
            return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        if not (isinstance(self.items[0], int) or isinstance(self.items[0], float)):
            return NotImplemented

        resultTuple = ()
        if (isinstance(other, Array)):
            if not len(other.items) == len(self.items):
                return NotImplemented
            else:
                for item1, item2 in zip(self.items, other.items):
                    result = item1 - item2
                    resultTuple = resultTuple + (result,)
                return self.__class__(self.shape, *resultTuple)

        elif (isinstance(other, int) or isinstance(other, float)):
            for item in self.items:
                result = item - other
                resultTuple = resultTuple + (result,)
            return self.__class__(self.shape, *resultTuple)

        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
    
        resultTuple = ()
        for item in self.items:
            result = other - item
            resultTuple = resultTuple + (result,)
        return self.__class__(self.shape, *resultTuple)


    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        if not (isinstance(self.items[0], int) or isinstance(self.items[0], float)):
            return NotImplemented

        resultTuple = ()
        if (isinstance(other, Array)):
            if not len(other.items) == len(self.items):
                return NotImplemented
            else:
                for item1, item2 in zip(self.items, other.items):
                    result = item1 * item2
                    resultTuple = resultTuple + (result,)
                return self.__class__(self.shape, *resultTuple)

        elif (isinstance(other, int) or isinstance(other, float)):
            for item in self.items:
                result = item * other
                resultTuple = resultTuple + (result,)
            return self.__class__(self.shape, *resultTuple)

        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """

        if (isinstance(other, Array)):
            if not len(other.items) == len(self.items):
                return False
            else:
                for item1, item2 in zip(self.items, other.items):
                    if item1 != item2:
                        return False
                return True

        else:
            return NotImplemented

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        if not (isinstance(self.items[0], int) or isinstance(self.items[0], float)):
            return NotImplemented

        resultTuple = ()
        if (isinstance(other, Array)):
            if not len(other.items) == len(self.items):
                return NotImplemented
            else:
                for item1, item2 in zip(self.items, other.items):
                    result = item1 == item2
                    resultTuple = resultTuple + (result,)
                return self.__class__(self.shape, *resultTuple)

        elif (isinstance(other, int) or isinstance(other, float)):
            for item in self.items:
                result = item == other
                resultTuple = resultTuple + (result,)
            return self.__class__(self.shape, *resultTuple)

        else:
            return NotImplemented
    
    def mean(self):
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        if not (isinstance(self.items[0], int) or isinstance(self.items[0], float)):
            return NotImplemented

        return sum(self.items)/len(self.items)

    def variance(self):
        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        if not (isinstance(self.items[0], int) or isinstance(self.items[0], float)):
            return NotImplemented

        return sum((item - self.mean()) ** 2 for item in self.items) / len(self.items)

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
        return min(self.items)

    def __getitem__(self, key):
        return self.items[key]