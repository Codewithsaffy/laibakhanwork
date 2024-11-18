// const variable = 'hello';
// switch (variable) {
//   case 'Oranges':
//     console.log('Oranges are $0.59 a pound.');
//     break;
//   case 'Mangoes':
//   case 'Papayas':
//     console.log('Mangoes and papayas are $2.79 a pound.');
//     // Expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
//   default:
//     console.log(`Sorry, we are out of ${variable}.`);
// }

const variable = prompt ('Enter a color');
switch (variable){
  case 'red':
    console.log ('red is red');
    break;
  case 'pink':
    case 'yellow':
    console.log ('pink and yellow are pink and yellow');
    break;
}
