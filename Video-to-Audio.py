from moviepy.editor import VideoFileClip

def extract_audio(video_file, audio_file):
    # Load the video clip
    video_clip = VideoFileClip(video_file)

    # Extract audio
    audio_clip = video_clip.audio

    # Write audio to file
    audio_clip.write_audiofile(audio_file)

    # Close the video clip
    video_clip.close()

if __name__ == "__main__":
    video_file = r"D:\RIISE.mp4"  # Using raw string literal
    audio_file = r"D:\RIISE_audio.wav"  # Using raw string literal

    extract_audio(video_file, audio_file)  # Corrected function call

