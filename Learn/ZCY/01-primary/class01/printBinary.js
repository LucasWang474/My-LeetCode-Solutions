// 从左到右打印一个 32 位整数的二进制表示

function printBinary(num) {
    // res 仅供测试用，实际上可以每次循环时直接打印对应的二进制位数，
    // 这样空间复杂度就是 O(1) 了
    let res = [];
    for (let i = 31; i >= 0; i--) {
        if (num & (1 << i)) {
            res.push(1);
        } else {
            res.push(0);
        }
    }
    return res.join('');
}

function bruteForce(num) {
    let res = num.toString(2);
    let zeros = 32 - res.length;
    return '0'.repeat(zeros) + res;
}

function test() {
    // 仅测试非负整数
    const times = 1000000;
    const MIN = 0, MAX = 2 ** 32 - 1;
    for (let i = 0; i < times; i++) {
        const num = Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;
        const expected = bruteForce(num);
        const actual = printBinary(num);
        if (expected !== actual) {
            console.log('num:', num);
            console.log('expected:', expected);
            console.log('actual:', actual);
            return;
        }
    }
    console.log('All passed!');
}

test();
