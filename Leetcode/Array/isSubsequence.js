const isSubsequence = (s, t) => {
    if (s.length === 0) return true;
    let sIdx = 0;
    for (let i = 0 ; i < t.length ; i += 1) {
        if (t[i] === s[sIdx]) sIdx += 1;
        if (sIdx === s.length) return true;
    }
    return false;
};
