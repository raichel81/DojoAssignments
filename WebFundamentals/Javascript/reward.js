
function doubleAmount() {
    var amt = 0.01;
    for (var i = 1; i <= 30; i++) {
        amt += amt;
    }
    console.log(amt);
}

doubleAmount();