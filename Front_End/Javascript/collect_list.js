function extractText() {
    const list = document.getElementById('items');
    const textarea = document.getElementById('result');
    let extractedtext = '';
    for (let i=0; i< list.children.length;i++)
    {
       extractedtext += list.children[i].textContent + '\n' ;
    }
 textarea.value= extractedtext;
}
