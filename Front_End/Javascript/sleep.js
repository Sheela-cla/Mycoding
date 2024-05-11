function sleepIn (weekday,vacation){
    if (!weekday || vacation){
        return true;
    }else{
        return false;
    }
}
 
 
console.log(sleepIn(false, false));
console.log(sleepIn(true, false));  
console.log(sleepIn(false, true));
