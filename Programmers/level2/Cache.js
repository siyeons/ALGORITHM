function solution(cacheSize, cities) {
    let answer = 0;
    let cache = [];
    const cityArray = cities.map((d) => d.toUpperCase());

    if (cacheSize === 0) return cities.length * 5;

    cityArray.forEach((city, index) => {
        const idx = cache.indexOf(city);
        if (idx !== -1) {
            cache.splice(idx, 1);
            cache.push(city);
            answer += 1;
        } else {
            if (cache.length !== cacheSize) cache.push(city);
            else {
                cache.shift();
                cache.push(city);
            }
            answer += 5;
        }
    });

    return answer;
}
