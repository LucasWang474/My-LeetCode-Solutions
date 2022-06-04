/**
 * https://leetcode.com/problems/single-number-ii/
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    return singleNumberKM(nums, 1, 3);
};

// 假设一个数组中只有一个数出现了 K 次，其余的都出现了 M 次，并且 1 <= K < M
function singleNumberKM(nums, K, M) {
    const bitCounts = Array(32).fill(0);
    for (let num of nums) {
        for (let i = 0; i <= 31; i++) {
            bitCounts[i] += (num >> i) & 1;
        }
    }
    
    let res = 0;
    for (let i = 0; i <= 31; i++) {
        if ((bitCounts[i] % M) !== 0) {
            res |= (1 << i);
        }
    }
    return res;
}

function bruteForce(nums, K, M) {
    let numToCount = {};
    for (let num of nums) {
        if (num in numToCount) {
            numToCount[num]++;
        } else {
            numToCount[num] = 1;
        }
    }
    let res;
    for (let num in numToCount) {
        if (numToCount[num] === K) {
            res = num;
        } else if (numToCount[num] !== M) {
            console.log('nums:', nums);
            console.log('K:', K);
            console.log('M:', M);
            console.log('numToCount:', numToCount);
            throw new Error('Invalid input!');
        }
    }
    return res;
}


function test() {
    const times = 100000;
    const MIN_COUNT = 1, MAX_COUNT = 30; // 这个不需要太大
    const MIN_NUM = -(2 ** 31), MAX_NUM = 2 ** 31;
    const MIN_LEN = 2, MAX_LEN = 30; // 这个不需要太大
    
    for (let i = 0; i < times; i++) {
        let K = Math.trunc(Math.random() * (MAX_COUNT - MIN_COUNT + 1)) + MIN_COUNT;
        let M = Math.trunc(Math.random() * (MAX_COUNT - MIN_COUNT + 1)) + MIN_COUNT;
        K = Math.min(K, M);
        M = Math.max(K, M);
        if (K === M) {
            continue;
        }
        
        const KNum = Math.trunc(Math.random() * (MAX_NUM - MIN_NUM + 1)) + MIN_NUM;
        const nums = Array(K).fill(KNum);
        const LEN = Math.trunc(Math.random() * (MAX_LEN - MIN_LEN + 1)) + MIN_LEN;
        const MNums = new Set();
        for (let i = 0; i < LEN; i++) {
            let curNum;
            do {
                curNum = Math.trunc(Math.random() * (MAX_NUM - MIN_NUM + 1)) + MIN_NUM;
            } while (MNums.has(curNum));
            
            for (let j = 0; j < M; j++) {
                nums.push(curNum);
            }
            MNums.add(curNum);
        }
        
        const expected = +bruteForce(nums, K, M);
        const actual = +singleNumberKM(nums, K, M);
        if (expected !== actual) {
            console.log('nums:', nums);
            console.log('K:', K);
            console.log('M:', M);
            console.log('expected:', expected);
            console.log('actual:', actual);
            return;
        }
    }
    console.log('All passed!');
}

test();
