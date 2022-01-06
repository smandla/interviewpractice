/**
 *
 * @param {nums}
 *
 * using a hashtable to check if it contains the key more than once
 */
const containsDuplicate = function (nums) {
  var ht = {};
  for (let i = 0; i < nums.length; i++) {
    console.log("nums[i]", nums[i]);
    if (ht.hasOwnProperty(nums[i])) {
      ht[nums[i]] += 1;
      console.log(i);
    } else {
      ht[nums[i]] = 1;
    }
  }

  return ht;
};

var nums = "Abc12[fgh]jklrtr13[rtr]rrr14[afg]rtxyz";
//console.log(containsDuplicate(nums));

/**
 * containsDuplicateRegEx
 *
 *
 */

const containsDuplicateRegEx = function (nums) {
  var ht = {};
  var digits = nums
    .toLowerCase()
    .split("")
    .join("")
    /**
     * [0-9]+ -> matches a character in this range (match 1 or more of the preceding token)
     * (?:) -> non capturing group - groups together without creating a capture group
     */
    .match(/[0-9]+(?:\.[0-9]*)?/g);

  var patterns = nums
    .toLowerCase()
    .split("")
    .join("")
    /**
     * (?<= ) -> positive lookbehind - matches a group before the main expression without including it in result
     * \[ -> matches expression
     * (.*?) -> capturing group (matches any character to 0 or more of preceding token and makes it lazy so it matches as few characters as possible)
     * (?=\]) -> positive lookahead - matches a group after the main expression without including it in result
     */
    .match(/(\d+?)(\[)(.*?)(\])/g);

  /**
   * /
   * (.) -> matches any character except line breaks
   * \1 -> matches the rsult of (.)
   * + -> match 1 or more of the preceding token
   */
  //   if (arr !== null) {
  //     arr.forEach((i) => {
  //       ht[i[0]] = i.length;
  //     });
  //   }
  console.log(digits);
  console.log(patterns);
  for (let i = 0; i < patterns.length; i++) {
    console.log(patterns[i]);
  }
};
console.log(containsDuplicateRegEx(nums));
