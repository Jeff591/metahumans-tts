import torch
from TTS.api import TTS

# Check if CUDA is installed
if torch.cuda.is_available():
    print("CUDA installed successfully\n") 
else:
    print("CUDA not properly installed. Stopping process...")
    quit()

device = "cuda" if torch.cuda.is_available() else "cpu"

model_choice = input("Which model? Biran or Gandhi: \n")

if (model_choice == "Biran") :
    tts = TTS(model_path="./metahuman-models/Biran/checkpoint_254000.pth", config_path="./metahuman-models/Biran/config.json", progress_bar=True).to(device)
if (model_choice == "Gandhi") :
    tts = TTS(model_path="./metahuman-models/Gandhi/checkpoint_1693000.pth", config_path="./metahuman-models/Gandhi/config.json", progress_bar=True).to(device)

tts.tts_to_file(text="This is a voice cloning test", file_path="./outputaudio/output.wav")