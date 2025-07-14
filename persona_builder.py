import openai


from dotenv import load_dotenv
import os
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_persona(user_data):
    content_blocks = [entry['body'] if entry['type'] == 'comment' else entry['title'] + "\n" + entry['body'] for entry in user_data]

    prompt = (
        "You are an AI that generates a detailed user persona based on Reddit content. "
        "A user persona includes interests, personality traits, profession, age group, etc. "
        "For each trait, cite the post/comment used.\n\n"
        "Here are Reddit posts/comments:\n\n"
    )

    prompt += "\n\n".join([f"{i+1}. {block}" for i, block in enumerate(content_blocks[:20])])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
