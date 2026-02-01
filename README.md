

     ....... Data Structure and Algorithms .................
------------------------------------------------------------
------------------------------------------------------------
Characteristics of a Data Structure

    - Correctness      > Data structure implementation should implement its interface correctly.

    - Time Complexity  > Running time or the execution time of operations of data structure must be as small as possible.

    - Space Complexity > Memory usage of a data structure operation should be as little as possible.

Execution Time Cases

    - Worst Case   > This is the scenario where a particular data structure operation takes maximum time it can take. If an operation's worst case time is ƒ(n) then this operation will not take more than ƒ(n) time where ƒ(n) represents function of n.

    - Average Case > This is the scenario depicting the average execution time of an operation of a data structure. If an operation takes ƒ(n) time in execution, then m operations will take mƒ(n) time.

    - Best Case    > This is the scenario depicting the least possible execution time of an operation of a data structure. If an operation takes ƒ(n) time in execution, then the actual operation may take time as the random number which would be maximum as ƒ(n).

Basic DSA Terminologies

    - Data                 >  Data are values or set of values.

    - Data Item            >  Data item refers to single unit of values.

    - Group Items          > Data items that are divided into sub items are called as Group Items.

    - Elementary Items     > Data items that cannot be divided are called as Elementary Items.

    - Attribute and Entity > An entity is that which contains certain attributes or properties, which may be assigned values.

    - Entity Set           > Entities of similar attributes form an entity set.

    - Field                > Field is a single elementary unit of information representing an attribute of an entity.

    - Record               > Record is a collection of field values of a given entity.

    - File                 > File is a collection of records of the entities in a given entity set.


    :: 1 ::   Time and Space complexities
    .........................................
    - Space Complexity
        Space complexity of an algorithm represents the amount of memory space required by the algorithm in its life cycle. 
        The space required by an algorithm is equal to the sum of the following two components
        1- A fixed part that is a space required to store certain data and variables,
            that are independent of the size of the problem. For example, simple variables and constants used, program size, etc.
        2- A variable part is a space required by variables, whose size depends on the size of the problem. 
            For example, dynamic memory allocation, recursion stack space, etc.
    - Time Complexity
        https://www.tutorialspoint.com/data_structures_algorithms/asymptotic_analysis.htm
        https://www.geeksforgeeks.org/dsa/time-complexity-and-space-complexity/
        
    

        


    :: 2 ::   Data Structure 
    .............................................................
    - Types of Data Structures  =======>
    -------------------------------------------------------------
    **  Data Definition
        Data Definition defines a particular data with the following characteristics.

        -  Atomic Definition should define a single concept.

        -  Traceable Definition should be able to be mapped to some data element.

        -  Accurate Definition should be unambiguous.

        -  Clear and Concise Definition should be understandable.
    **  Data Type
        -  Built-in Data type
            - Integers
            - Boolean ( True , False)
            - Floating ( Decimal numbers )
            - Character and Strings
        -  Derived Data Type
            - List
            - Array
            - Stack
            - Queue
    ** Basic Operations 
        -  Traversing
        -  Searching
        -  Insertion
        -  Deletion
        -  Sorting
        -  Merging
    **  Types of Data Structures 
        -  Linear Data Structure
            -  Array
            -  Linked List
            -  Stack
            -  Queue    
        -  Non-Linear Data Structure
            -  Tree
            -  Graph
            -  Tries
            -  Maps
    2.1 - Array Data Structure
            - Basic Operations on Array
                - Traverse  >>> print all the array elements one by one.
                    >>>>>>> This operation traverses through all the elements of an array. We use loop statements to carry this out.
                        1  Start
                        2. Initialize an Array of certain size and datatype.
                        3. Initialize another variable i with 0.
                        4. Print the ith value in the array and increment i.
                        5. Repeat Step 4 until the end of the array is reached.
                        6. End

                - Insertion >>> Adds an element at the given index
                    >>>>>>> An algorithm to insert elements into a Linear Array until we reach the end of the array 
                        1. Start
                        2. Create an Array of a desired datatype and size.
                        3. Initialize a variable 'i' as 0.
                        4. Enter the element at ith index of the array.
                        5. Increment i by 1.
                        6. Repeat Steps 4 & 5 until the end of the array.
                        7. Stop
  
                - Deletion  >>> Deletes an element at the given index.
                    >>>>>>> In this array operation, we delete an element from the particular index of an array
                        1. Start
                        2. Set J = K
                        3. Repeat steps 4 and 5 while J < N
                        4. Set LA[J] = LA[J + 1]
                        5. Set J = J+1
                        6. Set N = N-1
                        7. Stop

                - Search    >>> Searches an element using the given index or by the value.
                    >>>>>>> 
                        1. Start
                        2. Set J = 0
                        3. Repeat steps 4 and 5 while J < N
                        4. IF LA[J] is equal ITEM THEN GOTO STEP 6
                        5. Set J = J +1
                        6. PRINT J, ITEM
                    >>>>>>> Python Example

                - Update    >>> Updates an element at the given index
                    >>>>>>> refers to updating an existing element from the array at a given index.
                        1. Start
                        2. Set LA[K-1] = ITEM
                        3. Stop
                      
                - Display   >>> This operation displays all the elements in the entire array using a print statement
                    >>>>>>> print all elements inside the array
                        1. Start
                        2. Print all the elements in the Array
                        3. Stop
                    >>>>>>> Python Example
                        #Declaring array elements
                        LA = [2,3,4,5,6]
                        #Displaying the array
                        print("The array elements are: ")
                        for x in range(len(LA)):
                            print("LA", [x], " = " , LA[x])
                        
    2.2 - String Data Structure

    2.3 - Linked List Data Structure

    2.4 - Double Linked List Data Structure

    2.5 - Circular Linked List Data Structure

    2.6 - Stack Data Structure

    2.7 - Queue Data Structure

    2.8 - Heap Data Structure

    2.9 - Hash Data Structure

    2.10- Matrix/Grid Data Structure

    2.11- Graph Data Structure

    2.12- Tree Data Structure
--------------------------------------------------------------------------
    :: 3 ::   Algorithms     =======>
    ......................................................................
    **  Algorithm is a step-by-step procedure, which defines a set of instructions to be executed 
        in a certain order to get the desired output

    **  important categories of algorithms     
        -   Search Algorithm to search an item in a data structure.

        -   Sort Algorithm to sort items in a certain order.

        -   Insert Algorithm to insert item in a data structure.

        -   Update Algorithm to update an existing item in a data structure.

        -   Delete Algorithm to delete an existing item from a data structure.
    
    **  Characteristics of an Algorithm

        -   Not all procedures can be called an algorithm. An algorithm should have the following characteristics −

        -   Unambiguous Algorithm should be clear and unambiguous. Each of its steps (or phases), and their inputs/outputs should be clear and must lead to only one meaning.

        -   Input An algorithm should have 0 or more well-defined inputs.

        -   Output An algorithm should have 1 or more well-defined outputs, and should match the desired output.

        -   Finiteness Algorithms must terminate after a finite number of steps.

        -   Feasibility Should be feasible with the available resources.

        -   Independent An algorithm should have step-by-step directions, which should be independent of any programming code.

    **  Algorithm Analysis
        
        -   A Priori Analysis This is a theoretical analysis of an algorithm. Efficiency of an algorithm is measured by assuming that all other factors, for example, processor speed, are constant and have no effect on the implementation.

        -   A Posterior Analysis This is an empirical analysis of an algorithm. The selected algorithm is implemented using programming language. This is then executed on target computer machine. In this analysis, actual statistics like running time and space required, are collected.
    
    **  Algorithm Complexity

        -   Time Factor.  Time is measured by counting the number of key operations such as comparisons in the sorting algorithm.

        -   Space Factor. Space is measured by counting the maximum memory space required by the algorithm.

    **  Asymptotic Analysis

        Asymptotic analysis of an algorithm refers to defining the mathematical foundation/framing of its run-time 
        performance. Using asymptotic analysis, we can very well conclude the best case, average case, and worst case scenario of an algorithm.
        
        -  Best Case Minimum time required for program execution.

        -  Average Case Average time required for program execution.

        -  Worst Case Maximum time required for program execution


        Different types of asymptotic notations are used to represent the complexity of an algorithm
        O  Big Oh Notation

        Ω  Big omega Notation

        θ  Big theta Notation

        o  Little Oh Notation

        ω  Little omega Notation

    **  

        

    

    **  Types of Algorithms
    ----------------------------------------------------------------------
    3.1 - Searching Algorithms

    3.2 - Sorting Algorithms

    3.3 - Approximation Algorithms

    3.4 - Divide and Conquer Algorithms

    3.5 - Greedy Algorithms

    3.6 - Recursion Algorithm

    3.7 - Backtracking Algorithm

    3.8 - Randomized Algorithms

    3.9 - Dynamic Programming

    3.10- Pattern Searching

    3.11- Mathematical Algorithms

    3.12- Geometric Algorithms

    3.13- Bitwise Algorithms

    3.14- Branch and Bound Algorithm

.......
