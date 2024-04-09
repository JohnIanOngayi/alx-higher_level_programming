#!/usr/bin/node

exports.converter = function (base) {
  function worker (num) {
    return num.toString(base);
  }
  return worker;
};
