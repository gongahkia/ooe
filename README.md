![](https://img.shields.io/badge/OOE_1.0-passing-green)

# `ooe`

## What is ***ooe***?

![ooe_origin](https://github.com/gongahkia/ooe/assets/117062305/436e9d44-b274-4428-8da8-259b7d3a340c)

A badly constructed markup language, ending with the file extension `.ooe`.
  
Think more [groff](https://www.gnu.org/software/groff/), less [markdown](https://www.markdownguide.org/). 

The ***ooe*** interpreter transpiles `ooe` script to `html`.

## How does ***ooe*** work?

> This is dumbed down a lot. Detailed reference material can be found below.

For that, you'll need some context.

Know that in general, implementing a programming language interpreter (such as the Python3 interpreter) requires the three following components.

1. **Lexer**: Reads the input "source code" 
    * In this case, the `.ooe` code is taken in as input, and tokenised indiscriminately, before returning an array of tokens and their data types
2. **Parser**: Looks through the tokenised list, and returns an abstract syntax tree (AST), normally generated based on the hierachy of operations established in the programming language's syntax
    * Think BODMAS rule for mathematical operations, but on a much larger scale
3. **Interpreter**: Iterates through the AST, returns the output "other source code" 
    * In this case, ***ooe*** compiles to HTML, allowing you to render your `.ooe` notes in `.html` via a local web server.

However, as outlined in the book [Domain specific languages](https://www.amazon.com/Domain-Specific-Languages-Addison-Wesley-Signature-Fowler/dp/0321712943), most markup languages don't even have a well-defined AST, and occasionally skip implementation of the parser altogether. That is what I will be doing for ***ooe***, and as such, will really only be implementing anything close to resembling a conventional lexer, alongside a frankenstien abodmination of an interpreter cum half-parser. We'll see how it goes :<.

## Language syntax

| stylisation | syntax | implementation status |
| :---: | :---: | :---: |
| italics | \` ` | ✅ |
| bolded | * * | ✅ |
| underlined | _ _ | ✅ |
| highlighted | & & | ✅ |
| header | + + | ✅ |
| header depth max 6 | ++++++ ++++++ | ✅ |
| quotes | @ @ | ✅ |
| column names, column values | % ; $ ; % | ✅ |
| bulleted list | - ; ; ; - | ✅ |
| numbered list | ! ; ; ; ! | ✅ |

## Usage

To try out `ooe`...

1. Run the following commands in your terminal.

```console
$ git clone https://github.com/gongahkia/ooe
$ cd ooe/src
```

2. Create a `.ooe` file following the language syntax specified above. 

> *Don't worry, the OOE compiler will let you know if there is an issue with your syntax.*

3. Run the `main.py` file.

```console
$ Python3.11 main.py
```

4. OOE will compile the `.ooe` file to `.html` and create the new `.html` file in the same file directory as your `.ooe` source file.

## Notes

* I have no intention of implementing a bash script to run this command in the CLI as of yet. My focus is on completion of [`DC4U`](https://github.com/gongahkia/dc4u) for now.

---

## Media I referenced

* [Crafting interpreters book](https://craftinginterpreters.com)
* [Article on implementing pandoc in haskell](https://www.tweag.io/blog/2021-06-15-asciidoc-haskell-pandoc/)
