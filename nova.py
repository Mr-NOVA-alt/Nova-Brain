import os
from openai import OpenAI

# Pulls your API key securely from your cloud environment secrets
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

print("--- N.O.V.A. Cloud Core V2: Active ---")

def talk_to_nova():
    # Setting up N.O.V.A.'s core master identity
    system_instruction = (
        "You are N.O.V.A. (Neural Operational Virtual Assistant). "
        "Your creator is Boss Aditya. You are a genius software engineer "
        "and autonomous system built to design apps, games, and code perfectly."
    )
    
    print("\nSystem: Connection secure. Start chatting with N.O.V.A.!")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Disconnecting from N.O.V.A. core...")
            break
            
        print("\n[N.O.V.A. is processing...]")
        
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-chat", 
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = completion.choices[0].message.content
            print(f"\nN.O.V.A.:\n{reply}")
            
        except Exception as e:
            print(f"\nConnection Error: {e}")

if __name__ == "__main__":
    if not api_key:
        print("ERROR: OPENROUTER_API_KEY secret not found in your environment settings!")
    else:
        talk_to_nova()
      
