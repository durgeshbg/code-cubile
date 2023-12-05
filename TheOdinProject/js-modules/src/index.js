import myName from './myName';
import './style.css';
import Icon from './icon.png';
import Data from './data.csv';
import Notes from './data.xml';

function component() {
    const element = document.createElement('div');
    element.innerHTML = myName('John');
    element.classList.add('hello');
    const myImage = new Image();
    myImage.src = Icon;
    element.appendChild(myImage);

    console.log(Data);
    console.log(Notes);
    return element;
}

document.body.appendChild(component());
