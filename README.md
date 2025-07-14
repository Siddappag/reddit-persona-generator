# Reddit User Persona Generator 🧠

This project generates a user persona from a Reddit profile by:
- Scraping recent posts/comments
- Feeding the content into GPT-3.5
- Outputting a persona with cited content

---

## 🔧 Technologies Used
- Python 3
- PRAW (Reddit API)
- OpenAI GPT-3.5
- VS Code

---

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt


Add your OpenAI API key inside persona_builder.py:

python
Copy code
client = openai.OpenAI(api_key="YOUR_API_KEY")


Add your Reddit API credentials inside reddit_scraper.py:

python
Copy code
praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_SECRET",
    user_agent="YOUR_USER_AGENT"
)


 How to Run
bash
Copy code
python main.py https://www.reddit.com/user/kojied/
This will:

Fetch user comments/posts

Generate a persona using GPT

Save output in: user_kojied_persona.txt



Output
Two sample output files are included:

user_kojied_persona.txt

user_hungry_persona.txt

Each file contains:

Interests

Personality traits

Emotional cues

Citations for each insight# reddit-persona-generator
