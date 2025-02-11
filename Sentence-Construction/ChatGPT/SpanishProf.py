import ollama

def spanish_tutor(prompt):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

while True:
    user_input = input("Ask me something in Spanish (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    print("AI Tutor:", spanish_tutor(user_input))

