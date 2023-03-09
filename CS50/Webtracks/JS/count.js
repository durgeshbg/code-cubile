if (!localStorage.getItem('count')) {
    localStorage.setItem('count', 0);
}
function count() {
    let c = localStorage.getItem('count');
    c++
    document.querySelector('h1').innerHTML = c;
    localStorage.setItem('count', c);
}
document.addEventListener('DOMContentLoaded',function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('count');
    document.querySelector('button').onclick = count;
})