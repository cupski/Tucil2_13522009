import numpy as np
import matplotlib.pyplot as plt
import time

def QuadraticBezierCurve(P0, P1, P2, iterations):
    curve = []
    
    if iterations == 0:
        curve.extend([P0, P2])
    else:
        # Hitung titik kontrol baru
        Q0 = (P0 + P1) / 2
        Q1 = (P1 + P2) / 2
        R0 = (Q0 + Q1) / 2
        
        # Rekursi ke segmen kiri dan kanan
        left_curve = QuadraticBezierCurve(P0, Q0, R0, iterations - 1)
        right_curve = QuadraticBezierCurve(R0, Q1, P2, iterations - 1)
        
        # Gabungkan hasil dari kedua segmen
        curve = left_curve[:-1] + right_curve
    
    return curve

def plotBezierCurve(curve):
    x_curve, y_curve = zip(*curve)
    plt.plot(x_curve, y_curve, '-o')
    plt.title('Quadratic Bezier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

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
    iterations = int(input("Masukkan Jumlah Iterasi: "))

    start_time = time.time()
    curve = QuadraticBezierCurve(P0, P1, P2, iterations)
    end_time = time.time()

    # Output: Hasil kurva Bézier
    plotBezierCurve(curve)

    # Output: Waktu eksekusi program
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

if __name__ == "__main__":
    main()
