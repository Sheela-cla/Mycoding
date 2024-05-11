function Calc() {
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    var error = "Enter a number ";
    if (num1 != parseFloat(num1)) {
        document.getElementById('num1').value = error;
    }
    else if (num2 != parseFloat(num2)) {
        document.getElementById('num2').value = error;
    }
    else {
        var num1Value = parseFloat(num1);
        var num2Value = parseFloat(num2);

        var sum = num1Value + num2Value;

        document.getElementById('sum').value = sum;
    }
    
}