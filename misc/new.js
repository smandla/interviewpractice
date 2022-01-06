const newP = function (str) {
  var patterns = str.match(/(\d+?)(\[)(.*?)(\])/g);
  console.log("patterns", patterns);
  for (let i = 0; i < patterns.length; i++) {
    pattern = patterns[i];
    let start = pattern.indexOf("[");
    let end = pattern.indexOf("]");
    let value = pattern.substr(start + 1, end - start - 1);
    let digit = pattern.substr(0, start);
    let newInsert = value.repeat(digit);
    str = str.replace(patterns[i], newInsert);
  }
  return str;
};

var str = "Abc9[Fdd]ijk3[m]";

console.log(newP(str));
