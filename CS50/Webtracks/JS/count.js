let c = 0;
document.addEventListener('DOMContentLoaded',function() {
    document.querySelector('button').onclick = function() {
        c++;
        document.querySelector('h1').innerHTML = c;
    }
})