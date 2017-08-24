
function playSlots(games){
    for (var i = 1; i <= games; i++) {
        if(Math.trunc(Math.random() * 100) === 5){
            var winnings = (Math.floor(Math.random()* 50)+50);
            console.log("Quarters left: " + (games - i) + " Quarters won:" + winnings);
            return (games - i) + winnings; 
        }
    }
    return "You lost everything: " + 0;
}

playSlots(10);