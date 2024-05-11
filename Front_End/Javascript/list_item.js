
function addItem() {
    
    const newdata = document.getElementById('newText');
    const updatedlist = document.getElementById('items');

   
    const newItem = document.createElement('li');
    const deleteoption = document.createElement('a')
    deleteoption.textContent = '[Delete]';
    // deleteoption.style.textDecorationLine;

   
    newItem.textContent = newdata.value;

    newItem.appendChild(deleteoption);
   
    updatedlist.appendChild(newItem);

    newdata.value = '';

    
    deleteoption.addEventListener('click', function() {
        updatedlist.removeChild(newItem);
    });
}

