# chatbot

Simple "hello" query implementation

This repository provides a minimal Node.js module that handles a query string. If the query is exactly "hello" (case-insensitive), it returns "Hello!".

Usage:

- As a module:
  const { query } = require('./index');
  console.log(query('hello')) // -> "Hello!"

- CLI:
  node index.js hello

The implementation is intentionally small to satisfy the "hello" query requirement.