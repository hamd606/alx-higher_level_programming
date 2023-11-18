#!/usr/bin/node
// script that imports an array and prints a new one

const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map (function (e, index) {
    return (e * index);
});
console.log(mappedList);
