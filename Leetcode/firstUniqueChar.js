const firstUniqueChar = function (str) {
  var counter = {};

  for (let i = 0; i < str.length; i++) {
    if (counter.hasOwnProperty(str[i])) {
      //console.log(str[i]);
      counter[str[i]] += 1;
    } else {
      counter[str[i]] = 1;
    }
  }
  j = 0;
  while (j < str.length) {
    if (counter[str[j]] == 1) {
      return str[j];
    }
    j += 1;
  }
  return -1;
};

str = "cbcbdde";
console.log(firstUniqueChar(str));
