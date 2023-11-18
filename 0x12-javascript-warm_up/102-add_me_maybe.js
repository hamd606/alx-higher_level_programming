#!/usr/bin/node
// executes a function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
