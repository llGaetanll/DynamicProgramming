# Dynamic Programming

_This repo contains all functions from the freeCodeCamp Dynamic Programming course, written in Python._

[![Course](https://i.imgur.com/E4xK2zV.jpg "Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges")](https://www.youtube.com/watch?v=oBt53YbR9Kk)

## About

This repo is split into main sections: `memoization/` and `tabulation/`. Each of the following functions is implemented twice, as is done in the course.

## Functions

In the original course, these functions are written in JavaScript. In this repo, they have been translated to Python. In each file, you'll find more info about the function, as well as its time and space complexity.

### `fib(n)`
Computes the nth Fibonacci number. This is just a simple example to get started with DP.

### `grid_traveler(m, n)`
Given an `m` by `n` grid, this computes the number of ways that this grid can be travelled given that, on any given timestep, you can only travel one step down, or one step to the right. Additionally, you always start in the top left corner of the grid.

### `can_sum(target_sum, numbers)`
Given a number `target_sum` and a list of numbers `numbers`, this function returns whether it is possible to get to `target_sum` by adding elements of `numbers`. These elements are sampled with replacement.

### `how_sum(target_sum, numbers)`
Similar to the previous function, this function takes a number `target_sum`, and a list of of numbers `numbers`. It returns a list of elements of `numbers` that add to `target_sum`. These elements are sampled with replacement

### `best_sum(target_sum, numbers)`
This function improves on the previous function `how_sum` by returning the shortest list adding to `target_sum`. Elements are again sampled with replacement.

### `can_construct(target, word_bank)`
Given a target string `target`, and a list of strings `word_bank`, this function returns whether the string `target` can be constructed from the list of strings in `word_bank`. Elements of `word_bank` are sampled with replacement.

### `count_contruct(target, word_bank)`
This function returns the number of ways that the target string `target` can be constructed from the list of strings `word_bank`. Elements of `word_bank` are sampled with replacement.

### `all_construct(target, word_bank)`
This function returns all the ways that the target string `target` can be contructed from the list of strings `word_bank`. Elements are once again sampled with replacement.
