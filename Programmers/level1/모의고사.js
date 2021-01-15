function solution(answers) {
  var answer = [];
  const num1 = [1, 2, 3, 4, 5];
  const num2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let count = [0, 0, 0];
  answers.forEach((value, index) => {
    if (value === num1[index % 5]) count[0] += 1;
    if (value === num2[index % 8]) count[1] += 1;
    if (value === num3[index % 10]) count[2] += 1;
  });
  const max = Math.max(...count);
  if (max !== 0) {
    count.filter((value, index) => {
      if (value === max) answer.push(index + 1);
      answer.sort();
    });
  } else {
    answer = [1, 2, 3];
  }

  return answer;
}
