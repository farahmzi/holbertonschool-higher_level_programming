#!/usr/bin/env node
const { argv } = require('process');

function add (a, b) {
  console.log(`${Number(a) + Number(b)}`);
}

add(argv[2], argv[3]);