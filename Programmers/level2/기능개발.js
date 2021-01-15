class Queue {
  constructor() {
    this.store = [];
  }
  enqueue(item) {
    this.store.push(item);
  }
  dequeue(item) {
    this.store.shift();
  }
}

function solution(progresses, speeds) {
  var answer = [0];
  const queue = new Queue();
  progresses.forEach((progress, index) => {
    queue.enqueue(Math.ceil((100 - progress) / speeds[index]));
  });

  let maxDay = queue.store[0];
  for (let i = 0, j = 0; i < queue.store.length; i++) {
    if (queue.store[i] <= maxDay) {
      answer[j] += 1;
    } else {
      maxDay = queue.store[i];
      answer[++j] = 1;
    }
  }
  return answer;
}
