function solution(lottos, win_nums) {
    let answer = [];
    let rank = [6, 6, 5, 4, 3, 2, 1];
    let hit = 0;
    let zeroCount = 0;
    let maxCount = 0;

    lottos.forEach((i) => {
        if (i === 0) zeroCount += 1;
        win_nums.forEach((j) => {
            if (i === j) hit += 1;
        })
    })

    maxCount = zeroCount + hit;
    answer = [rank[maxCount], rank[hit]];

    return answer;
}
