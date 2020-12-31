
function multipleOf(input: number) {
   return input % 5 === 0 || input % 3 === 0;
}

function problem1() {
   let sum = 0;
   for (let counter = 1; counter < 100; counter++) {
      if (multipleOf(counter)) {
         sum += counter;
      }
   }
   return sum;
}

// export { problem1 };
module.exports = {problem1};
