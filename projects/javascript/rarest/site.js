var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

console.log(namesToAges['Alyssa']);

var ageArray = [];

for (var key in namesToAges) {
    ageArray.push(namesToAges[key])
};

var ageFreqObj = {};


for (var i in ageArray) {
    if (ageArray[i] in ageFreqObj) {
        ageFreqObj[ageArray[i]] = ageFreqObj[ageArray[i]] + 1;
    } else {
        ageFreqObj[ageArray[i]] = 1;
    }
}

var rarest = ageArray[0];
var rarestkey = '';

for (var key in ageFreqObj) {
    if (ageFreqObj[key] < rarest) {
        rarest = ageFreqObj[key];
        // rarestkey = key;
    }
}

console.log(ageArray);

console.log(ageFreqObj);

console.log(rarest);

console.log(rarestkey);

/*
function findRarestValue(obj) {
    var dict = flip_dictionary(obj);
    var rarest = Number.POSITIVE_INFINITY;
    var rarestlen = Number.POSITIVE_INFINITY;
    for (var age in dict) {
        if (dict[age].length < rarestlen) {
            rarest = age;
            rarestlen = dict[age].len
        }
    }
    return rarestlen
}