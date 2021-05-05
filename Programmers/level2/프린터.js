function solution(priorities, location) {
    let targetIndex = location;
    let answer = 0;

    while (priorities.length> 0) {
        first = priorities.shift();
        if (priorities.some((value, index) => value > first)) {
            priorities.push(first);
        } else {
            answer = answer + 1;
            if (targetIndex === 0) {
                break;
            }
        }

        if (targetIndex === 0) {
            targetIndex = priorities.length - 1;
        } else {
            targetIndex = targetIndex - 1;
        }
    }
    return answer;
}
