- [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&
- Dictionary:
    - Abstract data structure
    - Can insert, delete, and search(key) 
- Python:
    - D[key] -> search
    - D[key]=val -> insert
    - del D[key] -> delete
    - item is a pair (key, value)
- Motivation for building dicts:
    - databases sometimes are implemented using hash tables
    - Network routers have dicts for looking up the machines in the nertwork (to route requests and such)
- Simple approach:
    - Direct access table
        - Store items in an array, indexed by keys
    - Why this approach is bad:
        1. Index might not be integers
        2. Takes a lot of memory
    - Solution to 1: prehashing (python calls it hashing)
        - maps keys to non-negative integers 
        - In theory, keys are finite and discrete (striong of bits)
        - In python, hash(x) is the **prehash of x**
            - ideally, hash(x) = hash(y) only when x=y
            - If you define a custom class in python, __hash__ tells python what to do when you call hash(custom_object)
            - Mutable objects cannot be keys of a hashtable because they change over time
    - Solution to 2: hashing
        - reduce universe U of all keys (integers) down to reasonable size m for table
            - Basically, prehash the keys such that then a table of hopefully proportional to the number of keys can be created with the prehash as the key and the respective value for that key as the value
                - EX: Say integer key is 12345 and value you want to store is "cat", the hash table would then become: key: prehash(1234), value: "Cat"
        - Problems with this:
            - The is guaranteed to be 2 keys that match up to the same place in the hash table (vbecause all the possible keys are much greater than the size of the used keys and therefore the hashmap)
                - This is called a collision

    - Techniques to deal with collisions:
        - Chaining:
            - The idea is if you have multiople values in the 

    *** need to finish notes, rewatch and understand ***

- [PyCon 2010: The Mighty Dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)


- [ ] [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)

- [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - Karp Rabin string matching algorithm
        - Assumptions: 
            - We have a data structure that will compute the hash value every time you append a value
            - Also needs to be able to append and popFront in constant time O(1)
                - What data structure can do this?
        - First need to compute hash value of s
        ```python
        # rs the hash value of s, this only needs to be computed once
        # so we do it by appending every char in s to rs and computing the rolling hash each time
        for c in s:
            rs.append(c) 

        # now we want to get started an compute the hash function of the first s characters in t
        for c in t[:len(s)]
            rt.append(c) # rt is rolling hash of t

        if rs()==rt(): ... # check if they are equal

        for i in range(len(s), len(t)):
            rt.skip(t[i-len(s)])
            rt.append(t[i])

            # if hash values are equal
            if rs==rt:
                # check char by char if the stirngs are the same because this matcxh in hash values could be a collision
                # this check takes O(s) time
                s==t[i-len(s)+1:i+1]
            else:
                # we engineer this such that this happens with probability of at most 1/s
                # so that this takes O(1)
        ```
        - this takes: O(|s|+|t| + #of_hash_value_maches*|s|) 
            - expected time
        - We can use division method as a hash function
            - this is the prehash function
        - division method: h(k) = k mod n
                - where n is a random prime at least the size of |s|
        - Note: We will treat the string x as a multidigit number u in a base a ( the base is needs to be the size of your alphabet - for asccii then a=256)
            - the multidigit number representation of the string is based on the length of the string
                - we do this so that when we add a value, it is like taking the number ####, shifting it over by one, ####_, and adding the new value ##### (where the rightmost hashtag is the newest)
                - to shift over by one, multiply by `a` then we add the number representation of the new char c to append (in python this is `ord(c)`)
                - if we have some current number represented by the string in base a, `U`, then we shift it over by performing U*a then we add the new char with ord(c)
                    - `U*a + ord(c)`
                - to popleft, we do `U- c*a^(|u|-1)`
            - so to get the new hash value r, for the append we compute `r-> r*a+ord(c) mod m`
            - and we do the same thing for the popLeft as `r-> r-c*a^(|u|-1)` which gives us the new hash value
            - all of this takes constant time O(1)
        - r stores the current hash value of the string and it stores `a^(|u|-1)`

