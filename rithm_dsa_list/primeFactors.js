/** Write a function that takes a number and returns an array of factors that
 * are prime. Can I solve recursively?
 *
 * I: number
 * O: array
 * examples: 1 -> [], 2 -> [2], 3 -> [3], 4 -> [2,2], 6 -> [2,3] 12 -> [2,2,3], 15 -> [3,5], 45 -> [3,3,5]
 * logic:
 * create a function that determines if a number is prime: see isPrime
 * create a function that finds the factors of the input number
 *  divide num in half and round down: the max number of times need to loop
 *
 */

function primeFactors(num){
  const primeFactors = [];
  const half = Math.min(num/2);

  let i = 1;
  let j = 0;
  while(i <= half){
    if(num % i === 0){
      if(isPrime(i)){
        primeFactors.push(i)
        
      }
    }
  }
}

function isPrime(num){
  //counts factors excluding 1 and num
  const count = 0
  for(let i = 2; i < num; i++){
    if(num % i === 0) count++;
  }
  return count === 0 ? true : false;
}