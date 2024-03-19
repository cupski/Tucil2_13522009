import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from DnC import DnC
from BruteForce import BruteForce

def update(frame, curves, P0, P1, P2):
    plt.cla()  # Hapus gambar sebelumnya
    iteration_curve = curves[frame]
    x_curve, y_curve = zip(*iteration_curve)
    
    # Gambar garis yang menghubungkan titik awal
    plt.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], 'k--')
    
    # Gambar kurva Bézier
    plt.plot(x_curve, y_curve, '-o')
    
    plt.title('Quadratic Bezier Curve (Iteration {})'.format(frame+1))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)


def main():
    print("Welcome to Kurver Berzier Generator")
    print("----------Pilih Metode Input----------")
    print("1.Divide and Conquer")
    print("2.Brute Force")

    menu = int(input("Pilihan Menu : "))
        
    while (menu < 1 or menu > 2):
        print("\nMasukan Tidak Valid")
        menu = int(input("Pilihan Menu : "))

    P0_input = input("Masukkan titik P0 (contoh: 2,3): ")
    _x, _y = P0_input.split(',')
    P0 = np.array([float(_x.strip()), float(_y.strip())])

    P1_input = input("Masukkan titik P1 (contoh: 2,3): ")
    _x, _y = P1_input.split(',')
    P1 = np.array([float(_x.strip()), float(_y.strip())])

    P2_input = input("Masukkan titik P2 (contoh: 2,3): ")
    _x, _y = P2_input.split(',')
    P2 = np.array([float(_x.strip()), float(_y.strip())])

    iterations = int(input("Masukkan Jumlah iterasi: "))
    while(iterations < 1):
        print("Iterasi harus lebih dari sama dngan 1\n")
        iterations = int(input("Masukkan Jumlah iterasi: "))

    
    if menu == 1:
        algorithm = DnC(P0, P1, P2, iterations)
    else:
        algorithm = BruteForce(P0, P1, P2, iterations)


    curves, execution_time = algorithm.generate_curves()


    print("Execution time : {:.8f} milliseconds".format(execution_time))

    fig = plt.figure()
    ani = FuncAnimation(fig, update, fargs=(curves,P0,P1,P2), frames=range(iterations), repeat=False, blit=False)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
