
# ✋🖱️ AirClick – AI-Powered Virtual Mouse

**AirClick** turns your hand into a virtual mouse using AI-powered hand tracking. Move your index finger to control the cursor and pinch with your middle finger to click—no physical mouse required!

---

## 🛠️ Built With
- **[MediaPipe](https://github.com/google/mediapipe)** – Real-time hand tracking (21 landmarks).
- **[OpenCV](https://opencv.org/)** – Webcam access & frame processing.
- **[AutoPy](https://github.com/autopilot-rs/autopy)** – Controls your mouse programmatically.

---

## ✨ Features
✅ **Cursor Movement** – Move your index finger to control the mouse  
✅ **Left-Click Gesture** – Pinch index and middle fingers to click  
✅ **Smooth Tracking** – AI stabilizes movement for precision  
✅ **FPS Counter** – Monitor real-time performance  

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lourimi-ayoub/AirClick.git
   cd AirClick
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the virtual mouse**
   ```bash
   python virtualmouse.py
   ```

---

## 🎮 How to Use

| Gesture | Action             |
|---------|--------------------|
| 👆      | Index finger up → Move cursor |
| 🤏      | Pinch (index + middle) → Left click |
| 🖐️      | Open hand → Pause control |
| ❌      | Press `Q` → Quit the app |

---

## 🔍 How It Works

- **Hand Detection** – MediaPipe detects and tracks 21 key points of your hand.
- **Cursor Control** – Your index fingertip coordinates map to screen movement.
- **Click Detection** – When index and middle fingers pinch together, it simulates a left-click.
- **Smoothing Algorithm** – Reduces jitter to create natural movement.

---

## 🤝 Contributing
We welcome all contributions!  
- Fork the repo  
- Make your changes  
- Submit a Pull Request  

Open issues for any bugs or feature suggestions.

---

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
**Ayoub Lourimi**  
[GitHub](https://github.com/lourimi-ayoub) | [LinkedIn](https://www.linkedin.com/in/ayoub-lourimi)

---

🚀 **Happy Gesture Controlling with AirClick!** 🚀
