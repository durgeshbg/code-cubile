import './style.css';
import Icon from './assets/images/icon.png';
import Data from './assets/data/data.csv';
import _ from 'lodash';

function component() {
    const element = document.createElement('div');
    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    element.classList.add('hello');

    const myImage = new Image();
    myImage.src = Icon;
    element.appendChild(myImage);

    console.log(Data);

    return element;
}

document.body.appendChild(component());
