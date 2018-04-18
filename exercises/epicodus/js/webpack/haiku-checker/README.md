# Haiku Checker/Creator

#### Creates and checks Haikus, 04/18/18

#### By **Pablo Barreyro & Joe McKinney**

## Description

This application will check whether a poem is in fact a haiku.

### Specs
 Behavior | Input | Output
 -------- | ----- | ------
Verifies that poem has three lines | "Haikus are easy.<br>But sometimes they don't make sense.<br> Refrigerator." | True
Counts vowels for each sentence | "Haikus are easy.<br>But sometimes they don't make sense.<br> Refrigerator." | [7,11,5]
Applies exceptions to each word count | "Haikus are easy.<br>But sometimes they don't make sense.<br> Refrigerator." | [2, 1, 2 ]<br>[1, 3, 1, 1, 1]<br>[5]
Generate haiku from text entry | "Haikus are easy.<br>But sometimes they don't make sense.<br> Refrigerator." | [2, 1, 2 ]<br>[1, 3, 1, 1, 1]<br>[5]


## Setup/Installation Requirements

* Clone repo
* Run npm install command in root directory
* Open in favorite code editor
* View in browser

## Known Bugs

No known bugs on current version.

## Support and contact details

Start thread in repo.

## Technologies Used

* HTML
* CSS (_Bootstrap 4_)
* JavaScript (_jQuery, Node.js_)

### License

Copyright (c) 2015 **_McKinney </> Barreyro_**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
