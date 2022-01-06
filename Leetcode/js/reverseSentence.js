const reverseSentence = function (str) {
  return str
    .split(" ")
    .map(function (item) {
      return item.split("").reverse().join("");
    })
    .join(" ");
};
str = "I evol uoy os !hcum";
console.log(reverseSentence(str));
