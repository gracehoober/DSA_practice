// Write a function that take a string and returns all distinct permutations of a string.
// For example, the following string input 'POP' should return the set 'PPO' 'OPP' 'POP'
// Make sure to document additional example cases.


//Tests "POP" -> ['PPO', 'OPP', 'POP']

function stringPerms(str) {
  let perms = [];

  arrOfchars = str.split("");

  for (let i = 0; i < arrOfchars.length; i++) {
    let copy = arrOfchars.slice();
    let char = copy.splice(i, 1)[0];

    for (let j = 0; j < copy.length; j++) {
      copy.splice(j, 0, char);

      newString = copy.join("");

      if (!perms.includes(newString)) {
        perms.push(newString);
      }
    }
  }
  return perms;
}

console.log(stringPerms("SAP"))

/**
 * I: str
 * O: array of strings
 * considerations: what do do with strings that have spaces?
 * logic:
 * turn the string into an array
 * loop through the array and remove the value at the index
 * loop through the mutated array and add the value at each index
 * mutate array back to string
 * check if string is in perms -> no: add it to perms
 *
 *
 * str = "POP"
 * 0
 * perms = ["POP"]
 * arrOfChars = [ 'P', 'O', 'P' ]
 * copy = [ 'P', 'O', 'P' ]
 * arrOfChars length = 3
 * char = "P"
 * copy = ['O', 'P'] => ['O', "P", 'P']
 * newString = "OPP"
 *
 * 1
 * perms = ["POP", "OOP"]
 * arrOfChars = [ 'P', 'O', 'P' ]
 * copy = ['O', "P", 'P']
 * arrOfChars length = 3
 * char = "p"
 *
 */