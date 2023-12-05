import myName from './myName';
import './style.css';

function component() {
    const element = document.createElement('div');
    element.innerHTML = myName('John');
    element.classList.add('hello');
    return element;
}

document.body.appendChild(component());
