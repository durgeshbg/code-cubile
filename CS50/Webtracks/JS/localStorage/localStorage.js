if(!localStorage.getItem('counter')) {
    localStorage.setItem('counter',0);
}
document.addEventListener('DOMContentLoaded',function() {
    let counter = localStorage.getItem('counter');
    document.querySelector('h1').innerHTML = counter;
    document.querySelector('button').onclick = () => {
        counter++;
        document.querySelector('h1').innerHTML = counter;
        localStorage.setItem('counter', counter);
    };

});