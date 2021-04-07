function solution(x) {
    let answer = true;
    const temp = Array.from(String(x), Number);
    let sum = 0;
    temp.forEach((i) => {
        sum += i;
    })
    answer = x % sum === 0;
    return answer;
}
