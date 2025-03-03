# Connect Four Game 🎲🟡🔴

Welcome to the Connect Four Game repository! This project implements the classic Connect Four game using object-oriented programming and a layered architecture, where a human player faces off against a computer opponent. The game is designed with robust input validation, a strategic AI opponent, and an appealing color palette for your discs. Enjoy the friendly gameplay and have fun with your family and friends! 😊🎉

---

## Features 🌟

- **Layered Architecture & OOP**:  
  The code is organized into distinct layers:
  - **Core**: Game logic and models (board, players, AI, color utilities) 🧩
  - **Application**: Manages game state and flow 🚀
  - **UI**: Separate interfaces for console and (optionally) graphical play 🎨
  
- **Unit Testing**:  
  All non-trivial modules (except the UI) come with specifications and PyUnit test cases to ensure reliability and fun bug-free play! ✅

- **Human vs. Computer Gameplay**:  
  Challenge a friendly computer opponent that:
  - **Wins**: Seizes any opportunity to win.
  - **Blocks**: Prevents your one-move victories.
  - **Entertains**: Provides a fun, strategic challenge for players of all ages. 😄

- **Input Validation**:  
  The program protects against invalid input to keep your game running smoothly. 🚦

- **Customizable Color Palette**:  
  Choose your disc color from a variety of options:  
  **1**: Red, **2**: Green, **3**: Blue, **4**: Pink, **5**: Yellow.  
  (The computer uses a default color, White.) 🎨

- **Bonus Features**:
  - **Graphical User Interface (GUI)**: In addition to the console interface, a GUI is available, both sharing the same game layers. 🖥️
  - **Advanced AI (Minimax)**: For hard difficulty, the computer can use a minimax algorithm to make more competitive moves for a challenging match! 🤖
