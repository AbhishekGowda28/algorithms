






# arrayChange

You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

**Example**
```
For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
```
---
# arrayConversion

Given an array of 2*k integers (for some integer k), perform the following operation untill the array contains only one element: 
 - On the 1st, 3rd, 5th etc iterations replace each pair of consecutive elements with their sum.
 - On the 2nd, 4th, 6th etc iterations replace each pair of consecutive elements with their procudct. 
 
 After the alogrithm has finished, there will be a single element left in the array. Return that element

 **Example**
```
 For inputArray = [1,2,3,4,5,6,7,8], the output should be arrayConversion(inputArray) = 186;

 1st iteration -> [1,2,3,4,5,6,7,8] => [3,7,11,15]
 2nd iteration -> [3,7,11,15] => [21,165]
 3rd iteration -> [21,165] => 186
```
 ---
# arrayMaxConsecutiveSum

Given array of integers, find the maximal possible sum of some of its k consecutive elements.

**Example**
```
For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be arrayMaxConsecutiveSum(inputArray, k) = 8.

All possible sums of 2 consecutive elements are:
2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
```
---
# arrayMaximalAdjacentDifference

Given an array of integers, find the maximal absolute difference between any two of ts adjacent elements.

**Example**
```
 For inputArray = [2, 4, 1, 0], the output should be
 arrayMaximalAdjacentDifference(inputArray) = 3.
```
---
# arrayReplace

Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

**Example**
```
For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
```
---
# avoidObstacles

You are given an array of integers representing coordinates of obstacles situated on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.
Find the minimal length of the jump enough to avoid all the obstacles.

**Example**
```
For inputArray = [5, 3, 6, 7, 9], the output should be avoidObstacles(inputArray) = 4.

Check out the image for better understanding:
```
![Image](https://codefightsuserpics.s3.amazonaws.com/tasks/avoidObstacles/img/example.png?_tm=1490625560816 "Avoid Obstacles")
---
# bishopAndPawn

Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


**Example**
```
For bishop = "a1" and pawn = "c3", the output should be bishopAndPawn(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be bishopAndPawn(bishop, pawn) = false.
```
---
# boxBlur

Last night you had to study, but decided to party instead. Now there is a black and white photo of you that is about to go viral. You cannot let this ruin your reputation, so you want to apply box blur algorithm to the photo to hide its content.
The algorithm works as follows: each pixel x in the resulting image has a value equal to the average value of the input image pixels' values from the 3 × 3 square with the center at x. All pixels at the edges are cropped.
As pixel's value is an integer, all fractions should be rounded down.

**Example**
```
For image = [[1, 1, 1], 
            [1, 7, 1], 
            [1, 1, 1]]
the output should be boxBlur(image) = [[1]].
In the given example all boundary pixels were cropped, and the value of the pixel in the middle was obtained as 
(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9 = 15 / 9 = rounded down = 1.
```
---
# buildPalindrome

Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

**Example**
```
For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
```
---
# candies

n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

**Example**
```
-   For n = 3 and m = 10, the output should be candies(n, m) = 9.

    Each child will eat 3 pieces. So the answer is 9.
 
    The total number of pieces of candy the children will eat provided they eat as much as they can and all 
    children eat the same amount.
```
---
# centuryFromYear

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

**Example**
```
- For year = 1905, the output should be centuryFromYear(year) = 20;
- For year = 1700, the output should be centuryFromYear(year) = 17.
```
---
# checkPalindrome

Given the string, check if it is a palindrome.

**Example**
```
- For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
- For inputString = "abac", the output should be checkPalindrome(inputString) = false;
- For inputString = "a", the output should be checkPalindrome(inputString) = true.
```
---

# chessBoardCellColor

Given two cells on the standard chess board, determine whether they have the same color or not.

**Example**
```
For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.
```
---
# chessKnight

Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. 
The complete move therefore looks like the letter L. 
Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

**Example**
```
- For cell = "a1", the output should be chessKnight(cell) = 2.
- For cell = "c2", the output should be chessKnight(cell) = 6.
```
---
# chunkyMonkey

Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.

**Example**
```
-   chunkyMonkey(["a", "b", "c", "d"], 2) the output should be [["a", "b"], ["c", "d"]].
-   chunkyMonkey([0, 1, 2, 3, 4, 5], 4) the output should be [[0, 1, 2, 3], [4, 5]].
```
---
# circleOfNumbers

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighbouring numbers is equal 

(note that 0 and n - 1 are neighbouring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

**Example**
```
For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
```
---


# domainType

A domain registrar makes a lot of different top-level domains available to its customers. A top-level domain is one that goes directly after the last dot ('.') in the domain name, for example .com in example.com. To help the users choose from available domains, domain registrar is introducing a new feature that shows the type of the chosen top-level domain. You have to implement this feature.
To begin with, you want to write a function that labels the domains as "commercial", "organization", "network" or "information" for .com, .org, .net or .info respectively.
For the given list of domains return the list of their labels.

**Example**
```
- For domains = ["example.org", "example.com", "example.net", "example.info", "example.gov"], 
domainType(domains) = ["organization", "commercial", "network", "information", "government"].
```
---
# depositeProfit

You have deposited a specific amount into your bank account. Each year your balance increases at the same growth rate. Find out how long it would take for your balance to pass a specific threshold with the assumption that you don't make any additional deposits.

**Example**

For deposit = 100, rate = 20 and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.

Each year the amount of money on your account increases by 20%. It means that throughout the years your balance would be:

- **year 0: 100;**
- **year 1: 120;**
- **year 2: 144;**
- **year 3: 172,8.**

Thus, it will take 3 years for your balance to pass the threshold, which is the answer.

---
# Different Characters in a String

Given a string, find the number of different characters in it.

**Example**

For s = "cabbage", the output should be differentCharacters(s) = 5.

---
# Angle between minute and hour hands of Analog clock

Give a time in 24 Hours format. Find the angle between minute and hour hands of the clock.

**Example**

For  time="01:12", the output should be convertTime(time) = 36.

---
# EncloseInBrackets

Given a string, enclose it in round brackets.

**Example**

For inputString = "abacaba", the output should be encloseInBrackets(inputString) = "(abacaba)".

---
# EvenDigitsOnly

Check if all digits of the given integer are even.

**Example**

- For input = 123, the output should be evenDigitsOnly(input) = false
- For input = 246, the output should be evenDigitsOnly(input) = true

---
# DigitsProduct

Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product.
If there is no such integer, return -1 instead.

**Example**

- For product = 12, the output should be digitsProduct(product) = 26
- For product = 19, the output should be digitsProduct(product) = -1

---
# Extract nth Element

Given array of integers, remove each kth element from it.

**Example**

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and n = 3, 

the output should be extractNth(inputArray, n) = [1, 2, 4, 5, 7, 8, 10].

---
# Extract Elements from Matrix

Given a rectangular matrix and an integer column, return an array containing the elements of the columnth column of the given matrix (0th index elements).

**Example**

For matrix = [[1, 1, 1, 2], [0, 5, 0, 4], [2, 1, 3, 6]] and column = 2, 

the output should be extractMatrixColumn(matrix, column) = [1, 0, 3].

---
# File Naming

You are given an array of desired filenames in the order of their creation. 
Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), 
where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

**Example**

For names = ["doc", "doc", "image", "doc(1)", "doc"], 

the output should be fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

---
# Uber Ride

Being a new Uber user, you have ₹20 off your first ride. You want to make the most out of it and drive in the fanciest car you can afford, without spending any out-of-pocket money. There are 5 options, from the least to the most expensive: "UberX", "UberXL", "UberPlus", "UberBlack" and "UberSUV".

You know the length *l* of your ride in kilometers and how much one kilometer costs for each car. Find the best car you can afford.

**Example**

For *l* = 30 and fares = [0.3, 0.5, 0.7, 1, 1.3], 

the output should be fancyRide(l, fares) = "UberXL".

---
# Uber Fair Estimation

Uber is building a Fare Estimator that can tell you how much your ride will cost before you request it. It works by passing approximated ride distance and ride time through this formula:

(Cost per minute) * (ride time) + (Cost per kilo meters) * (ride distance)

where Cost per minute and Cost per kilo meters depend on the car type.

You are one of the engineers building the Fare Estimator, so knowing cost per minute and cost per kilo meters for each car type, as well as ride distance and ride time, return the fare estimates for all car types. 

**Example**

For ride_time = 30, ride_distance = 7, cost_per_minute = [0.2, 0.35, 0.4, 0.45] and cost_per_km = [1.1, 1.8, 2.3, 3.5], 

the output should be fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_km) = [13.7, 23.1, 28.1, 38].

---
# Fermat's factorization method

Wiki Link [Fermat's factorization method](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)

**Example**

For n = 15, the output should be FermatFactorization(n) = [4, 1] => 15 = 4^2 - 1^2.

---
# Closed Sum Pair

Given an array of integers numbers, we'd like to find the closest pair of elements that add up to sum. Return the distance between the closest pair (absolute difference between the two indices). If there isn't a pair that adds up to sum, return -1.

**Example**
- For numbers = [1, 0, 2, 4, 3, 0] and sum = 5 the output should be findClosestPair(numbers, sum) = 2.

- For numbers = [2, 3, 7] and sum = 8 the output should be findClosestPair(numbers, sum) = -1. 

---
# Domain Name of a given Email

An email address such as "John.Smith@example.com" is made up of a local part "John.Smith", an "@" symbol, then a domain part "example.com".

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters.

Given a valid email address, find its domain part.

**Example**

- For address = "prettyandsimple@example.com", the output should be findEmailDomain(address) = "example.com";

- For address = "<>[]:,;@"!#$%&*+-/=?^_{}| ~.a"@example.org", the output should be findEmailDomain(address) = "example.org".

---
# firstDigit

Find the leftmost digit that occurs in a given string.

**Example**

- For inputString = "var_1__Int", the output should be firstDigit(inputString) = '1';

- For inputString = "q2q-q", the output should be firstDigit(inputString) = '2';

- For inputString = "0ss", the output should be firstDigit(inputString) = '0'.

---
# Closest Duplicate

Given an array that contains, find the closest duplicate for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicate, return for which the second occurrence has a smaller index than the second occurrence. If there are no such elements, return `undefined`.

**Example**


- For inputArray = [2, 1, 3, 5, 3, 2], the output should be closestDuplicate(inputArray) = 3.

- For inputArray = [2, 4, 3, 5, 1], the output should be closestDuplicate(inputArray) = undefined.

---
# firstNotRepeatingCharacter

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

**Example**

- For s = "abacabad", the output should be firstNotRepeatingCharacter(s) = 'c'.

- For s = "abacabaabacaba", the output should be firstNotRepeatingCharacter(s) = '_'.

---
# Flatten Array

Flatten a nested array. You must account for varying levels of nesting.

This problem can also be solved using Array Method [Array.flat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat).

**Example**
- flattenArray([[["a"]], [["b"]]]) should return ["a", "b"]
- flattenArray([1, [2], [3, [[4]]]]) should return [1, 2, 3, 4]

---
# Growing Plant

Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.

**Example**

For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be growingPlant(upSpeed, downSpeed, desiredHeight) = 10.

---
# Sum of Houses

A boy is walking a long way from school to his home. To make the walk more fun he decides to add up all the numbers of the houses that he passes by during his walk. Unfortunately, not all of the houses have numbers written on them, and on top of that the boy is regularly taking turns to change streets, so the numbers don't appear to him in any particular order.

At some point during the walk the boy encounters a house with number 0 written on it, which surprises him so much that he stops adding numbers to his total right after seeing that house.

For the given sequence of houses determine the sum that the boy will get. It is guaranteed that there will always be at least one 0 house on the path.

**Example**

For inputArray = [5, 1, 2, 3, 0, 1, 5, 0, 2], the output should be houseNumbersSum(inputArray) = 11.

---
# Root Sum

For a given number reduce the given number to single digit by adding each numbers

**Example**

For inputNumber = 28081994, the output should be rootNumberOfString(inputNumber) = 5.

---
# Valid Time

Check if the given string is a correct time representation of the 24-hour  clock.

**Example**

- time = "13:58", the output should be validTime(time) = true;

- time = "25:51", the output should be validTime(time) = false;

- time = "02:76", the output should be validTime(time) = false.

---
# Root Product

For a given number reduce the given number to single digit by adding each numbers

**Example**

For inputNumber = 222, the output should be rootProduct(inputNumber) = 5.

---
# Validate Variable

Correct variable names consist only of Latin letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

**Example**

- For name = "var_1__Int", the output should be validateVariable(name) = true;

- For name = "qq-q", the output should be validateVariable(name) = false;

- For name = "2w2", the output should be validateVariable(name) = false.

---
# Longest Word

Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

**Example**

For text = "Ready, steady, go!", the output should be longestWord(text) = "steady"

---
# Reverse Parentheses

You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.

**Example**

#For string s = "a(bc)de", the output should be reverseParentheses(s) = "acbde".

---
# isIPv4Address

An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network  that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. 
One of them is the IPv4 address.

**Example**

- For inputString = "172.16.254.1", the output should be isIPv4Address(inputString) = true;

- For inputString = "172.316.254.1", the output should be isIPv4Address(inputString) = false.
316 is not in range [0, 255].

- For inputString = ".254.255.0", the output should be isIPv4Address(inputString) = false.
There is no first number.

---
# Lucky Lottery Ticket

Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

**Example**

- For n = 1230, the output should be luckyTicket(n) = true.

- For n = 239017, the output should be luckyTicket(n) = false.

---
# isMAC48Address

A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), 
separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

**Example**

- For inputString = "00-1B-63-84-45-E6", the output should be isMAC48Address(inputString) = true

- For inputString = "Z1-1B-63-84-45-E6", the output should be isMAC48Address(inputString) = false

- For inputString = "not a MAC-48 address", the output should be isMAC48Address(inputString) = false.

---
# knapsackWeight

You found two items in a treasure chest! The first item weighs weight1 and is worth value1,  and the second item weighs weight2 and is worth value2. 
What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

**Example**

- For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the output should be knapsackWeight(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

- For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the output should be knapsackWeight(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

---
# Line Encoding

Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.

**Example**

For line = "aabbbc", the output should be lineEncoding(line) = "2a3bc".

---
# Increment Backups

One of the easiest ways to back up files is with an incremental backup. This method only backs up files that have changed since the last backup.

You are given a list of changes that were made to the files in your database, where for each valid i, fileChanges[i][0] is the timestamp of the time the change was made, and fileChanges[i][1] is the file id.

Knowing the timestamp of the last backup lastBackupTime, your task is to find the files which should be included in the next backup. Return the ids of the files that should be backed up as an array sorted in ascending order.

**Example**

For lastBackupTime = 461620205 and fileChanges = [[461620203, 1], [461620204, 2], [461620205, 6], [461620206, 5], [461620207, 3], [461620207, 5], [461620208, 1]] the output should be incrementalBackups(lastBackupTime, fileChanges) = [1, 3, 5].

---
# Larget Number

Largest Number of the given digit

**Example**

For n = 2, the output should be largestNumber(n) = 99.

---
# Larget of the Given Array

Return an array consisting of the largest number from each provided sub-array.

**Example**

- For largestOfElements([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]) returns [5, 27, 39, 1001];

- For largestOfElements([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) returns [9, 35, 97, 1000000];

---
# Late Ride

One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.

When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.

Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

**Example**

- For n = 240, the output should be lateRide(n) = 4.

Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

- For n = 808, the output should be lateRide(n) = 14.

808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.

---
# Longest Digit Prefix

Given a string, output its longest prefix which contains only digits.

**Example**

- For inputString="123aa1", the output should be longestDigitsPrefix(inputString) = "123".

---
# Maximum Multiple

Given a divisor and a bound, find the largest integer N such that:

- N is divisible by divisor.
- N is less than or equal to bound.
- N is greater than 0.

It is guaranteed that such a number exists.

**Example**

For divisor = 3 and bound = 10, the output should be maxMultiple(divisor, bound) = 9.
The largest integer divisible by 3 and not larger than 10 is 9.

---
# messageFromBinaryCode

You are taking part in an Escape Room challenge designed specifically for programmers. 
In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. 
After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

**Example**

#For code = "010010000110010101101100011011000110111100100001", the output should be messageFromBinaryCode(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 
72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.

---
# minimalNumberOfCoins

You find yourself in Bananaland trying to buy a banana. You are super rich so you have an unlimited supply of banana-coins, but you are trying to use as few coins as possible.

The coin values available in Bananaland are stored in a sorted array coins. coins[0] = 1, and for each i (0 < i < coins.length) coins[i] is divisible by coins[i - 1]. Find the minimal number of banana-coins you'll have to spend to buy a banana given the banana's price.

**Example**

For coins = [1, 2, 10] and price = 28, the output should be minimalNumberOfCoins(coins, price) = 6.
You have to use 10 twice, and 2 four times.

---
# mostFrequentDigitSum

A step(x) operation works like this: it changes a number x into x - s(x), where s(x) is the sum of x's digits. You like applying functions to numbers, so given the number n, you decide to build a decreasing sequence of numbers: n, step(n), step(step(n)), etc., with 0 as the last element.

Building a single sequence isn't enough for you, so you replace all elements of the sequence with the sums of their digits (s(x)). Now you're curious as to which number appears in the new sequence most often. If there are several answers, return the maximal one.

**Example**

- For n = 88, the output should be mostFrequentDigitSum(n) = 9. Here is the first sequence you built: 88, 72, 63, 54, 45, 36, 27, 18, 9, 0. And here is s(x) for each of its elements: 16, 9, 9, 9, 9, 9, 9, 9, 9, 0.  As you can see, the most frequent number in the second sequence is 9.

- For n = 8, the output should be mostFrequentDigitSum(n) = 8. At first you built the following sequence: 8, 0. s(x) for each of its elements is: 8, 0. As you can see, the answer is 8 (it appears as often as 0, but is greater than it).

---
# Pig Latin

Translate the provided string to pig latin.

Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end of the word and suffixes an "ay".

If a word begins with a vowel you just add "way" to the end.

**Example**

- pigLatin("glove") should return "oveglay".
- pigLatin("eight") should return "eightway".

---
# proCategorization

Thumbtack helps Professionals (Pros) grow their business by identifying new customers. Upon registering on Thumbtack, a Pro specifies which categories of services they provide. To help match customer requests with qualified Pros, Thumbtack maintains a list of Pros grouped by service categories.

Given a list of pros and their category preferences, return the list of Pros for each category.

**Example**

For pros = ["Jack", "Leon", "Maria"] and

preferences = [["Computer repair", "Handyman", "House cleaning"], ["Computer lessons", "Computer repair", "Data recovery service"], ["Computer lessons", "House cleaning"]]

Output -> proCategorization(pros, preferences) = 
[
    [
        ["Computer lessons"], ["Leon", "Maria"]
    ], 
    [
        ["Computer repair"], ["Jack", "Leon"]
    ], 
    [
        ["Data recovery service"], ["Leon"]
    ], 
    [
        ["Handyman"], ["Jack"]
    ], 
    [
        ["House cleaning"], ["Jack", "Maria"]
    ]
]

---
# Capatilize word

Proper nouns always begin with a capital letter, followed by small letters.

Correct a given proper noun so that it fits this statement.

**Example**

- For noun = "pARiS", the output should be capatilize(noun) = "Paris";

- For noun = "John", the output should be capatilize(noun) = "John".

---
# ratingThreshold

In Thumbtack, users are able to rate Pros based on their experience working with them. Each rating is an integer ranging from 1 to 5, and all ratings are averaged to produce a single number rating for any given Pro. Those Pros who have a rating lower than a specified threshold are manually reviewed by Thumbtack staff to ensure high quality of service.

You're given a list of ratings for some Pros. Find out which Pros should be manually reviewed.

**Example**

- For threshold = 3.5 and ratings = [[3, 4], [3, 3, 3, 4], [4]] the output should be ratingThreshold(threshold, ratings) = [1].

`Assume that we have 3 Pros that have received the following ratings: [3, 4], [3, 3, 3, 4] and [4]. Then And if threshold = 3.5 the answer is ratingThreshold(threshold, ratings) = [1]. The first Pro's rating is 3.5, the second one's is 3.25, and the last one's is 4, so only the second Pro should be reviewed manually (the output is their 0-based index).`

---
# spiralNumbers

Construct a square matrix with a size N x N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

**Example**

- For n = 3, the output should be spiralNumbers(n) = 
                                                    [
                                                        [1, 2, 3],
                                                        [8, 9, 4],
                                                        [7, 6, 5]
                                                    ]

---
# Strong Password Checker
 
Password should be more than 8 characters long, should have atleast a number, Captial letter, small letter and special characters.

---
# Refelection String

Define an alphabet reflection as follows: a turns into z, b turns into y, c turns into x, ..., n turns into m, m turns into n, ..., z turns into a.

Define a string reflection as the result of applying the alphabet reflection to each of its characters.

Reflect the given string.

**Example**

For inputString = "name", the output should be reflectionString(inputString) = "mznv".

---
# Seek And Destroy

You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.

**Example**

- seekAndDestroy([3, 5, 1, 2, 2], [2, 3, 5]) should return [1]

- seekAndDestroy([1, 2, 3, 5, 1, 2, 3], [2, 3]) should return [1, 5, 1]

---
# Stolen Lunch

When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a note with a strange, coded message. Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit 0 is replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.

The note is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.

**Example**

For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be stolenLunch(note) = "you'll never guess it: 2390".

---
# Sum of all Primes

Sum all the prime numbers up to and including the provided number.

A prime number is defined as a number greater than one and having only two divisors, one and itself. For example, 2 is a prime number because it's only divisible by one and two.

The provided number may not be a prime.

**Example**

- sumAllPrimes(10) should return 17

- sumAllPrimes(977) should return 73156

---
# Sum of odd Fibonacci numbers

Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.

The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.

**Example**

- sumOddFibonacciNums(10) should return 10

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are 1, 1, 3, and 5.

---
# Sort array elements based on the provided feild.

An array of object is provided. Sort the given array in ascending order, based on the provided field.

**Example**

- arr = [{name: "A",gender: "F",age: 1},{name: "B",gender: "M",age: 2},{name: "C",gender: "M",age: 3}] field = "age" sortByField(arr, field) = [{name: "A",gender: "F",age: 1},{name: "B",gender: "M",age: 2},{name: "C",gender: "M",age: 3}];

---
# Unique Digit Products

Let's call product(x) the product of x's digits. Given an array of integers a, calculate product(x) for each x in a, and return the number of distinct results you get.

**Example**

- For a = [2, 8, 121, 42, 222, 23], the output should be uniqueDigitProducts(a) = 3.

---
# Tasks Type

You have some tasks in your Asana account. For each ith of them you know its deadlinesi, which is the last day by which it should be completed. As you can see in your calendar, today's date is day. Asana labels each task in accordance with its due date:

- If the task is due today or it's already overdue, it is labeled as Today;
- If the task is due within a week but not today - that is, its deadline is somewhere between day + 1 and day + 7 both inclusive - it is labeled as Upcoming;
- All other tasks are labeled as Later;

Given an array of deadlines and today's date day, your goal is to find the number of tasks with each label type and return it as an array with the format [Today, Upcoming, Later], where Today, Upcoming and Later are the number of tasks that correspond to that label.

**Example**

- For deadlines = [1, 2, 3, 4, 5] and day = 2, the output should be tasksTypes(deadlines, day) = [2, 3, 0].

![Image](https://codefightsuserpics.s3.amazonaws.com/tasks/tasksTypes/img/example2.png?_tm=1491409778572)

- For deadlines = [1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8] and day = 1, the output should be tasksTypes(deadlines, day) = [2, 8, 2].

![Image](https://codefightsuserpics.s3.amazonaws.com/tasks/tasksTypes/img/example1.png?_tm=1491409778393)

---
# shapeArea

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

![Image](https://codefightsuserpics.s3.amazonaws.com/tasks/shapeArea/img/area.png?_tm=1491302317375)

**Example**

- For n = 2, the output should be shapeArea(n) = 5;

- For n = 3, the output should be shapeArea(n) = 13.

---
# Sort By Height

Some people are standing in a row in a park.  There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

**Example**

For arr = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(arr) = [-1, 150, 160, 170, -1, -1, 180, 190].

---
# Minesweeper

In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. 
Starting off with some arrangement of mines we want to create a Minesweeper game setup.

**Example**

matrix = [[true, false, false],[false, true, false],[false, false, false]]

minesweeper(matrix) = [[1, 2, 1],[2, 1, 1],[1, 1, 1]]

---
# Find Pair

Given an unsorted array of integers, find a pair with a given sum in it.

**Example**

- For arr = [8, 7, 2, 5, 3, 1] sum = 10 findPair(arr, sum) = [ [ 8, 2 ], [ 7, 3 ] ]

- For arr = [8, 7, 2, 5, 3, 1] sum = 100 findPair(arr, sum) = [ ]

---
# String Peeler

Remove first and last character of the string.
If string cannot be peeled return the string.

**Example**

- peeler("abcvf") = "bcv"

- peeler("ab") = "ab"

---
# Vowel

 Number of vowels in a string

 **Example**

For str = "Hello World. This is first output C Programming book", vowelsCount(str) = 12

---
# CheckBook Balance

You are given a small checkbook to balance that is given to you as a string. Sometimes, this checkbook will be cluttered by non-alphanumeric characters.

The first line shows the original balance. Each other (not blank) line gives information: check number, category, and check amount.

You need to clean the lines first, keeping only letters, digits, dots, and spaces. Next, return the report as a string. On each line of the report, you have to add the new balance. In the last two lines, return the total expenses and average expense. Round your results to two decimal places. 

**Example**

1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10

Solution

Original_Balance: 1000.00
125 Market 125.45 Balance 874.55
126 Hardware 34.95 Balance 839.60
127 Video 7.45 Balance 832.15
128 Book 14.32 Balance 817.83
129 Gasoline 16.10 Balance 801.73
Total expense 198.27
Average expense 39.65

---
