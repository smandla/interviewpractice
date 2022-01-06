// /**
//  * input 'ABC'
//  * output 'ABC, 'ACB', 'BCA', 'BAC', 'CAB', 'CBA'
//  *
//  */
// const print = function (str) {
//   generatePermutations("", str);
// };
// const generatePermutations = function (prefix, str) {
//   var len = str.length;
//   for (let i = 0; i < len; i++) {
//     generatePermutations(
//       prefix + str.charAt(i),
//       str.substr(i + 1, len) + str.substr(0, i)
//     );
//   }
//   console;
//   console.log("patterns", prefix + str);
// };

// var str = "Abc";
// console.log(generatePermutations("", str));

const permute_and_print = function (str) {
  permute("", str);
};

const permute = function (prefix, str) {
  var n = str.length;
  if (n == 0) {
    console.log(prefix + "");
  }
  if (n != 0) {
    for (let i = 0; i < n; i++) {
      permute(
        prefix + str.charAt(i),
        str.substring(i + 1, n) + str.substring(0, i)
      );
    }
  }
};
console.log(permute("", "Abc"));
