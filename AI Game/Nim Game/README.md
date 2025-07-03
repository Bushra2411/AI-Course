# 🪨 Nim Game – Human vs AI

This is a simple terminal-based **Nim Game** where a human player competes against an AI. The AI uses the **Minimax algorithm** to make optimal moves.

---

## 🛠️ How to Run the Game

1. **Make sure have Python installed** (version 3.x).
2. Open terminal or command prompt.
3. Navigate to the folder where `nim_game.py` file is saved.
4. Run the game using:

`python nim_game.py`


## 📦 Requirements

No additional libraries or frameworks are needed.

✅ Only **Python 3.x** is required.

---

## 🎮 How to Play

* The game starts with **10 stones** in a pile.
* **Two players** take turns: **Human** and the **AI**.
* On each turn, a player can remove **1 to 3 stones**.
* The player who **picks the last stone wins**.

**Example:**

* If there are 4 stones left and you pick 3, the AI will have to pick the last 1 stone (and win).

---

## 🤖 Algorithm Used

This game uses the **Minimax algorithm** to determine the AI's best move.

* The algorithm simulates all possible future game states.
* It assumes the opponent (human) plays optimally.
* The AI always tries to **maximize its chances of winning**.

