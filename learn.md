# Learning journal 📖

## How computers work

### Components

* Computer circuits are composed of many little transistors 
* Each transistor is composed of a semiconductor, 2 electrodes and a control wire
    * **Primary function**: takes in an input of 0 or 1, and they return a 0 or 1.
    * This allows the creation of logic gates
* Logic gates allow us to implement basic control flow (NOT, AND, OR, XOR), represented via truth tables

Generally, when looking at making a computer from scratch, we look at two things, the ALU *(arithmetic logic unit)* and the CU *(control unit)*.

* **ALU**: performs all the basic arithmetic operations, and logical operations 
* **CU**: creates communication between memory unit and ALU, in charge of managing computer memory

### Arithmetic (ALU)

* Truth table allows us to perform basic arithmetic using logic gates
* Output of truth table reflects the inputs and outputs when performing [calculating in binary](https://youtu.be/rsxT4FfRBaM?si=0NCoo2WrkjigxNYB)

#### Truth tables

##### AND truth table

| A | B | Y |
| :--: | :--: | :--: |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

##### OR truth table

| A | B | Y |
| :--: | :--: | :--: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

##### XOR truth table

| A | B | Y |
| :--: | :--: | :--: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

##### NOT truth table

| A | B |
| :--: | :--: |
| 0 | 1 | 
| 1 | 1 |

### Memory (CU)

Visualised through the...

* [S-R latch](https://youtu.be/-aQH0ybMd3U?si=IFrBk0u7Qb1rS4Bb)
    * Set keys
    * Reset keys
    * Output

and managing the relationship between these inputs and the output.

## How language interpreters / compilers work

* **Compilers** read source code and convert it to binary (machine code)
    * Source code read through Lexical analysis, parsing, ***compiling***
* **Interpreters** read source code and convert it to another language's source code 
    * Source code similarly read through Lexical analysis, parsing, ***interpreting***
    * Interpreter will affect memory changes where initiated in source code
    * Interpreter will also render output

### Looking inside an interpreters 

#### Lexical analysis 

* **Input**: Input source code
* **Output**: Tokens
* Performs Tokenisation
* Breaks down input into tokens, stores tokens in a sequential data structure
* Assigns data type and other characterstics as values to the token
* Blindly converts the input source code into a bunch of tokens
* Does NOT check whether the tokens abide by any of the rules of the programming language

#### Parsing

* **Input**: Tokens
* **Output**: Abstract Syntax Tree (AST)
* Recognises patterns and structure in the tokens by applying grammer rules
* CHECKS whether the tokens abide by any of the rules of the programming language by comparing it against the recognised list of structures laid out in programming language's syntax
* Frameworks to define a programming langauge's grammer rules:
    * [**BNF**](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
        * Utilises recursion to break down every expression to its basic building blocks

#### Interpreting

* **Input**: Abstract Syntax Tree (AST) 
* **Output**: Output source code
* Takes in an AST (in the structure of a binary tree) and executes it statement by statement (node by node, traversing down each node if there are branches)

