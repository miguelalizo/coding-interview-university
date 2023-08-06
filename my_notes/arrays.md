# Arrays

## [Arrays CS50 Harvard University](https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s)

- Programs and files being run are stored in RAM (able to open files and run programs more quickly if stored in ram)
    - RAM is volatile and requires power to run it (it is purely electrical)
- We can think of RAM as an matrix of bytes in the 'chip'
    - The chip can store some finite number of bytes
    - One bool takes one position in the matrix
    - One int takes 4 bytes
    - One double takes up 8 bytes

**An array is a sequence of values stored in memory back-to-back-to-back**
- For a string (array of chars) there is always one extra char wihc is 0 (ascii for NUL) which symbolizes the end of the string

## [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)

- Arrays have constant time access (read and write access)
- Arrays are contiguous area of memory consisting of equal size elemenets indexed by continuous integers
- Constant time access to any element
- Constant time add/remove at the end O(1)
- Linear time add/remove at an arbitrary location O(n)
    - This occurs bc if you add a new element to the front, you need to shift all the preexisting elements by one location
- Works via the following arythmetic:
    - When retreiving the i-th element of an array:
        - Constant time access = array_addr + element_size x (i - first_index) [ FIRST INDEX IS USUALLY 0 FOR MOTH LANGUAGES]
    - For multi-dim arrays when retreiving the (i, j) index:
        - constant time access = array_addr + eoem_size + ((i - i_first_index)xn + (j - j_first_index))
- 

## [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)]

- In Java, every array is an object consisting of a numbered list of variables
    - Each is a primitive type or a reference to an object
        - primitive types are existing object (char, bool, int, etc.) [not arrays]
    
- 
    ```
    car[] c; //reference (any length of chars)
    c = new char[4];
    c[0] = 'b';
    c[3] = 'e';
    c[4] = 's'; // run-time error (happens during runtimebecause at compile time because java does not know thelength of the array at compile time)
    ```
- Every array has a length field `c.length` 
    - You cannot overwrite this value `c.length=7 // compile time error`
- Sieve of Eratosthenes: method of finding primes
    - All ints are considered prime until proven composite
        - Loop thru all possible divisors and wipe off the primes list all the values they can divide
    - ```
        public static void printPrimes(int n){
            boolean[] prime = new boolean[ n+1]; // declaring an array of size n+1 because when you create an array of size n you will get indexes from [0, n) but we want [0, n]
            for (int i=2; i<=n; i++){
                prime[i] = true;
            }
            for(int divisor=2; divisor*divisor<=n; divisor++){
                if (prime[divisor]) {
                    for (int i=2*divisor; i<=n; i=i+divisor){
                        prime[i] = false;
                    }
                }
            }
            for (int i=2; i<=n; i++){
                if (prime(i)){
                    System.out.println(i);
                }
            }
        }
        ```
- Multidimensional arrays:
    - An array of reference to arrays
    - Exammple: Pascals triangle
    - ```
        import java.util.*;

        public class MyClass {
            public static int[][] pascalTriangle(int n){
                int[][] pascal = new int[n][];
                pascal[0] = new int[1];
                pascal[0][0] = 1;
                
                for (int i=1; i<n; i++){
                    pascal[i] = new int[i+1];
                    pascal[i][0] = 1;
                    for (int j=1; j<i; j++){
                        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
                    }
                    pascal[i][i] = 1;
                }
                return pascal;
            }
            public static void main(String args[]) {
                int[][] arr = pascalTriangle(10);
                for (int i=0; i<arr.length; i++){
                    System.out.println(Arrays.toString(arr[i]));
                }
            }
        }
    ```

## Dynamic Arrays (video)
- Problem with arrays are they are `static`
    - Once you declare it, it's size is fixed
    - You have to determine this size at compile time
- One solution is a dynamically allocatd array
    - You can allocate the array and determine the size of it at runtime
    - Problem: What if you dont know the max size when declaring the array?
        - A solution is using a dynamic array (also known as resizeable array)
        - idea: store a pointer to a dynamically allocated array, and replace it withy a newly-allocated array as needed

- A dynamic array is an abstract data type with the following operations
    - get(i): returns element at location i
    - set(i, val): sets element i to val
        - Both of these operations are constant time access
    - PushBack(val): adds val to the end
    - Remove(i): removes element at location i
    - Size(): returns the number of elements

    - Implementation:
        - Store:
            - arr: dynam,ically-allocated array
            - Capacity: size of the dynamically allocated array (often times not all of the size is used)
            - Size: number of elements `currently` in the array
        - Runtimes
            - Get(i): O(1)
            - Set(i,val): O(1)
            - PushBack(val): O(n)
            - Remove(i): O(n) 

## Jagged Arrays (video) 
AKA Array of Arrays


