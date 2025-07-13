import sys
import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

def generate_story_with_wallet_name(wallet_name, words):
    """
    Generate a story using OpenAI GPT-3.5-turbo with the wallet name as central character/theme
    """
    load_dotenv()
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create a prompt that makes the wallet name central to the story
    prompt = f"""Create a short, creative story (2-3 paragraphs) where '{wallet_name}' is the central character or central theme of the story. 

    The story should prominently feature '{wallet_name}' - either as a character name, location, or central concept that readers can easily recognize.
    
    Naturally incorporate these additional words into the story: {', '.join(words)}.
    
    Make the story engaging and adventurous, where '{wallet_name}' plays a key role in the narrative. The other words should feel like they belong naturally in the story alongside '{wallet_name}'.
    
    For example, if the wallet name is 'Alaska', make Alaska central to the story - perhaps as a character named Alaska, or a story set in Alaska, or about someone going to Alaska."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative storyteller who can make any name central to an engaging narrative while naturally incorporating random words."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.8
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error generating story: {str(e)}"

def save_story_to_file(wallet_name, story, selected_words):
    """
    Save the story to a text file with timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"story_{wallet_name}_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Wallet Story for: {wallet_name}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Selected words: {', '.join(selected_words)}\n")
        f.write("-" * 60 + "\n\n")
        f.write(story)
        f.write("\n\n" + "-" * 60 + "\n")
    
    return filename

def main():
    # Get wallet name and words from command line arguments
    if len(sys.argv) < 3:
        print("Usage: python Story.py <wallet_name> <word1> <word2> <word3> ...")
        print("Example: python Story.py Alaska weasel blind omit")
        return
    
    wallet_name = sys.argv[1]
    selected_words = sys.argv[2:]
    
    print(f"Generating story with '{wallet_name}' as the central theme...")
    print(f"Additional words: {', '.join(selected_words)}")
    print("-" * 60)
    
    story = generate_story_with_wallet_name(wallet_name, selected_words)
    print(story)
    print("-" * 60)
    
    # Save story to file
    filename = save_story_to_file(wallet_name, story, selected_words)
    print(f"Story saved to: {filename}")

if __name__ == "__main__":
    main()





