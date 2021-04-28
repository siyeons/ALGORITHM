const leastInterval = (tasks, n) => {
    const taskCounts = [];

    for (let i = 0; i < tasks.length; i++) {
        let index = taskCounts.findIndex((el) => el[0] === tasks[i]);

        if (index === -1) {
            taskCounts.push([tasks[i], 1]);
        } else {
            taskCounts[index][1] += 1;
        }
    }

    taskCounts.sort((a, b) => b[1] - a[1]);

    let maxVal = taskCounts[0][1] - 1;
    let idleSlots = maxVal * n;

    for (let i = 1; i < taskCounts.length; i++) {
        idleSlots -= Math.min(taskCounts[i][1], maxVal);
    }

    return idleSlots > 0 ? idleSlots + tasks.length : tasks.length;
};
