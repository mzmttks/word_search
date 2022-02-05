# wordfilter
A tool to filter words.


## How to use


If you want to filter words that 
* contain `h` and `e`
* do not contain `a`
* have letter 
    * `l` at the 3rd letter and
    * `l` at the 4th letter (one-based indexing)
* do not have
    * letter `s` at the 5th letter and
    * letter `y` at the 5th letter (one-based indexing)


```
python3 filter.py --contain h e --notcontain a --at 3l 4l --notat 5s 5y
```

Then, you will get the following output.

```
Constraints
    Contain    : ['h', 'e']
    Not contain: ['a']
    At         : [(2, 'l'), (3, 'l')]
    Not at     : [(4, 's'), (4, 'y')]
    
['hello']
The number of found words: 1
```

You can find the words that satisfy all constraints.