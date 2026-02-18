import os
from groq import Groq

def main():
    api_key = input("Enter your GROQ_API_KEY: ").strip()
    client = Groq(api_key=api_key)

    print("Groq Chat — type 'quit' to exit\n")

    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user = input("You: ")

        if user.lower() == "quit":
            print("Bye!")
            break

        messages.append({"role": "user", "content": user})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
        )

        reply = response.choices[0].message.content
        print("\nAssistant:", reply, "\n")

        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
