import myName from './myName';
import './style.css';
import Icon from './icon.png';
import Data from './data.csv';
import Notes from './data.xml';
import toml from './data.toml';
import yaml from './data.yaml';
import json5 from './data.json5';

function component() {
    const element = document.createElement('div');
    element.innerHTML = myName('John');
    element.classList.add('hello');
    const myImage = new Image();
    myImage.src = Icon;
    element.appendChild(myImage);

    console.log(Data);
    console.log(Notes);
    console.log(toml);
    console.log(yaml);
    console.log(json5);
    return element;
}

document.body.appendChild(component());
