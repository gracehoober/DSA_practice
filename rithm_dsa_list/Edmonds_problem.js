/** Write a function that takes a number and prints out each digit of the number
 * in reverse order.
 * You cannot change the data type of the string.
 *
 *
 *  I: number
 *  O: nothing returned from function
 * test cases:
 *  10 ---> console: 0
 *                   1
 *
 *  103 ---> console: 3
 *                    0
 *                    1
 *
 *  9 ---> console: 9
 * base case: if num % 10 is less than 10 print it
 * progress: take 'next' num and call printInReverse on it
 *
 *
 * ideas:
 *  next = num/10 --> move to next iteration
 *  remainder = num % 10 --> print out remainder
 *
 *
 */

function printInReverse(num) {// 12
  if (num < 10) {
    console.log(num);
  } else {
    const remainder = num % 10; 2
    console.log(remainder);
    const next = Math.floor(num / 10);
    printInReverse(next);

  }
}

/** 9
 * next = 1
 * remainder = 0
 * printed = 2, 0, 1
 */

printInReverse(12345678);
// console.log(printInReverse(10))
// console.log(printInReverse(102))

function reverseNumber(x, power = 1) { //123 //12 //1
  //base case
  if(x < 10) return x; //1
  else{
      const toAdd = x%10//3 //2
      const next = Math.floor(x/10);// 12 //1

      //const power = 1 //power need to increment with each function on the stack

      //calls itself and progress
      return ((10 ** power) * toAdd) + reverse(next, power + 1);
      //((10^1) * 2) + 1 => 21
      //((10^2) * 3) + 21 => 321
  }
};