import vosk
import pyaudio

# Modelo de idioma (para mais informações voce pode ler o arquivo readme no repositório)
#model_path = "C:/Users/Andre/Downloads/vosk-model-pt-fb-v0.1.1-20220516_2113/vosk-model-pt-fb-v0.1.1-20220516_2113"
model_path = 'C:/Users/Andre/Desktop/bibliotecas/modelsmall'

model = vosk.Model(model_path)
kHz = 16000
tamBuffer = 8000

# Taxa de reconhecimento de fala 16kHz
# Voce pode tentar aumentar a taxa de reconhecimento de 16kHz para 44kHz ou superior.
# Voce pode tentar diminuir o tamanho do buffer de 8k para 2,4k.
rec = vosk.KaldiRecognizer(model, kHz)

# Configuração para captura de audio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=kHz, input=True, frames_per_buffer=tamBuffer)

# Loop para capturar e reconhecer a fala em tempo real
while True:
    # Buffer de leitura do audio
    data = stream.read(tamBuffer)

    # Entrada para VOSK realizar o processamento
    if rec.AcceptWaveform(data):
        # Saida do texto reconhecido
        print(rec.Result())

# Finalizacao complementar disponivel (fora do loop)
result = rec.FinalResult()
print(result)
