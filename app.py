from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    def word_guess_game():
        # List of words to guess from
        words = ["python", "flask", "django", "javascript", "html", "css", "react", "node", "ruby", "java"]
        # Select a random word
        word_to_guess = random.choice(words)
        word_length = len(word_to_guess)
        attempts_left = 6  # Number of attempts allowed

        # HTML and JS to display the game
        html_content = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px; text-align: center;">
            <h2>Guess the Word Game!</h2>
            <p>Try to guess the word! It's {word_length} letters long.</p>
            <div id="attempts">Attempts Left: {attempts_left}</div>
            <p><span id="hint">_ " * {word_length}</span></p>
            <input type="text" id="guessInput" maxlength="1" placeholder="Enter letter" style="padding: 10px; font-size: 16px;">
            <button onclick="guessLetter()">Guess</button>
            <p id="message"></p>
        </div>

        <script>
            let word = "{word_to_guess}";
            let attempts = {attempts_left};
            let guessedLetters = [];
            let displayWord = "_".repeat({word_length});

            function guessLetter() {{
                const guess = document.getElementById("guessInput").value.toLowerCase();
                if (guess.length !== 1 || guessedLetters.includes(guess)) {{
                    document.getElementById("message").innerText = "Please enter a valid and unique letter.";
                    return;
                }}
                guessedLetters.push(guess);
                if (word.includes(guess)) {{
                    displayWord = updateDisplayWord(guess);
                    document.getElementById("hint").innerText = displayWord;
                    if (displayWord === word) {{
                        document.getElementById("message").innerText = "You guessed the word! Congratulations!";
                        document.getElementById("message").style.color = "green";
                    }} else {{
                        document.getElementById("message").innerText = "Correct! Keep going.";
                    }}
                }} else {{
                    attempts--;
                    document.getElementById("attempts").innerText = "Attempts Left: " + attempts;
                    if (attempts === 0) {{
                        document.getElementById("message").innerText = "Sorry, you've lost! The word was: " + word;
                        document.getElementById("message").style.color = "red";
                    }} else {{
                        document.getElementById("message").innerText = "Incorrect! Try again.";
                    }}
                }}
                document.getElementById("guessInput").value = "";
            }}

            function updateDisplayWord(letter) {{
                let newDisplay = "";
                for (let i = 0; i < word.length; i++) {{
                    newDisplay += (word[i] === letter || guessedLetters.includes(word[i])) ? word[i] : "_";
                }}
                return newDisplay;
            }}
        </script>
        """
        return html_content

    return word_guess_game()  # Call the function to return the HTML content

if __name__ == '__main__':
    app.run(debug=True)
