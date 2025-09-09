# 🃏 Blackjack Web App (Python + Flask + AWS)

A fully deployed web-based Blackjack game built with **Python** and **Flask**, hosted on **AWS Elastic Beanstalk**, and served over **HTTPS** with a **custom domain** via **Route 53** and **ACM**.

🎯 **Live App:** [https://www.martinscloud.be/blackjack](https://www.martinscloud.be/blackjack)

---

## 🚀 Project Overview  
This project started as a simple Python terminal game and evolved into a deployed web application.  
I used this as an opportunity to learn real-world deployment skills by taking a backend game, wrapping it in a web framework, and deploying it securely on AWS infrastructure.

---

## 🧠 What I Learned & Implemented

✅ Built a full-stack web app using **Flask**  
✅ Designed a dynamic interface with **HTML/CSS/JS** and **Jinja2**  
✅ Deployed using **AWS Elastic Beanstalk** with application load balancing  
✅ Connected a custom domain (`martinscloud.be`) via **Route 53**  
✅ Secured the site using **HTTPS** through **AWS ACM**  
✅ Managed secrets (`SECRET_KEY`) via **AWS Parameter Store**  
✅ Configured health checks and load balancer target groups  
✅ Migrated from NGINX-based proxying to native HTTPS with **ACM + ALB**

---

## 🧩 Game Features

- Player and computer each start with 2 cards  
- You can **Hit** (draw a card) or **Stand** (end your turn)  
- Aces count as 1 or 11, whichever is more helpful  
- Go over 21 and you **bust**  
- Game ends with a result message and option to restart  
- Helpful **“How It Works?”** popup built with JavaScript

---

## 🌐 Technologies Used

| Tool / Service         | Role                          |
|------------------------|-------------------------------|
| Python, Flask          | Backend logic and routing     |
| Jinja2, HTML/CSS/JS    | Templating and UI             |
| AWS Elastic Beanstalk  | Hosting and deployment        |
| AWS Route 53           | DNS + custom domain           |
| AWS ACM                | SSL/TLS certificate (HTTPS)   |
| AWS ALB (Load Balancer)| HTTPS and health checks       |
| AWS Parameter Store    | Secure secret management      |
| Git & GitHub           | Version control and portfolio |

---

## 📦 Run the App Locally

You can clone and run this Flask app locally:

```bash
git clone https://github.com/MartijnMGit/blackjack-flask.git
cd blackjack-flask
pip install -r requirements.txt
export SECRET_KEY="your_own_secret"  # Or set via .env
python application.py
```

Then open http://localhost:5000 in your browser.

---

## 🛠 Future Improvements

Add user login & sessions 

Store win/loss history

Add animations and sounds

Multiplayer support

Docker support for easier deployment

Automated tests using pytest

---

## 💼 Why This Project?

I built this to bridge the gap between Python scripting and full web deployment. It demonstrates my understanding of software development and cloud architecture, and serves as a showcase of how I learn by building and shipping real projects.

