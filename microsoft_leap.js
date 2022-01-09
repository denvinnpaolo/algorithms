// # Find the length of the longest numeric sequence in an unsorted array of integers. Input: [11,5,1,8,3,9,4,6]

const FindLongestNumericSequence = (nums) => {
    longest = 0
    
    const numSet = new Set(nums);
    
    numSet.forEach(num => {
        if (!numSet.has(num - 1)) {
            console.log(num)
            let currNum = num;
            let currStreak = 1;

            while (numSet.has(currNum + 1)) {
                currNum += 1
                currStreak += 1
            };
            console.log('streak: ', currStreak)
            if (currStreak > longest) {
                longest = currStreak;
            }

        }
    })    
    return longest
};

const a = [11,5,1,8,3,9,4,6]

FindLongestNumericSequence(a);


