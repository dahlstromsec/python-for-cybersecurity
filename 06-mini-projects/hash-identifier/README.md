# Hash Identifier

A simple Python tool that identifies common hash algorithms based on their format and length.

This project was built as part of my **Python for Cybersecurity** repository to reinforce Python programming concepts while learning about cryptographic hash functions commonly encountered in cybersecurity.

---

## Features

* Identify common hash algorithms
* Validate hexadecimal hash formats
* Detect multiple possible hash types
* Interactive command-line interface
* Continuous input until the user exits

---

## Currently Supported Hashes

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512
* NTLM
* LM
* bcrypt

---

## Example

```text
==================================================
 Hash Identifier v1.0
==================================================

Type 'exit' to quit.

Enter hash:
5f4dcc3b5aa765d61d8327deb882cf99

Possible hash types:
 - MD5
 - NTLM
 - LM

Note:
Some algorithms share the same output length.
Additional context is required for a definitive identification.
```

---

## Learning Objectives

This project reinforces several Python concepts, including:

* Functions
* Conditional statements
* Lists
* Regular expressions
* User input
* Loops
* Input validation
* Program structure

It also introduces an important cybersecurity concept: **hashes cannot always be uniquely identified based solely on their length.**

---

## Future Improvements

Possible enhancements include:

* Support for additional hash algorithms
* Colorized terminal output
* Command-line arguments
* File input for bulk hash identification
* Hash identification confidence levels
* Improved format detection
* Unit tests

---

## License

This project is licensed under the MIT License.
