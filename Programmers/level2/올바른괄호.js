function solution(s) {
  var answer = true;
  let targetStack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") targetStack.push(s[i]);
    else {
      if (s.length <= 0) return (answer = false);
      else {
        if (targetStack[targetStack.length - 1]) targetStack.pop(s[i]);
        else targetStack.push(s[i]);
      }
    }
  }
  if (targetStack.length > 0) answer = false;
  else answer = true;

  return answer;
}
