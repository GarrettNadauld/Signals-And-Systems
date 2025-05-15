import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

def sinusoid(T, k, f_0, f_s, A=1, p=0):
    x_k = A*np.sin(2*np.pi*k*(f_0/f_s) + p)
    # plt.plot(x, x_k)
    # plt.show()
    return x_k

def chirp(u, t, f_1, f_s, A=1, p=0):
    c_t = A * np.cos(np.pi*u*(t/f_s)**2 + 2*np.pi*f_1 + p)

    return c_t

def main():
    f_s = 8000
    f_0 = [300, 500, 700, 900] #7700, 7500, 7300, 7100]
    T = 1/f_s
    k = np.arange(0, 80)
    x_k = np.zeros((8, int(f_s*10E-3)))
    A = 1

    for n in range(len(f_0)):
        x_k[n] = sinusoid(T, k, f_0[n], f_s)

    plt.stem(k, x_k[0], label='Sampled Data')
    plt.title('Sampled Sinusoid at 300 Hz')
    plt.xlabel('Sample Number')
    plt.ylabel('x(kt)')
    # plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Sampled Data at Varying Frequencies')
    # fig, axs.set_title('x(kt) at varying f_0')

    axs[0, 0].stem(k, x_k[0], label='Sampled Data')
    axs[0, 0].set_title('300 Hz')
    axs[0, 0].set_xlabel('Sample')
    axs[0, 0].set_ylabel('x(kt)')
    #line0, = axs[0, 0].plot(k, x_k[0], label='Sampled Data')
    # axs[0, 0].legend(loc='upper right')
    axs[0, 0].grid(True)

    # Similarly, set labels and titles for the other subplots
    axs[0, 1].stem(k, x_k[1], label='Sampled Data')
    axs[0, 1].set_title('500 Hz')
    axs[0, 1].set_xlabel('Sample')
    axs[0, 1].set_ylabel('x(kt)')
    # line1, = axs[0, 1].plot(k, x_k[1], label='Sampled Data')
    # axs[0, 1].legend(loc='upper right')
    axs[0, 1].grid(True)

    axs[1, 0].stem(k, x_k[2], label='Sampled Data')
    axs[1, 0].set_title('700 Hz')
    axs[1, 0].set_xlabel('Sample')
    axs[1, 0].set_ylabel('x(kt)')
    # line2, = axs[1, 0].plot(k, x_k[2], label='Sampled Data')
    # axs[1, 0].legend(loc='upper right')
    axs[1, 0].grid(True)

    axs[1, 1].stem(k, x_k[3], label='Sampled Data')
    axs[1, 1].set_title('900 Hz')
    axs[1, 1].set_xlabel('Sample')
    axs[1, 1].set_ylabel('x(kt)')
    # line3, = axs[1, 1].plot(k, x_k[3], label='Sampled Data')
    # axs[1, 1].legend(loc='upper right')
    axs[1, 1].grid(True)

    plt.tight_layout()  # Adjust subplot spacing
    plt.show()

    sps = 8000  # Samples per second, should match your f_s
    duration_s = 2.0  # 10 ms
    f_s = 8000
    f_0 = [300, 500, 700, 900, 7700, 7500, 7300, 7100]
    T = 2
    k = np.arange(0, int(f_s*T))
    x_k = np.zeros((8, int(f_s * T)))
    A = 0.3

    for n in range(len(f_0)):
        x_k[n] = sinusoid(T, k, f_0[n], f_s)
    for n in range(len(f_0)):
        waveform = x_k[n] * A
        sd.play(waveform, f_s)
        time.sleep(duration_s)
        sd.stop()

    waveform = np.hstack((x_k[0], x_k[1], x_k[2], x_k[3]))
    sd.play(waveform,f_s)
    time.sleep(duration_s)
    sd.stop()

    waveform = np.hstack((x_k[4], x_k[5], x_k[6], x_k[7]))
    sd.play(waveform, f_s)
    time.sleep(duration_s)
    sd.stop()

    #new f_0
    # f_0 = [7700, 7500, 7300, 7100]

    #chirp
    f_1 = 100
    u = 2000
    f_s = [32000, 16000, 8000]
    T = 8

    fig, axs = plt.subplots(3, 1)
    fig.suptitle('Chirp Signal at Varying Sample Frequencies')

    for n in range(0, len(f_s)):
        t = np.arange(0, f_s[n]*T)
        c_t = chirp(u, t, f_1, f_s[n])
        axs[n].plot(t[:2000], c_t[:2000], label='Sampled Data')
        string = f"{f_s[n]} Hz"
        axs[n].set_title(string)
        axs[n].set_xlabel('Sample')
        axs[n].set_ylabel('Chirp Signal')
        # axs[n].legend(loc='upper right')
        axs[n].grid(True)

        waveform = c_t
        sd.play(waveform, f_s[n])
        time.sleep(duration_s)
        sd.stop()
    # plt.plot(t[:2000],c_t[:2000])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()