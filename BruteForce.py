import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def midpoint(Px, Py):
    return (((Px[0] + Py[0]) / 2), ((Px[1] + Py[1]) / 2))

def QuadraticBezierCurve(P0, P1, P2, iterations):
    curve = []
    for i in range(iterations + 1):
        t = i / iterations
        curve.append((1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2)
    return curve

def update(frame, curves):
    plt.cla()  #Hapus Gambar Sebelumnya
    iteration_curve = curves[frame]
    x_curve, y_curve = zip(*iteration_curve)
    plt.plot(x_curve, y_curve, '-o')
    plt.title('Quadratic Bezier Curve (Iteration {})'.format(frame+1))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

def main():
    # Input: Tiga pasang titik
    P0_input = input("Masukkan titik P0 (contoh: 2,3): ")
    _x, _y = P0_input.split(',')
    P0 = np.array([float(_x.strip()), float(_y.strip())])
    
    P1_input = input("Masukkan titik P1 (contoh: 2,3): ")
    _x, _y = P1_input.split(',')
    P1 = np.array([float(_x.strip()), float(_y.strip())])
    
    P2_input = input("Masukkan titik P2 (contoh: 2,3): ")
    _x, _y = P2_input.split(',')
    P2 = np.array([float(_x.strip()), float(_y.strip())])

    # Input: Jumlah iterasi
    iterations = int(input("Masukkan Jumlah iterasi: "))

    curves = []
    for i in range(iterations):
        curve = QuadraticBezierCurve(P0, P1, P2, i+1)
        curves.append(curve)

    fig = plt.figure()
    ani = FuncAnimation(fig, update, fargs=(curves,), frames=range(iterations), repeat=False)
    plt.show()

if __name__ == "__main__":
    main()
