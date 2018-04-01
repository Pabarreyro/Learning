# **Cryptosquare Generator**

#### Pablo Barreyro

## Description

Behavior | Input | Ouput
------------ | ------------- | -------------
Convert string to lower case | "Samplestring" | "samplestring"
Remove punctuation & whitespace from a string| "Sample string" | "Samplestring"
Find length | "samplestring" | 12
Find square root of length to determine columns x rows | 12 | rows = 4,<br>columns = 3
Split string by _n_<sub>columns</sub> | "samplestring" | ["sam","ple","str","ing"]
Split strings in array | ["sam","ple","str","ing"] | [["s", "a", "m"],<br>["p", "l", "e"],<br>["s", "t", "r"],<br>["i", "n", "g"]]
Push all elements in nested array to new array | [["s", "a", "m"],<br>...<br>["i", "n", "g"]] | ["s", "a", "m", ... "i", "n", "g"]
Push just first element in nested array to new array | [["s", "a", "m"],<br>...<br>["i", "n", "g"]] | ["s", ... "i"]
Push just the last element in nested array | [["s", "a", "m"],<br>...<br>["i", "n", "g"]] | ["m", ... "g"]
Loop .push() method through nested arrays, targeting each index one at a time from 0 - ( _n_<sub>rows</sub> ) | [["s", "a", "m"],<br>...<br>["i", "n", "g"]] | ["s", "p", "s" ... "e", "r", "g"]
Splice first five elements in array | ["s", "p", "s", "i", "a", "l"...] | ["s", "p", "s", "i", "a"]
Loop splice across array | ["s", "p", "s", "i", "a", "l"...] | ["s", "p", "s", "i", "a"]<br>["l"...]


## Setup/Installation Requirements

* To view project code, _clone repository from_ https://github.com/pabarreyro/projectname
* To view project, _open in web browser_ https://pabarreyro.github.io/projectname

## Technologies Used

* HTML
* CSS _(Bootstrap)_
* JavaScript _(jQuery)_

## License

* GPL

Copyright (c) 2018 **_Pablo Barreyro_**
