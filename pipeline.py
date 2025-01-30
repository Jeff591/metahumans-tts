from ChatWithFinetune import ChatWithFinetune
import tkinter as tk
from tkinter import ttk
import subprocess

# Take the base model and add finetuned LoRA adapter weights on top of model to modify behavior
# We do not actually adjust the weights/parameters of the base model
model_id ="unsloth/llama-3-8b-Instruct-bnb-4bit"
system_prompt = "You are Gandhi, respond as him in first-person with his style of direct rhetoric. You are having a conversation with the user, and are humble and curious about them. If the user prompt indicates ther emotion with arousal, valence, and dominance values in the following format [a,v,d] on a scale of -1 to 1, do not mention these values but consider these values and respond empathetically."
adapter_path = "LLaMA-Factory\\llama3_lora_2"
llama3 = ChatWithFinetune(model_id, adapter_path, system_prompt)

def process_input():
    # Get input values from GUI
    prompt_text = text_input.get("1.0", tk.END).strip()
    prompt_emotion = [emotion1.get(),  emotion2.get(), emotion3.get()]
    legal_actions = [action for action, var in action_vars.items() if var.get()]

    # Create input string
    input_str = (
        f"=====prompt_text=====\n{prompt_text}\n"
        f"=====prompt_emotion=====\n{prompt_emotion}\n"
        f"=====legal_actions=====\n{legal_actions}\n"
    )

    # Display the input string
    input_display.delete("1.0", tk.END)
    input_display.insert(tk.END, input_str)
    
    return input_str

def parse_output(output_str):
    # Parse the output string
    lines = output_str.split("\n")
    result = []
    current_action = None

    for line in lines:
        if line.startswith("=====") and line.endswith("====="):
            # Extract the action name
            current_action = line.strip("=").strip()
            result.append(f"<{current_action}>")
        elif current_action == "speak" and line.strip():
            # Append the text following the 'speak' action
            result.append(line.strip())

    # Create the final parsed output
    parsed_output = " ".join(result)

    return parsed_output

def communicate_with_model():
    # Process input to get the formatted string
    prompt = process_input()

    # Send the prompt to the model and get the response
    response = llama3.talk_to_model(prompt)

    #

    # Display the input string
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, response)

    # Parse the model's response
    parsed_response = parse_output(response)

    # Display the parsed response
    response_display.delete("1.0", tk.END)
    response_display.insert(tk.END, parsed_response)

# Create the main window
root = tk.Tk()
root.title("Talk to Gandhi")

# Create input fields
ttk.Label(root, text="Prompt Text:").grid(row=0, column=0, sticky="w")
text_input = tk.Text(root, width=50, height=5)
text_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Prompt Emotion represents the emotion values associated with the real person inputting text
ttk.Label(root, text="Prompt Emotion:").grid(row=2, column=0, sticky="w")
emotion1 = tk.DoubleVar(value=0.0)
emotion2 = tk.DoubleVar(value=0.0)
emotion3 = tk.DoubleVar(value=0.0)
ttk.Entry(root, textvariable=emotion1, width=5).grid(row=3, column=0, sticky="w", padx=5)
ttk.Entry(root, textvariable=emotion2, width=5).grid(row=3, column=0, padx=5)
ttk.Entry(root, textvariable=emotion3, width=5).grid(row=3, column=0, sticky="e", padx=5)

# Define actions
actions = ['speak', 'shrug', 'crouch', 'jump', 'wink', 'bow', 'smile', 'nod']
action_vars = {action: tk.BooleanVar() for action in actions}
ttk.Label(root, text="Legal Actions:").grid(row=4, column=0, sticky="w")
for i, action in enumerate(actions):
    ttk.Checkbutton(root, text=action, variable=action_vars[action]).grid(row=5 + i // 2, column=i % 2, sticky="w", padx=5, pady=5)

# Button to communicate with the model
ttk.Button(root, text="Talk to Gandhi", command=communicate_with_model).grid(row=9, column=0, pady=10)

# Display processed input
ttk.Label(root, text="Processed Input:").grid(row=10, column=0, sticky="w")
input_display = tk.Text(root, width=50, height=5)
input_display.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

# Display unparsed output
ttk.Label(root, text="Unparsed Response:").grid(row=12, column=0, sticky="w")
output_display = tk.Text(root, width=50, height=5)
output_display.grid(row=13, column=0, columnspan=2, padx=5, pady=5)

# Display parsed output
ttk.Label(root, text="Response:").grid(row=14, column=0, sticky="w")
response_display = tk.Text(root, width=50, height=5)
response_display.grid(row=15, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()