
var weekday = true;
var vacation= true;
    function sleepin(weekday,vacation)
    {
        if(weekday==false || vacation==true){
            return("True");
         }
        else {
            return("False");
        }
}

console.log(sleepin(false,false));
console.log(sleepin(true,false));
console.log(sleepin(false,true));

