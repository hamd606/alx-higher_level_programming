#!/usr/bin/node
// converts a number from base 10 to another base (from args)

exports.converter = function (base) {
  return function (n) {
    return (n.toString(base));
  };
};
