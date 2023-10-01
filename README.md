# `ooe`

## Why the name?

One of my friends once shared it with me, as a warning.

## What is ***ooe***?

A badly constructed markup language, ending with the file extension `.ooe`. Think more [groff](https://www.gnu.org/software/groff/), less [markdown](https://www.markdownguide.org/). 

> Not to shit on groff though...

## How does ***ooe*** work?

> This is dumbed down a lot. @Zooming, please forgive me.

For that, you'll need some context.

Know that in general, implementing a programming language interpreter (such as the Python3 interpreter) requires the three following components.

1. **Lexer**: Reads the input "source code" 
    * In this case, the `.ooe` code is taken in as input, and tokenised indiscriminately, before returning an array of tokens and their data types
2. **Parser**: Looks through the tokenised list, and returns an abstract syntax tree (AST), normally generated based on the hierachy of operations established in the programming language's syntax
    * Think BODMAS rule for mathematical operations, but on a much larger scale
3. **Interpreter**: Iterates through the AST, returns the output "other source code" 
    * In this case, ***ooe*** compiles to another markup language.

However, as outlined in the book [Domain specific languages](https://www.amazon.com/Domain-Specific-Languages-Addison-Wesley-Signature-Fowler/dp/0321712943), most markup languages don't even have a well-defined AST, and occasionally skip implementation of the parser altogether. That is what I will be doing for ***ooe***, and as such, will really only be implementing anything close to resembling a conventional lexer, alongside a frankenstien abodmination of an interpreter cum half-parser. We'll see how it goes :<.

## ***ooe*** syntax

> ***WIP***

| stylisation | syntax |
| :---: | :---: |
| italics | \` ` |
| bolded | * *|
| underlined | _ _ |
| highlighted | & & |
| header | + + |
| header depth max 6 | ++++++ +++++++
| quotes | @ @ |
| table name, column names | % ; ; ; % |
| column values | $ ; ; $
| bulleted list | - ; ; ; - |
| numbered list | ! ; ; ; ! |

---

## Media I referenced

* [Article on implementing pandoc in haskell](https://www.tweag.io/blog/2021-06-15-asciidoc-haskell-pandoc/)
