var arr1 = ["cats","cows", "dogs","ducks"];
var arr2 = ["meow","moo","woof","quack"];

function createObj(arr1,arr2) {
    var newObj = {};
    for(var i = 0; i<arr1.length; i++){
        var key = arr1[i];
        var val = arr2[i];
        newObj[key]= val;
    }
    console.log(newObj);
    return newObj; 
}

createObj(arr1,arr2);

var newObj = createObj(arr1,arr2);

function reverseObj(newObj) {
    for (var key in newObj){
        var val = newObj[key];
        newObj [val] = key;
        delete newObj[key];
    }
    console.log(newObj);
    return newObj;
}
reverseObj(newObj);