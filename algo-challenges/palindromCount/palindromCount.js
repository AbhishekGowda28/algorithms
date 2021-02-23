function palindromCount(str) {
    let largestPalindrom = 0;
    let counter = 1;
    let endCounter = str.length;
    while(counter < endCounter) {
     console.log(str[counter];
     let distance = 1;
     let previous = str[counter - distance];
     let next = str[counter + distance];
     let intermediatePalindromCount = 1;
     while(previous === next){
      distance++;
      intermediatePalindromCount+=2;
      previous = str[counter - distance];
      next = str[counter + distance];
     }
     counter++;
    }
    return str;
}

const str = "ababa";
const result = palindromCount(str);
console.log(result);
