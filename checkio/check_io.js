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
function median(data) {
    let sorted = data.slice().sort((a,b) => a - b);
    let middle = (data.length - 1) / 2;
    return (sorted[Math.floor(middle)] + sorted[Math.ceil(middle)])/2;
}
*/
