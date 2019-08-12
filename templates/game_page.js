const alphabet = document.querySelector('#alphabet')
document.addEventListener('onclick', (event)=> {
  console.log('letter clicked');
  alphabet.style.backgroundColor= 'yellow';
})
var highlight = (button) => {
  if(button.style.backgroundColor == 'yellow'){
    console.log('letter clicked');
    button.style.backgroundColor= 'white';
  }
  else {
    button.style.backgroundColor= 'yellow';
  }
}
