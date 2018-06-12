import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy import signal
import wave
import sys
import scipy.io as sio
from pydub import AudioSegment

def _wav2array(nchannels, sampwidth, data):
    """data must be the string containing the bytes from the wav file."""
    num_samples, remainder = divmod(len(data), sampwidth * nchannels)
    if remainder > 0:
        raise ValueError('The length of data is not a multiple of '
                         'sampwidth * num_channels.')
    if sampwidth > 4:
        raise ValueError("sampwidth must not be greater than 4.")

    if sampwidth == 3:
        a = np.empty((num_samples, nchannels, 4), dtype=np.uint8)
        raw_bytes = np.fromstring(data, dtype=np.uint8)
        a[:, :, :sampwidth] = raw_bytes.reshape(-1, nchannels, sampwidth)
        a[:, :, sampwidth:] = (a[:, :, sampwidth - 1:sampwidth] >> 7) * 255
        result = a.view('<i4').reshape(a.shape[:-1])
    else:
        # 8 bit samples are stored as unsigned ints; others as signed ints.
        dt_char = 'u' if sampwidth == 1 else 'i'
        a = np.fromstring(data, dtype='<%s%d' % (dt_char, sampwidth))
        result = a.reshape(-1, nchannels)
    return result

def readwav(file):
    """
    Read a wav file.
    Returns the frame rate, sample width (in bytes) and a numpy array
    containing the data.
    This function does not read compressed wav files.
    """
    wav = wave.open(file)
    rate = wav.getframerate()
    nchannels = wav.getnchannels()
    sampwidth = wav.getsampwidth()
    nframes = wav.getnframes()
    data = wav.readframes(nframes)
    wav.close()
    array = _wav2array(nchannels, sampwidth, data)
    return rate, sampwidth, array


input ("Com a ajuda do cursor (observando do lado inferior direito da janela) observe o tempo (s) em que ocorre o disparo, em seguida feche a janela da plotagem.\n Pressione enter para iniciar\n")

rate, sampwidth, data = readwav("f8_espacial7mic_xm8500_tiro1-mic1.wav")

c = data;

c = c - np.mean(c);
c = c/max(abs(c));

#converte vetor n dimensional
tam = len(c);
vetc = np.zeros(tam);
for i in range (0,tam-1):
    vetc[i] = c[i][0]

#eixo x em segundos
x = np.zeros(tam)
for i in range (0,tam-1):
    x[i] = i/44100

plt.plot(x,vetc)
plt.title('Amostra 1')
plt.xlabel('tempo')
plt.show()

d = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com essa amostra \n 2)Fazer o median filtering\n"));
if d==1:

    e = int( input("Qual alternativa deseja escolher para as amostras após recortadas? \n 1)Não fazer o median filtering \n 2)Fazer o median filtering\n"));

    if e==1:

        print ("Processando...");

        #corta
        sound1 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic1.wav")
        sound2 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic2.wav")
        sound3 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic3.wav")
        sound4 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic4.wav")
        sound5 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic5.wav")
        sound6 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic6.wav")
        sound7 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic7.wav")

        e1 = float(input("Insira o centro do corte em segundos:"));
        a1 = 1000*e1 - 250;
        b1 = 1000*e1 + 250;

        sample1 = sound1[a1:b1]
        sample2 = sound2[a1:b1]
        sample3 = sound3[a1:b1]
        sample4 = sound4[a1:b1]
        sample5 = sound5[a1:b1]
        sample6 = sound6[a1:b1]
        sample7 = sound7[a1:b1]

        # create a new file "sclicefromAtoB.wav":
        sample1.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra1.wav", format="wav")
        sample2.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra2.wav", format="wav")
        sample3.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra3.wav", format="wav")
        sample4.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra4.wav", format="wav")
        sample5.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra5.wav", format="wav")
        sample6.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra6.wav", format="wav")
        sample7.export("C:/Users/Guilherme Moreira/Downloads/IC Python/1amostra7.wav", format="wav")

        #abre as novas amostras
        rate1, sampwidth1, data1 = readwav("1amostra1.wav")
        rate2, sampwidth2, data2 = readwav("1amostra2.wav")
        rate3, sampwidth3, data3 = readwav("1amostra3.wav")
        rate4, sampwidth4, data4 = readwav("1amostra4.wav")
        rate5, sampwidth5, data5 = readwav("1amostra5.wav")
        rate6, sampwidth6, data6 = readwav("1amostra6.wav")
        rate7, sampwidth7, data7 = readwav("1amostra7.wav")

        #armazena os dados nos vetores
        c1 = data1;
        c2 = data2;
        c3 = data3;
        c4 = data4;
        c5 = data5;
        c6 = data6;
        c7 = data7;


        #converte vetor n dimensional
        tam1 = len(c1);
        vetc1 = np.zeros(tam1);
        for i1 in range (0,tam1-1):
            vetc1[i1] = c1[i1][0]
        tam2 = len(c2);
        vetc2 = np.zeros(tam2);
        for i2 in range (0,tam2-1):
            vetc2[i2] = c2[i2][0]
        tam3 = len(c3);
        vetc3 = np.zeros(tam3);
        for i3 in range (0,tam3-1):
            vetc3[i3] = c3[i3][0]
        tam4 = len(c4);
        vetc4 = np.zeros(tam4);
        for i4 in range (0,tam4-1):
            vetc4[i4] = c4[i4][0]
        tam5 = len(c5);
        vetc5 = np.zeros(tam5);
        for i5 in range (0,tam5-1):
            vetc5[i5] = c5[i5][0]
        tam6 = len(c6);
        vetc6 = np.zeros(tam6);
        for i6 in range (0,tam6-1):
            vetc6[i6] = c6[i6][0]
        tam7 = len(c7);
        vetc7 = np.zeros(tam7);
        for i7 in range (0,tam7-1):
            vetc7[i7] = c7[i7][0]


        #eixo x em segundos
        x1 = np.zeros(tam1)
        for i in range (0,tam1-1):
            x1[i] = i/44100
        x2 = np.zeros(tam2)
        for i in range (0,tam2-1):
            x2[i] = i/44100
        x3 = np.zeros(tam3)
        for i in range (0,tam3-1):
            x3[i] = i/44100
        x4 = np.zeros(tam4)
        for i in range (0,tam4-1):
            x4[i] = i/44100
        x5 = np.zeros(tam5)
        for i in range (0,tam5-1):
            x5[i] = i/44100
        x6 = np.zeros(tam6)
        for i in range (0,tam6-1):
            x6[i] = i/44100
        x7 = np.zeros(tam7)
        for i in range (0,tam7-1):
            x7[i] = i/44100

        #plotagem
        plt.subplot(7,1,1)
        plt.plot(x1,vetc1)

        plt.subplot(7,1,2)
        plt.plot(x2,vetc2)

        plt.subplot(7,1,3)
        plt.plot(x3,vetc3)

        plt.subplot(7,1,4)
        plt.plot(x4,vetc4)

        plt.subplot(7,1,5)
        plt.plot(x5,vetc5)

        plt.subplot(7,1,6)
        plt.plot(x6,vetc6)

        plt.subplot(7,1,7)
        plt.plot(x7,vetc7)


        plt.show()

    elif e==2:

        print ("Processando...");

        #corta
        sound1 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic1.wav")
        sound2 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic2.wav")
        sound3 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic3.wav")
        sound4 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic4.wav")
        sound5 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic5.wav")
        sound6 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic6.wav")
        sound7 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic7.wav")

        e1 = float(input("Insira o centro do corte em segundos:"));
        a1 = 1000*e1 - 250;
        b1 = 1000*e1 + 250;

        sample1 = sound1[a1:b1]
        sample2 = sound2[a1:b1]
        sample3 = sound3[a1:b1]
        sample4 = sound4[a1:b1]
        sample5 = sound5[a1:b1]
        sample6 = sound6[a1:b1]
        sample7 = sound7[a1:b1]

        # create a new file "sclicefromAtoB.wav":
        sample1.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra1.wav", format="wav")
        sample2.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra2.wav", format="wav")
        sample3.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra3.wav", format="wav")
        sample4.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra4.wav", format="wav")
        sample5.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra5.wav", format="wav")
        sample6.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra6.wav", format="wav")
        sample7.export("C:/Users/Guilherme Moreira/Downloads/IC Python/2amostra7.wav", format="wav")

        #abre as novas amostras
        rate1, sampwidth1, data1 = readwav("2amostra1.wav")
        rate2, sampwidth2, data2 = readwav("2amostra2.wav")
        rate3, sampwidth3, data3 = readwav("2amostra3.wav")
        rate4, sampwidth4, data4 = readwav("2amostra4.wav")
        rate5, sampwidth5, data5 = readwav("2amostra5.wav")
        rate6, sampwidth6, data6 = readwav("2amostra6.wav")
        rate7, sampwidth7, data7 = readwav("2amostra7.wav")

        #armazena os dados nos vetores
        c1 = data1;
        c2 = data2;
        c3 = data3;
        c4 = data4;
        c5 = data5;
        c6 = data6;
        c7 = data7;


        #converte vetor n dimensional
        tam1 = len(c1);
        vetc1 = np.zeros(tam1);
        for i1 in range (0,tam1-1):
            vetc1[i1] = c1[i1][0]
        tam2 = len(c2);
        vetc2 = np.zeros(tam2);
        for i2 in range (0,tam2-1):
            vetc2[i2] = c2[i2][0]
        tam3 = len(c3);
        vetc3 = np.zeros(tam3);
        for i3 in range (0,tam3-1):
            vetc3[i3] = c3[i3][0]
        tam4 = len(c4);
        vetc4 = np.zeros(tam4);
        for i4 in range (0,tam4-1):
            vetc4[i4] = c4[i4][0]
        tam5 = len(c5);
        vetc5 = np.zeros(tam5);
        for i5 in range (0,tam5-1):
            vetc5[i5] = c5[i5][0]
        tam6 = len(c6);
        vetc6 = np.zeros(tam6);
        for i6 in range (0,tam6-1):
            vetc6[i6] = c6[i6][0]
        tam7 = len(c7);
        vetc7 = np.zeros(tam7);
        for i7 in range (0,tam7-1):
            vetc7[i7] = c7[i7][0]


        #eixo x em segundos
        x1 = np.zeros(tam1)
        for i in range (0,tam1-1):
            x1[i] = i/44100
        x2 = np.zeros(tam2)
        for i in range (0,tam2-1):
            x2[i] = i/44100
        x3 = np.zeros(tam3)
        for i in range (0,tam3-1):
            x3[i] = i/44100
        x4 = np.zeros(tam4)
        for i in range (0,tam4-1):
            x4[i] = i/44100
        x5 = np.zeros(tam5)
        for i in range (0,tam5-1):
            x5[i] = i/44100
        x6 = np.zeros(tam6)
        for i in range (0,tam6-1):
            x6[i] = i/44100
        x7 = np.zeros(tam7)
        for i in range (0,tam7-1):
            x7[i] = i/44100

        #medianfiltering
        d1 = vetc1 - sp.signal.medfilt(vetc1);
        d2 = vetc2 - sp.signal.medfilt(vetc2);
        d3 = vetc3 - sp.signal.medfilt(vetc3);
        d4 = vetc4 - sp.signal.medfilt(vetc4);
        d5 = vetc5 - sp.signal.medfilt(vetc5);
        d6 = vetc6 - sp.signal.medfilt(vetc6);
        d7 = vetc7 - sp.signal.medfilt(vetc7);


        #plotagem
        plt.subplot(7,1,1)
        plt.plot(x1,d1)

        plt.subplot(7,1,2)
        plt.plot(x2,d2)

        plt.subplot(7,1,3)
        plt.plot(x3,d3)

        plt.subplot(7,1,4)
        plt.plot(x4,d4)

        plt.subplot(7,1,5)
        plt.plot(x5,d5)

        plt.subplot(7,1,6)
        plt.plot(x6,d6)

        plt.subplot(7,1,7)
        plt.plot(x7,d7)

        plt.show()

elif d==2:

    print ("Processando...");
    rate1, sampwidth1, data1 = readwav("f8_espacial7mic_xm8500_tiro1-mic1.wav")
    rate2, sampwidth2, data2 = readwav("f8_espacial7mic_xm8500_tiro1-mic2.wav")
    rate3, sampwidth3, data3 = readwav("f8_espacial7mic_xm8500_tiro1-mic3.wav")
    rate4, sampwidth4, data4 = readwav("f8_espacial7mic_xm8500_tiro1-mic4.wav")
    rate5, sampwidth5, data5 = readwav("f8_espacial7mic_xm8500_tiro1-mic5.wav")
    rate6, sampwidth6, data6 = readwav("f8_espacial7mic_xm8500_tiro1-mic6.wav")
    rate7, sampwidth7, data7 = readwav("f8_espacial7mic_xm8500_tiro1-mic7.wav")

    #armazena os dados nos vetores
    c1 = data1;
    c2 = data2;
    c3 = data3;
    c4 = data4;
    c5 = data5;
    c6 = data6;
    c7 = data7;

    #normaliza
    c1 = c1 - np.mean(c1);
    c1 = c1/max(abs(c1));
    c2 = c2 - np.mean(c2);
    c2 = c2/max(abs(c2));
    c3 = c3 - np.mean(c3);
    c3 = c3/max(abs(c3));
    c4 = c4 - np.mean(c4);
    c4 = c4/max(abs(c4));
    c5 = c5 - np.mean(c5);
    c5 = c5/max(abs(c5));
    c6 = c6 - np.mean(c6);
    c6 = c6/max(abs(c6));
    c7 = c7 - np.mean(c7);
    c7 = c7/max(abs(c7));


    #converte vetor n dimensional
    tam1 = len(c1);
    vetc1 = np.zeros(tam1);
    for i1 in range (0,tam1-1):
        vetc1[i1] = c1[i1][0]
    tam2 = len(c2);
    vetc2 = np.zeros(tam2);
    for i2 in range (0,tam2-1):
        vetc2[i2] = c2[i2][0]
    tam3 = len(c3);
    vetc3 = np.zeros(tam3);
    for i3 in range (0,tam3-1):
        vetc3[i3] = c3[i3][0]
    tam4 = len(c4);
    vetc4 = np.zeros(tam4);
    for i4 in range (0,tam4-1):
        vetc4[i4] = c4[i4][0]
    tam5 = len(c5);
    vetc5 = np.zeros(tam5);
    for i5 in range (0,tam5-1):
        vetc5[i5] = c5[i5][0]
    tam6 = len(c6);
    vetc6 = np.zeros(tam6);
    for i6 in range (0,tam6-1):
        vetc6[i6] = c6[i6][0]
    tam7 = len(c7);
    vetc7 = np.zeros(tam7);
    for i7 in range (0,tam7-1):
        vetc7[i7] = c7[i7][0]


    #eixo x em segundos
    x1 = np.zeros(tam1)
    for i in range (0,tam1-1):
        x1[i] = i/44100
    x2 = np.zeros(tam2)
    for i in range (0,tam2-1):
        x2[i] = i/44100
    x3 = np.zeros(tam3)
    for i in range (0,tam3-1):
        x3[i] = i/44100
    x4 = np.zeros(tam4)
    for i in range (0,tam4-1):
        x4[i] = i/44100
    x5 = np.zeros(tam5)
    for i in range (0,tam5-1):
        x5[i] = i/44100
    x6 = np.zeros(tam6)
    for i in range (0,tam6-1):
        x6[i] = i/44100
    x7 = np.zeros(tam7)
    for i in range (0,tam7-1):
        x7[i] = i/44100


    #medianfiltering
    d1 = vetc1 - sp.signal.medfilt(vetc1);
    d2 = vetc2 - sp.signal.medfilt(vetc2);
    d3 = vetc3 - sp.signal.medfilt(vetc3);
    d4 = vetc4 - sp.signal.medfilt(vetc4);
    d5 = vetc5 - sp.signal.medfilt(vetc5);
    d6 = vetc6 - sp.signal.medfilt(vetc6);
    d7 = vetc7 - sp.signal.medfilt(vetc7);


    #plotagem
    #plt.subplot(5,1,1)
    plt.plot(x1,d1)

    plt.show()
    
    e1 = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com o ponto de corte \n 2)Visualizar próximo sinal\n"));

    if e1!=1: 
        #plt.subplot(5,1,2)
        plt.plot(x2,d2)
        plt.show()

        e1 = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com o ponto de corte \n 2)Visualizar próximo sinal\n"));

        if e1!=1:
            #plt.subplot(5,1,3)
            plt.plot(x3,d3)
            plt.show()
            e1 = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com o ponto de corte \n 2)Visualizar próximo sinal\n"));

            if e1!=1:
                #plt.subplot(5,1,4)
                plt.plot(x4,d4)
                plt.show()
                e1 = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com o ponto de corte \n 2)Visualizar próximo sinal\n"));

                if e1!=1:
                    #plt.subplot(5,1,5)
                    plt.plot(x5,d5)
                    plt.show()
                    e1 = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com o ponto de corte \n 2)Visualizar próximo sinal\n"));

                    if e1!=1:
                        #plt.subplot(6,1,6)
                        plt.plot(x6,d6)
                        plt.show()
                        e1 = int( input("Qual alternativa deseja escolher? \n 1)Prosseguir com o ponto de corte \n 2)Visualizar próximo sinal\n"));

                        if e1!=1:
                            #plt.subplot(7,1,7)
                            plt.plot(x7,d7)

                            plt.show()


    if e1==1:
        print("Arguarde alguns instantes");

        #corta
        sound1 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic1.wav")
        sound2 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic2.wav")
        sound3 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic3.wav")
        sound4 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic4.wav")
        sound5 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic5.wav")
        sound6 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic6.wav")
        sound7 = AudioSegment.from_file("f8_espacial7mic_xm8500_tiro1-mic7.wav")

        e1 = float(input("Insira o centro do corte em segundos:"));
        a1 = 1000*e1 - 250;
        b1 = 1000*e1 + 250;

        sample1 = sound1[a1:b1]
        sample2 = sound2[a1:b1]
        sample3 = sound3[a1:b1]
        sample4 = sound4[a1:b1]
        sample5 = sound5[a1:b1]
        sample6 = sound6[a1:b1]
        sample7 = sound7[a1:b1]

        # create a new file "sclicefromAtoB.wav":
        sample1.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra1.wav", format="wav")
        sample2.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra2.wav", format="wav")
        sample3.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra3.wav", format="wav")
        sample4.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra4.wav", format="wav")
        sample5.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra5.wav", format="wav")
        sample6.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra6.wav", format="wav")
        sample7.export("C:/Users/Guilherme Moreira/Downloads/IC Python/amostra7.wav", format="wav")

        #abre as novas amostras
        rate1, sampwidth1, data1 = readwav("amostra1.wav")
        rate2, sampwidth2, data2 = readwav("amostra2.wav")
        rate3, sampwidth3, data3 = readwav("amostra3.wav")
        rate4, sampwidth4, data4 = readwav("amostra4.wav")
        rate5, sampwidth5, data5 = readwav("amostra5.wav")
        rate6, sampwidth6, data6 = readwav("amostra6.wav")
        rate7, sampwidth7, data7 = readwav("amostra7.wav")

        #armazena os dados nos vetores
        c1 = data1;
        c2 = data2;
        c3 = data3;
        c4 = data4;
        c5 = data5;
        c6 = data6;
        c7 = data7;


        #converte vetor n dimensional
        tam1 = len(c1);
        vetc1 = np.zeros(tam1);
        for i1 in range (0,tam1-1):
            vetc1[i1] = c1[i1][0]
        tam2 = len(c2);
        vetc2 = np.zeros(tam2);
        for i2 in range (0,tam2-1):
            vetc2[i2] = c2[i2][0]
        tam3 = len(c3);
        vetc3 = np.zeros(tam3);
        for i3 in range (0,tam3-1):
            vetc3[i3] = c3[i3][0]
        tam4 = len(c4);
        vetc4 = np.zeros(tam4);
        for i4 in range (0,tam4-1):
            vetc4[i4] = c4[i4][0]
        tam5 = len(c5);
        vetc5 = np.zeros(tam5);
        for i5 in range (0,tam5-1):
            vetc5[i5] = c5[i5][0]
        tam6 = len(c6);
        vetc6 = np.zeros(tam6);
        for i6 in range (0,tam6-1):
            vetc6[i6] = c6[i6][0]
        tam7 = len(c7);
        vetc7 = np.zeros(tam7);
        for i7 in range (0,tam7-1):
            vetc7[i7] = c7[i7][0]


        #eixo x em segundos
        x1 = np.zeros(tam1)
        for i in range (0,tam1-1):
            x1[i] = i/44100
        x2 = np.zeros(tam2)
        for i in range (0,tam2-1):
            x2[i] = i/44100
        x3 = np.zeros(tam3)
        for i in range (0,tam3-1):
            x3[i] = i/44100
        x4 = np.zeros(tam4)
        for i in range (0,tam4-1):
            x4[i] = i/44100
        x5 = np.zeros(tam5)
        for i in range (0,tam5-1):
            x5[i] = i/44100
        x6 = np.zeros(tam6)
        for i in range (0,tam6-1):
            x6[i] = i/44100
        x7 = np.zeros(tam7)
        for i in range (0,tam7-1):
            x7[i] = i/44100

        #plotagem
        plt.subplot(7,1,1)
        plt.plot(x1,vetc1)

        plt.subplot(7,1,2)
        plt.plot(x2,vetc2)

        plt.subplot(7,1,3)
        plt.plot(x3,vetc3)

        plt.subplot(7,1,4)
        plt.plot(x4,vetc4)

        plt.subplot(7,1,5)
        plt.plot(x5,vetc5)

        plt.subplot(7,1,6)
        plt.plot(x6,vetc6)

        plt.subplot(7,1,7)
        plt.plot(x7,vetc7)


        plt.show()

    
