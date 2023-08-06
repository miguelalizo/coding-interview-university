# Asymptotic Complexity - Big-O

Left to do:
- Take notes on the concepts in Cracking the coding interview
- Make flashcards of all the important concept

## [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?)

### What does it mean for an algorithm to be fast/efficient?

- We cant directly compare algorithms directly using runtime in seconds or minutes (diue to hw and sw environment differences)

### Big O notation 

- A way of analyzing how fast a program grows asymtotically 
    - As the size of your input increase, how does the runtime of an algorithm grow?

Example: 
    - Counting the letters in a string: "cat"
    - Each character takes the same amount of time to  count, and so the runtime will increase with increasing length of string, n
    - Runtime for an algorithm that counts chars in a str is O(n), linear time

What if you save the length of the str into an int?
    - Now the program to find the length of the str runs in constant time O(1) as it doesnt depend on the length of the str (asymtoticlly constant runtime)

#### Different Runtimes

O(n^2)
    - Increases with the square of n. Not always slower than O(n) but specizlly for larger inputs it will always be less efficient than O(n)

O(log(n))
    - Example: binary search. With every operation, the input size is reduced by half. 
    - Doubling the size of the array only increases the runtime by one operation


### Best case time complexity $\Omega$ 

For the binary search example, the best case is searching for the element in the middle of the array, which would take 1 operation
    - Denoted as $\Omega$(1) 

### Best and worst case are the same time complexity $\Theta$

When best and worst run times are the same

Example: Retreiving a variable is $\Omega$(1) = O(1) thus $\Theta(1)$


## [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)

Big-O is a way of measduring how well an algorithm scales as the size of the input increases

- [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)

### Big-O Mathematical definition
- f(n) is O(g(n)) IF there exists a C and n0 where f(n)<=Cg(n) for all n>n0

Example: Is f(n) 0(n^2) ? 
    - when 5 is 5 and n0 is 6
    - f(n) = 4n^2 + 16n + 2 <= 5n^2 
    - YES


### Big-$\Omega$ Mathematical definition
- f(n) is $\Omega$(g(n)) IF there exists a C and n0 where f(n)>=Cg(n) for all n>n0

Example: Is f(n) $\Omega$(n^2) ? 
    - when C is 1 and n0>=0
    - f(n) = 4n^2 + 16n + 2 <= 1n^2 
    - YES

### Big-$\Theta$ Mathematical definition
- f(n) is $\Theta$(g(n)) IFF:
    - f(n) is O(g(n))
    - f(n) is $\Omega$(g(n))

Example:
- f(n) = 4n^2 + 16n + 2 <= 5n^2 
- f(n) IS 0(n^2)
- f(n) $\Omega$(n^2)
- therefore YES f(n) is $\Theta$(g(n))

## [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)

A potential function $\phi$ that maps each data structure Di to a real number $\phi$(Di) which is the potential associated with the data structure Di*D0 = 0 and Di>=0 for all i?0





- [ ] [Skiena (video)](https://www.youtube.com/watch?v=z1mkCe3kVUA)
- [ ] [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [ ] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20one)
    - [Computational Complexity: Section 2](https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20two)
- [ ] [Cheat sheet](http://bigocheatsheet.com/)
- [ ] [[Review] Big-O notation in 5 minutes (video)](https://youtu.be/__vX2sjlpXU)