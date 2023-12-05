import _ from 'lodash';
import printMe from './print';

import './style.css';
import Icon from './assets/images/icon.png';
import Data from './assets/data/data.csv';

function component() {
    const element = document.createElement('div');
    const btn = document.createElement('button');

    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    element.classList.add('hello');

    const myImage = new Image();
    myImage.src = Icon;
    element.appendChild(myImage);

    console.log(Data);

    btn.innerHTML = 'Click me to log!';
    btn.onclick = printMe;
    element.appendChild(btn);

    return element;
}

document.body.appendChild(component());
