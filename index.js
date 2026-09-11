#!/usr/bin/env node
'use strict';

function query(input) {
  if (typeof input !== 'string') return 'Invalid input';
  const normalized = input.trim().toLowerCase();
  if (normalized === 'hello') return 'Hello!';
  return `I don't understand: ${input}`;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (!arg) {
    console.log('Usage: node index.js <query>');
    process.exit(1);
  }
  console.log(query(arg));
}

module.exports = { query };
