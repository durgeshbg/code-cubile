import myName from './myName';
import './style.css';
import Icon from './icon.png';

function component() {
    const element = document.createElement('div');
    element.innerHTML = myName('John');
    element.classList.add('hello');
    const myImage = new Image();
    myImage.src = Icon;
    element.appendChild(myImage);
    return element;
}

document.body.appendChild(component());
