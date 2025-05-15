import numpy as np

def recu_solution(f, b, a):

    if len(b) > len(a):
        raise ValueError("Length of b greater than length of a")

    zero = np.zeros(len(a)-len(b), dtype=float)
    b = np.append(zero,b)
    y = np.zeros_like(f)

    tempa = a#[1:]
    # tempa = np.append(0, tempa)
    paddedf = np.append(np.zeros(len(a)-1), f)
    paddedy = np.append(np.zeros(20),y)
    b = b[::-1]
    tempa = tempa[::-1]

    for k in range(0, len(f)):
        suma = np.sum(tempa * paddedy[k+1:k+len(a)+1])
        sumb = np.sum(b * paddedf[k:k+len(b)])
        paddedy[k+len(a)] = sumb - suma

    return paddedy[len(b):len(f)+len(b)]

def find_impulse_response (b, a, N):

    if len(b) > len(a):
        raise ValueError("Length of b greater than length of a")

    return [0]

def frequency_response(b, a, N=1000):

    if len(b) > len(a):
        raise ValueError("Length of b greater than length of a")

    return [0], [0]

def main():
    a = np.array([1.0, 4.0, 6.0])
    b = np.array([6.0,1.0])
    f = np.array([1.0,3.0,2.0,4.0, 7.0, 9.0])
    y = recu_solution(f,b,a)
    # print(y)



if __name__ == "__main__":
    main()