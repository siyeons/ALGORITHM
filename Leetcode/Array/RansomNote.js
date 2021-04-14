const canConstruct = function(ransomNote, magazine) {
    magazine = [...magazine]

    for(const letter of ransomNote) {
        const index = magazine.indexOf(letter)

        if(index < 0) {
            return false
        }
        magazine[index] = null
    }

    return true
};
