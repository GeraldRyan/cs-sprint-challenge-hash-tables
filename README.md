# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions

# Hashing functions are complex mathematical functions that take variable length input and return fixed length collision resistent output (strings or ints), used for many things- security, encryption, pki and to build hash tables. 

2. Collision resolution

# Collision is when two different inputs hash to the same hash. One way to deal with this in hash table is to make each entry a node that is a linked list (or normal list) and then you can find the index by using the typical hash method and then find the actual data sought after by looking through the list and for the unhashed key. 

3. Performance of basic hash table operations

# Hash tables are much more performative than other methods as y0ou don't have to binary search or anything like that. Your data is indexed by the hash of itself so you know right what index to go to, so it is between O(logN) to O(n) but much much closer to the O(logN). The O(n) is just an unrealistic absolute worst case scenario where all strings hash to same value and you have to run through the list of n elements to find the one with the matching key. 

4. Load factor

# load factor tells us how full a hash table is, irrespective of whether the load is based on filled indeces or on elements in a list all on one index. In other words, the number of data entries in a hash table divided by the number of slots or indeces. Therefore it can be over 100%. It can be infinite but generally...... (see #5 below)

5. Automatic resizing

# generally when the load factor hits .7 or whatever you decree, the table can be resized- most generally doubled in size. THat is there's 2x the number of slots. Each element in the old table whether the head of an index slot or part of a chain is rehashed to find a new home on the resized table. Since the index chosen is based on the mod of the number of spaces, each old element is a candidate for receiving a brand new index, so its possible nothing will be where it was before. Things have to spread out. 

6. Various use cases for hash tables

# quick lookup is one- where performance is wished for. Since it's also a dictionary like structure, it gives all the features of that, such as username lookup. 

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

