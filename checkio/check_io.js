/*
Input: A list of integers.

Output: An iterable of integers.

Precondition: 0 < len(data) < 1000
 */
function nonUniqueElements(data) {
    var filterData = [];
    for (var i=0; i<data.length; i++) {
        for (var j=data.length-1; j>=0; j--) {
            if (i !== j && data[i] === data[j]) {
                filterData.push(data[i]);
                break;
            }
        }
    }

    return filterData;
}
/*
*****************
* index methods *
*****************
 function filterNonUnique(data) {
    return data.filter(function(a){
        return data.indexOf(a) !== data.lastIndexOf(a)    
    });
}
*/


/*
Input: An array as a list of integers.

Output: The median as a float or an integer.

Precondition:
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data) 
*/

function median(data) {
    const len = data.length;
    const halfN = n => Math.floor(n / 2);
    const sortedData = data.sort((a,b) => a- b);
    if (len % 2 > 0) {
        return sortedData[halfN(len)];
    } else {
        return (sortedData[halfN(len-1)] + sortedData[halfN(len)]) / 2;
    }
}

/* 
****************
* floor + ceil *
****************
function median(data) {
    let sorted = data.slice().sort((a,b) => a - b);
    let middle = (data.length - 1) / 2;
    return (sorted[Math.floor(middle)] + sorted[Math.ceil(middle)])/2;
}

************
* manually *
************
function median(data) {
    let len = data.length;
    let sorted = data.slice().sort((a,b) => a - b);
    let mid = Math.floor(len / 2);
    return (sorted[mid] + sorted[(len - 1 - mid)]) / 2;
}
*/
