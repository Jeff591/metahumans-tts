import torch
import argparse
from TTS.api import TTS

def main(text, speaker):
    # Check if CUDA is installed
    if torch.cuda.is_available():
        print("CUDA installed successfully\n") 
    else:
        print("CUDA not properly installed. Stopping process...")
        quit()

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model_choice = speaker

    if (model_choice == "Biran") :
        tts = TTS(model_path="./metahuman-models/Biran/checkpoint_254000.pth", config_path="./metahuman-models/Biran/config.json", progress_bar=True).to(device)
    if (model_choice == "Gandhi") :
        tts = TTS(model_path="./metahumans-tts/metahuman-models/Gandhi/checkpoint_1693000.pth", config_path="./metahumans-tts/metahuman-models/Gandhi/config.json", progress_bar=True).to(device)

    tts.tts_to_file(text= text, file_path="./metahumans-tts/outputaudio/output.wav")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text-to-Speech Generation")
    parser.add_argument("text", type=str, help="Text to be converted to speech")
    parser.add_argument("speaker", type=str, help="Who is speaking")
    args = parser.parse_args()

    main(args.text, args.speaker)