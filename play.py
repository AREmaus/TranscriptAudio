import vosk
import pyaudio

# Modelo de idioma (para mais informações voce pode ler o arquivo readme no repositório)
#model_path = "C:/Users/Andre/Downloads/vosk-model-pt-fb-v0.1.1-20220516_2113/vosk-model-pt-fb-v0.1.1-20220516_2113"
model_path = 'C:/Users/Andre/Desktop/bibliotecas/modelsmall'

model = vosk.Model(model_path)

# Taxa de reconhecimento de fala 16kHz
# Voce pode tentar aumentar a taxa de reconhecimento (em vosk.KaldiRecognizer) para 44kHz ou superior. Se este for o caso, lembre-se de adequar a variável rate no parâmetro de audio.open (voce pode ver estes métodos nas linhas abaixo).
rec = vosk.KaldiRecognizer(model, 16000)

# Configuração para captura de audio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

# Loop para capturar e reconhecer a fala em tempo real
while True:
    # Buffer de leitura do audio
    data = stream.read(8000)

    # Entrada para VOSK realizar o processamento
    if rec.AcceptWaveform(data):
        # Saida do texto reconhecido
        print(rec.Result())

# Finalizacao complementar disponivel (fora do loop)
result = rec.FinalResult()
print(result)
