import openai

openai.api_key = "  "

def call_gpt_api(role, model, messages):
    chat_response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    message = chat_response.choices[0].message['content'].strip()
    return message

def main():
    # Edit the role descriptions below
    role_descriptions = {
        "1": "You are an academic assistant who is good at find logical error in the paper. You will tell me the logicall errors of my inputs.",
        "2": "You are a native speaker assistant who is good at academic language polishing. You will use a native speaker and academic way provide a new rewrite of my inputs.",
        "3": "You are an assistant who is good at asking questions. You will raise possible doubts or questions based on a given content to promote more complete thinking by listing them into bullet points. You will also try to provide counter cases to examine if the claim has any potential of being wrong."
    }
    
    messages = [{"role": "system", "content": ""}]
    
    while True:
        print("\nSelect a role for GPT:")
        print("1. 逻辑漏洞")
        print("2. 润色")
        print("3. 追问讨论")
        print("4. Quit")

        role = input("Enter the role number (1, 2, 3, or 4): ")

        if role == "4":
            print("Exiting...")
            break

        # Set the role description for the selected role
        messages[0]['content'] = role_descriptions.get(role, role_descriptions["1"])

        print("\nSelect a model:")
        print("1. gpt-3.5-turbo")

        model = "1"

        model_mapping = {
            "1": "gpt-3.5-turbo",
        }

        if model not in model_mapping:
            print("Invalid model number. Please try again.")
            continue

        model_name = model_mapping[model]

        prompt = input("\nEnter your prompt: ")
        messages.append({"role": "user", "content": prompt})

        response = call_gpt_api(role, model_name, messages)
        messages.append({"role": "assistant", "content": response})
        
        print("\nGenerated response:")
        print(response)

if __name__ == "__main__":
    main()
