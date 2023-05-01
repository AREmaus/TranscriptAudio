import vosk
import pyaudio

# Carrega o modelo de idioma
#model_path = "C:/Users/Andre/Downloads/vosk-model-pt-fb-v0.1.1-20220516_2113/vosk-model-pt-fb-v0.1.1-20220516_2113"
model_path = 'C:/Users/Andre/Desktop/bibliotecas/modelsmall'

model = vosk.Model(model_path)

# Reconhecedor de fala
rec = vosk.KaldiRecognizer(model, 16000)

# Captura de audio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

# Loop principal para capturar e reconhecer a fala em tempo real
while True:
    # Leitura do audio
    data = stream.read(8000)

    # Reconhecimento para VOSK
    if rec.AcceptWaveform(data):
        # Saida do texto reconhecido
        print(rec.Result())

# Finalizacao complementar disponivel (fora do loop)
result = rec.FinalResult()
print(result)
