import js2py;



// Print 1-225
/*
function Print1To255(){
    for(var i = 1; i <= 225; i++) {
        console.log(i);
    }
}
Print1To255()
// Print Odds 1-225
function PrintOdds1To155(){
    for(var i = 1; i <= 225; i+=2) {
        console.log(i);
    }
}
PrintOdds1To155()
// Iterate and Print Array
function PrintArrayVals(arr){
    var arrayLength = myArr.length
    for(var i = 0; i<arrayLength; i++){
        console.log(myArr[i]);
    }
}
PrintArrayVals([2,5,6,7,1]);
// Print Ints and Sum 0-255
function PrintIntsAndSum0To255(){
    var total = 0
    for(var i = 0; i<=255; i++){
        total += i;
        console.log("integer: "+ i);
        console.log("sum: "+ total);
    } 
}
PrintIntsAndSum0To255()
// Find and Print Max
function PrintMaxOfArray(arr){
    var max = arr.reduce(function(a, b) {
        return Math.max(a, b);
    });
    console.log(max)
}
PrintMaxOfArray([1,45,3,6,2,78])
// Get and Print Average
function PrintAverageOfArray(arr){
    var sum = arr.reduce((previous, current) => current += previous);
    var avg = sum/arr.length;
    console.log(avg);
}
PrintAverageOfArray([1,45,3,6,2,78])
// Array with Odds
function ReturnOddsArray1To255(){
    var arr = [];
    for(i=1; i<=255; i+=2){
        arr.push(i);
    }
    console.log (arr);
}
ReturnOddsArray1To255()
// Square the Values
function SquareArrayVals(arr){
    
    var arrSquared =  arr.map(function (x) {
        return Math.pow(x, 2);
         });
    console.log(arrSquared)
}
SquareArrayVals([3,1,5,8])
// Greater than Y
function ReturnArrayCountGreaterThanY(arr,y){
    var counter = 0;
    for(var i=0; i<arr.length; i++){
        if(arr[i] > y){
        counter++; 
        }
    }
    console.log(counter);
    return counter;
}
ReturnArrayCountGreaterThanY([3,4,12,78,2], 11)
// Zero Out Negative Numbers
function ZeroOutArrayNegativeVals(arr){
    for(var i=0; i<arr.length;i++){
        if(arr[i]<0){
            arr[i]=0
        }
    }
    console.log(arr);
    return arr;
}
ZeroOutArrayNegativeVals([-3,3,-6,5,8])
// Max, Min, Average
function PrintMaxMinAverageArrayVals(arr){
    var max = arr.reduce(function(a, b) {
        return Math.max(a, b);
    });
    console.log(max);
    var min = arr.reduce(function(a, b) {
        return Math.min(a, b);
    });
    console.log(min);
    var sum = arr.reduce((previous, current) => current += previous);
    var avg = sum/arr.length;
    console.log(avg);
}
PrintMaxMinAverageArrayVals([4,6,1,9,22])
// Shift Array Values
function ShiftArrayValsLeft(arr){
    for(var i=0;i<arr.length;i++){
        arr[i] = (arr[i+1] || 0) ;  
    }
    console.log(arr);
}
ShiftArrayValsLeft([1,2,3,4,5])
// Swap String For Array Negative Values
function SwapStringForArrayNegativeVals (arr){
    for(var i=0; i<arr.length;i++){
        if(arr[i]<0){
            arr[i]= "Dojo";
        }
    }
    console.log(arr);
}
SwapStringForArrayNegativeVals([3,-9,3,3,-1])
*/
