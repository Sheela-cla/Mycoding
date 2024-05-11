function monkeyTrouble(asmile,bsmile){
    if (asmile && bsmile){
        return true;
    }
    else if (!asmile && !bsmile){
        return true;
    }
    else{
        return false;
    }
}
 
console.log(monkeyTrouble(true, true));
console.log(monkeyTrouble(false, false));
console.log(monkeyTrouble(true, false));