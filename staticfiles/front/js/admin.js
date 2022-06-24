
const input = document.getElementById('id_payment_descount');

input.addEventListener('input', event => {
  if (input.value === '') {
    input.style.backgroundColor = '';
  } else {
    input.style.backgroundColor = 'white';
  }
});