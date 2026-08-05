<div align="center">

# 🤖 RL Quest

### Teaching an AI Agent to Explore, Learn, and Succeed

<img src="docs/banner.png" width="100%">

<br>

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?style=for-the-badge)
![Q-Learning](https://img.shields.io/badge/Reinforcement-Learning-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

</div>

## 🌲 About

RL Quest is a reinforcement learning playground built entirely from scratch using **Python** and **Pygame**.

Instead of hardcoding the solution, the robot learns through **trial and error** using the **Q-Learning algorithm**.

Watch the agent explore the environment, collide with obstacles, receive rewards, and eventually discover the optimal path completely on its own.

## ✨ Features

- 🤖 AI Agent powered by Q-Learning
- 🌲 Custom forest environment
- 🎮 Built with Pygame
- 🧠 Real-time learning
- 📊 Live training statistics
- 🎞 Animated robot
- 🪨 Obstacles and maze generation
- 🎯 Goal-based reward system


## 📸 Screenshots

### Current Gameplay

<p align="center">
  <img src="assets/image.png" width="700">
</p>

### Learning Process

<p align="center">
  <img src="docs/screenshot2.png" width="700">
</p>

### Forest Environment

<p align="center">
  <img src="docs/screenshot3.png" width="700">
</p>

## 📂 Project Structure

```text
RL-Quest/
│
├── assets/
│   ├── grass/
│   ├── robot/
│   ├── wall/
│   └── goal/
│
├── docs/
│   ├── banner.png
│   ├── screenshot1.png
│   └── demo.gif
│
├── game/
│   ├── agent.py
│   ├── animation.py
│   ├── draw.py
│   ├── qlearning.py
│   └── world.py
│
├── run.py
├── requirements.txt
├── README.md
└── LICENSE
```

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/RL-Quest.git
```

Move into the project

```bash
cd RL-Quest
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python run.py
```

