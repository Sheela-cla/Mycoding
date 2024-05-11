function showText() {
    const hiddentext = document.getElementById('text');
    const moretext = document.getElementById('more');

    hiddentext.style.display = 'block';
    moretext.style.display = 'none';
    let newtext = '';
    for (let i = 0 ; i < 30 ; i++) {
        newtext += hiddentext.textContent + '';
    }
document.getElementById('text').textContent = newtext;
 }
