import matplotlib.pyplot as plt

def plot(t):
    buff = []
    f1 = open("result.txt", "r")

    for a in f1:
        buff.append(a.rstrip('\n'))
    x=[1,2, 3]
    y=[buff[0], buff[1], buff[2]]
    LABELS = ["Positif: "+str(buff[0])+"%", "Negatif: "+str(buff[1])+"%", "Tidak Pasti/Neutral: "+str(buff[2])+"%"]

    plt.bar(x,y,label="Carta Bar", color='r')
    plt.xticks(x, LABELS)

    plt.xlabel("Sentimen")
    plt.ylabel("Peratusan (%)")
    plt.title("Sentimen Untuk Kata Kunci: "+t)

    plt.show()
#plot()