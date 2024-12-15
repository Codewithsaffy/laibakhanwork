let randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts =0;
const userInput = document.querySelector('.Search_bar'); 
const guessButton = document.querySelector('.check');
const guideText = document.querySelector('.guide');
const attemptCount = document.querySelector('.attempt_no');
const newGameButton = document.querySelector('.new_game');

guessButton.addEventListener('click', () => {
  const userGuess = Number(userInput.value);
  if (isNaN(userGuess) || userGuess < 1 || userGuess > 100){
    guideText.textContent = 'Please enter a valid number between 1 and 100.';
    return;
  }
  attempts++;
  attemptCount.textContent = attempts;
  if (userGuess === randomNumber){
    guideText.textContent = `🎉 Correct! The number was ${randomNumber}.`;
    guideText.style.color = '';
  }
  else if (userGuess < randomNumber){
    guideText.textContent = ' 📉 Try a higher number ';
    guideText.style.color = '';
  }  
  else{
    guideText.textContent = ' 📈 Try a lower number ';
    guideText.style.color = '';
  }
  userInput.value = '';
});

newGameButton.addEventListener('click', () => {
  randomNumber = Math.floor(Math.random() * 100) + 1; // Generate a new random number
  attempts = 0; // Reset attempts
  attemptCount.textContent = attempts;
  guideText.textContent = 'Please guess a number';
  guessInput.value = '';
})