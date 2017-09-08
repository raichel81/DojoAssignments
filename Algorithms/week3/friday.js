// // 


function doubleTroubleCheaper(arr){
    var delta = arr.length-1;
    arr.map(el=>{arr.push(el)})
    for (var i=1;i<arr.length-1;i++){
        var temp = arr[i];
        arr[i] = arr[i+delta];
        arr[i+delta] = temp;
    }
    console.log(arr);
}
doubleTroubleCheaper([2, 3, 54,"dog","re"]);

// function zip(arr1,arr2){
//     if(Array.isArray(arr1) && Array.isArray(arr2)){
//         var result = [];
//         var pointer1 = 0;
//         var pointer2 = 0;
//         while(pointer1 < arr1.length && pointer2 < arr2.length){
//             var val1 = arr1[pointer1];
//             var val2 = arr2[pointer2];
//             result.push(val1, val2);
//             pointer1 += 1
//             pointer2 += 1
//         }
//     if (pointer1 < arr1.length){
//         for(var i = pointer1;i<arr1.length;i++){
//             result.push(arr1[i]);
//         }
//     if(pointer2 < arr2.length){
//         for(var i = pointer2;i<arr2.length;i++){
//             result.push(arr2[i]);
//         }
//     }}}
//     console.log(result);
// }
// zip([2, 3, 54,"dog","re"],[33, 0, true]);