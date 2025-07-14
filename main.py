import sys
from reddit_scraper import get_user_content
from persona_builder import generate_persona

def extract_username(profile_url):
    return profile_url.rstrip("/").split("/")[-1]

def save_persona_to_file(username, persona_text):
    with open(f"user_{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"Persona saved to user_{username}_persona.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_profile_url>")
        sys.exit(1)

    url = sys.argv[1]
    username = extract_username(url)
    print(f"[+] Fetching data for Reddit user: {username}")
    
    user_data = get_user_content(username)
    if not user_data:
        print("[-] No data found.")
        sys.exit(1)

    print("[+] Generating persona...")
    persona = generate_persona(user_data)

    save_persona_to_file(username, persona)
