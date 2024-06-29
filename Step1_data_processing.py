from viphoneme import vi2IPA_split
import tqdm, glob
import sys
from pydub import AudioSegment

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def TTSnorm(text):
    # Ví dụ về cách ghi tệp với mã hóa utf-8
    with open('temporary_file.txt', 'w', encoding='utf-8') as fw:
        fw.write(text)
    return text  # Giả sử TTSnorm trả về chuỗi đã xử lý

def vi2IPA_split(text, delimiter):
    # Sử dụng TTSnorm đã được tùy chỉnh
    TN = TTSnorm(text)
    # Trả về kết quả của bạn ở đây (ví dụ)
    return TN

def process_text():
    # Đọc và xử lý tệp train.txt
    with open("DATA/train.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    norm_lines = []
    for line in tqdm.tqdm(lines):
        file, script = line.split(" ", 1)
        if not file.endswith(".wav"):
            file = file + ".wav"
        phoneme = vi2IPA_split(script.lower(), "/")
        if phoneme is None or len(phoneme.split(" ")) < 4:
            continue
        norm_lines.append(file + "|" + file.replace("/wavs", "/embedding").replace(".wav", ".npy") + "|" + phoneme)

    with open("DATA/train.txt", "w", encoding="utf-8") as file:
        for item in norm_lines:
            file.write(item + "\n")

    # Đọc và xử lý tệp val.txt
    with open("DATA/val.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    norm_lines = []
    for line in tqdm.tqdm(lines):
        file, script = line.split(" ", 1)
        if not file.endswith(".wav"):
            file = file + ".wav"
        phoneme = vi2IPA_split(script.lower(), "/")
        if phoneme is None or len(phoneme.split(" ")) < 4:
            continue
        norm_lines.append(file + "|" + file.replace("/wavs", "/embedding").replace(".wav", ".npy") + "|" + phoneme)

    with open("DATA/val.txt", "w", encoding="utf-8") as file:
        for item in norm_lines:
            file.write(item + "\n")

def process_speech():

     wavs = glob.glob("DATA/wavs/*.wav")
     for wav_file in tqdm.tqdm(wavs):
          audio = AudioSegment.from_file(wav_file)

          if audio.channels == 2:
               # Convert stereo audio to mono
               audio = audio.set_channels(1)

          if audio.frame_rate != 22050:
               # Convert the audio to 22050 Hz sample rate
               audio = audio.set_frame_rate(22050)

          audio.export(wav_file, format="wav")

if __name__ == "__main__":
     process_text()
     process_speech()
