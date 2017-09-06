
// str = "08gsre9"
// function getStringDigits(str){
    // var result= "";
//     for(var i = 0;i<str.length;i++){
//         var char = str.charAt(i);
//         console.log(str.charAt(i));
//         console.log(result)
//         if(!isNaN(char)){
//             console.log(char);

//         }
//     }
//     console.log(Number(result.concat()));
// }
// getStringDigits(str);

function getStringDigits(str){
    var results = "";
    for (var i=0; i<str.length; i++){
        var char = str.charAt(i);
        if (char!== " " &&   !Number.isNaN(Number(char))){
            results +=char;
        }
    }
    console.log(Number(results));
    return Number(results);
}
  getStringDigits("0hytg00908yt" );

  function removeSpace(str){
    console.log(str.split(" ").join(''));
    return str.split(" ").join("");
  }
  removeSpace("I am cool");

  function firstletter(str){
    var words = str.split(" ");
    var newStr = "";
    for (var i=0; i<words.length; i++){
      var word = words[i];
      var letter = word.charAt(0);
      newStr += letter;
    }
    console.log(newStr.toUpperCase());
    return newStr.toUpperCase();
  }
  firstletter("hello - world");