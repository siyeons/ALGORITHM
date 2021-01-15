function solution(phone_number) {
  var answer = "";
  const temp = phone_number.split("");
  for (let i = 0; i < temp.length - 4; i++) {
    temp[i] = "*";
  }
  answer = temp.join("");
  return answer;
}
solution("0233334444");

function hide_numbers(s) {
  var result = "*".repeat(s.length - 4) + s.slice(-4);
  return result;
}
