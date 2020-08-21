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