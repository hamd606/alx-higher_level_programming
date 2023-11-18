#!/usr/bin/node
// prints the number of args already printed and the new arg

let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
