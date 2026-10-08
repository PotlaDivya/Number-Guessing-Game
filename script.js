let number = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

function checkGuess() {

    let guess = Number(document.getElementById("guess").value);
    attempts++;

    if (guess < number) {
        document.getElementById("message").innerText = "Too low! Try again.";
    }

    else if (guess > number) {
        document.getElementById("message").innerText = "Too high! Try again.";
    }

    else {
        document.getElementById("message").innerText =
            "🎉 Correct! You won!";
    }

    document.getElementById("attempts").innerText =
        "Attempts: " + attempts;
}