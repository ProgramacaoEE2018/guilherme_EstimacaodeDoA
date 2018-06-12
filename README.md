# guilherme_EstimacaodeDoA

## Descriçao
A base deste vem do projeto que tenho desenvolvido na iniciação científica, com o professor Apolinário. A motivação vem de um projeto maior, que foi uma demanda da Emgepron, consistindo na estimação da direção de chegada (ou DoA, direction of arrival) de tiros a partir de amostras de áudio coletadas por um arranjo espacial de microfones. A proposta seria um programa em Python que lê arquivos de áudio (cada arquivo referente a um tiro), aplica o median filter  (ou não, ficando a critério do usuário) e recorta o intervalo de interesse (o que contém o disparo). Esse programa facilita as medições das diferenças de tempo entre as amostras para, depois de alguns recursos matemáticos envolvendo FFT (Fast Fourier Transform) e método dos mínimos quadrados, poder determinar a  DoA.

## Documentação

### Diagrama de Classes

### Fluxograma
![Fluxograma](Fluxograma.pdf)

### Tutorial Tkinter
O tutorial escolhido encontra-se no Youtube e refere-se à interface gráfica padrão do Python, o **Tkinter**. Link para acesso: https://www.youtube.com/watch?v=_lSNIrR1nZU&t=970s

![Tutorial GUI](GUItutorial.png)

### Esboço GUI
![Esboço GUI](GUI.png)

### Instalação e funcionamento

#### Instalando o Python
Primeiramente entre no site https://www.python.org/ , clique em Downloads e baixe a versão 3.6 (32 bit). Depois de feito o download, siga a sequência proposta, ao começar a instalação:
Customize Installation -> Deixar somente C:\Python36-32 (para facilitar quando for usar o prompt de comando)

#### Instalando as bibliotecas necessárias (Matplotlib, Scipy e FFmpeg)
Uma vez instalado, execute o prompt de comando como administrador (essa opção aparece ao se clicar com o botão direito do mause no app cmd). Em seguida execute os seguintes comandos para instalar Matplotlib e Scipy:
cd.. -> cd.. -> cd Python36-32 -> cd Scripts -> dir/w -> pip install matplotlib -> pip install scipy

