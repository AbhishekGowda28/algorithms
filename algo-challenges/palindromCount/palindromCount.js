// @ts-check

/**
 * @param {string} str
 */
function palindromCount(str) {
    str = str.toLowerCase();
    let largestPalindrom = 0;
    let counter = 1;
    let endCounter = str.length - 1;
    while (counter < endCounter) {
        let distance = 1;
        let previous = str[counter - distance];
        let next = str[counter + distance];
        let intermediatePalindromCount = 1;
        while (previous === next && previous !== undefined) {
            distance++;
            intermediatePalindromCount += 2;
            previous = str[counter - distance];
            next = str[counter + distance];
        }
        if (intermediatePalindromCount > largestPalindrom && intermediatePalindromCount !== 1) {
            largestPalindrom = intermediatePalindromCount;
        }
        counter++;
    }
    return largestPalindrom;
}

let str = "ababa";
let result = palindromCount(str);
console.log(result);
str = "palindromStringabaValue";
result = palindromCount(str);
console.log(result);
str = "Abhishek Gowda";
result = palindromCount(str);
console.log(result);
