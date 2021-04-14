function solution(num) {
    let answer = 0;
    let tempNum = num;
    let count = 0;

    while (tempNum !== 1) {
        if (tempNum % 2 === 0) tempNum = tempNum / 2;
        else tempNum = (tempNum * 3) + 1;
        count += 1;
    }

    if (count > 500) answer = -1;
    else answer = count;

    return answer;
}
