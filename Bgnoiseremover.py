import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio(audio_file, output_folder):
    # Check if the audio file exists
    if not os.path.exists(audio_file):
        print(f"Audio file '{audio_file}' not found.")
        return
    
    # Specify the path to ffmpeg
    ffmpeg_path = r"C:\path\to\ffmpeg.exe"  # Replace with the path to ffmpeg executable
    
    # Set the path to ffmpeg for pydub
    AudioSegment.converter = ffmpeg_path

    audio = AudioSegment.from_file(audio_file)

    # Split the audio on silence intervals
    segments = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Export each segment as a separate MP3 file
    for i, segment in enumerate(segments):
        output_file = os.path.join(output_folder, f"segment_{i}.mp3")
        segment.export(output_file, format="mp3")

# Example usage
audio_file = r"D:\RIISE_audio.wav"  # Replace with the full path to your audio file
output_folder = r"D:\Output Folder"  # Replace with the full path to your output folder
split_audio(audio_file, output_folder)
