function solution(s) {
    let answer = '';
    let midNum = Math.round(s.length / 2)
    if (s.length % 2 === 0) {
        answer = s[midNum -1].concat(s[midNum]);
    }
    if (s.length % 2 === 1) {
        answer = s[midNum - 1];
    }
    return answer;
}
