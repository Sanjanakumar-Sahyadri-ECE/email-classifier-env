# Email Classification Environment

## Description
This project simulates a real-world email classification system where an agent identifies whether an email is spam or not spam.

## Features
- Random email generation
- Reward-based system
- Multiple difficulty levels (easy, medium, hard)
- Simple environment simulation using OpenEnv structure

## Environment Design
- State: Email text
- Action: "spam" or "not spam"
- Reward:
  - +1 → Correct prediction
  - -0.5 → Wrong prediction
  - -1 → Invalid input

## Files
- env.py → Environment logic
- main.py → Run the environment
- tasks.py → Difficulty levels
- grader.py → Scoring system

## How to Run
1. Install Python
2. Run the command:
   python main.py

## Example Output
Email: Win money now!!!
Enter prediction: spam
Reward: 1

## Conclusion
This project demonstrates how reinforcement learning environments can be simulated for real-world problems like spam detection.