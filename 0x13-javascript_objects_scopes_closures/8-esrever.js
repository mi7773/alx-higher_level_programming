#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;
  const rlist = [];
  for (let i = len; i > -1; i--) {
    rlist.push(list[i]);
  }
  return rlist;
};
