
function time(HOUR, MINUTE, PERIOD){
    function afterOrAlmost() {
        if(MINUTE < 30){
           MINUTE = "It's just after ";
        }
        else if(MINUTE === 30){
            MINUTE = "It's half past ";
        }
        else{
            MINUTE = "It's almost ";
            HOUR++;
        }
        function dayOrNight(){
            if (PERIOD === "AM"){
                PERIOD = " in the morning.";
            } 
            else{
                PERIOD = " in the evening.";
            }
        console.log(MINUTE, HOUR, PERIOD);
        }
        dayOrNight();
    } 
    afterOrAlmost();
}
time(8, 40, "PM");