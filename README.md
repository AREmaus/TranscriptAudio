# TranscriptAudio
PTBR: Este sistema foi construído para acessibilidade auditiva. Construído em Python utilizando as bibliotecas VOSK e AudioPy<BR>
EN: This system was built for hearing accessibility. Built in Python using the VOSK and AudioPy libraries

<h2>Introdução</h2>

<p>Este repositório contém um script Python que utiliza a biblioteca Vosk e Pyaudio para reconhecer a fala em tempo real. O script é capaz de capturar áudio de um microfone e reconhecer a fala usando o modelo de idioma fornecido.</p>

<h2>Requisitos</h2>

<ul>
  <li>Python 3.x</li>
  <li>Biblioteca Vosk</li>
  <li>Biblioteca Pyaudio</li>
</ul>

<h2>Instalação</h2>

<ol>
  <li>Certifique-se de ter o Python 3.x instalado em sua máquina. Caso não tenha, você pode baixá-lo <a href="https://www.python.org/downloads/">aqui</a>.</li>
  <li>Instale a biblioteca Vosk executando o seguinte comando:</li>
</ol>

<pre><code>pip install vosk</code></pre>

<ol start="3">
  <li>Instale a biblioteca Pyaudio executando o seguinte comando:</li>
</ol>

<pre><code>pip install pyaudio</code></pre>

<h2>Uso</h2>

<ol>
  <li>Baixe o modelo de idioma necessário e salve-o em um diretório. Este modelo pode ser encontrado <a href="https://alphacephei.com/vosk/models">aqui</a>.</li>
  <li>Abra o script Python em um editor de código e atualize a variável <code>model_path</code> para o caminho onde você salvou o modelo de idioma.</li>
  <li>Execute o script Python:</li>
</ol>

<pre><code>python speech_recognition.py</code></pre>

<p>O script irá capturar áudio do microfone e imprimirá o texto reconhecido na tela.</p>

<h2>Observações</h2>

<ul>
  <li>Você pode alterar a taxa de amostragem e o tamanho do buffer para capturar áudio com maior precisão. No entanto, isso pode aumentar a carga de processamento do sistema.</li>
  <li>O script atual não lida com a interrupção do usuário. Para encerrar o script, você precisará interrompê-lo manualmente (por exemplo, pressionando Ctrl + C no terminal).</li>
</ul>
