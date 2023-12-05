import myName from "./myName";

function component() {
    const element = document.createElement('div');
    element.innerHTML = myName('John')
    return element;
    
}

document.body.appendChild(component());
