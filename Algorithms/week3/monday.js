// var arr1 = ["cats","cows", "dogs","ducks"];
// var arr2 = ["meow","moo","woof","quack"];

function createObj(arr1,arr2) {
    var obj = {};
    for(var i = 0; i<arr1.length; i++){
        var key = arr1[i];
        var val = arr2[i];
        obj[key]= val;
    }
    console.log(obj);
    return obj; 
}

createObj(["cats","cows", "dogs","ducks"],["meow","moo","woof","quack"]);

var newObj = obj;

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