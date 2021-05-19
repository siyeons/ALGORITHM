function solution(bridge_length, weight, truck_weights) {
    const firstTruck = truck_weights.shift();

    let bridge = new Array(bridge_length - 1).fill(0);
    bridge.push(firstTruck);

    let bridgeWeight = firstTruck;
    let time = 1;

    while (bridgeWeight) {
        bridgeWeight = bridgeWeight - bridge.shift();
        const nextTruckWeight = truck_weights[0];

        if(bridgeWeight + nextTruckWeight <= weight) {
            bridge.push(nextTruckWeight);
            truck_weights.shift();
            bridgeWeight = bridgeWeight + nextTruckWeight;
        } else {
            bridge.push(0);
        }
        time++;
    }
    return time;
}
