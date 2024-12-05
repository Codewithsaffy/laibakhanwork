let userscore = 0;
let compscore = 0;

const choices = document.querySelectorAll(".choice");
const msg = document.querySelector("#msg");
const userscorepara = document.querySelector("#user_score");
const compscorepara = document.querySelector("#comp_score");

// Generate computer's choice
const getcompchoice = () => {
  const options = ["rock", "paper", "scissors"];
  const randIndex = Math.floor(Math.random() * 3);
  return options[randIndex];
};

// Handle a draw game
const drawgame = () => {
  msg.innerText = "Draw Game. Please Try Again";
  msg.style.backgroundColor = "#081b31";
};

// Show winner or loser message
const showwiner = (userwin, userchoice, compchoice) => {
  if (userwin) {
    userscore++;
    userscorepara.innerText = userscore;
    msg.innerText = `You win! ${userchoice} beats ${compchoice}`;
    msg.style.backgroundColor = "green";
  } else {
    compscore++;
    compscorepara.innerText = compscore;
    msg.innerText = `You lose! ${compchoice} beats ${userchoice}`;
    msg.style.backgroundColor = "red";
  }
};

// Play the game
const playgame = (userchoice) => {
  console.log("User Choice:", userchoice);

  // Generate computer choice
  const compchoice = getcompchoice();
  console.log("Computer Choice:", compchoice);

  // Check for a draw
  if (userchoice === compchoice) {
    drawgame();
    return;
  }

  // Determine if the user wins
  let userwin = false;
  if (userchoice === "rock") {
    userwin = compchoice === "scissors"; // Rock beats Scissors
  } else if (userchoice === "paper") {
    userwin = compchoice === "rock"; // Paper beats Rock
  } else if (userchoice === "scissors") {
    userwin = compchoice === "paper"; // Scissors beat Paper
  }

  showwiner(userwin, userchoice, compchoice);
};

// Add event listeners to all choice buttons
choices.forEach((choice) => {
  const userchoice = choice.getAttribute("id");
  choice.addEventListener("click", () => {
    playgame(userchoice);
  });
});
