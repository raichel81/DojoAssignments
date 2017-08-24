function numberOnlyArray(arr){
    var numArr = []
    for (var i = 0; i < arr.length; i++) {
        if (typeof arr[i] === 'number'){
            numArr.push(arr[i]);
        }
    }
console.log(numArr);
}

numberOnlyArray(["yes", 4, .98, 0, "jim", true, 67]);
