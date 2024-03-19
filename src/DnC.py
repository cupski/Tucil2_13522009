import numpy as np
import time

class DnC:
    def __init__(self, P0, P1, P2, iterations):
        self.P0 = P0
        self.P1 = P1
        self.P2 = P2
        self.iterations = iterations
        self.curves = []

    def midpoint(self, Px, Py):
        return (((Px[0] + Py[0]) / 2), ((Px[1] + Py[1]) / 2))

    def QuadraticBezierCurve(self, P0, P1, P2, iterations):
        curve = []  # Inisialisasi larik untuk menyimpan titik-titik kurva

        # Kasus dasar: iterasi = 0, Basis rekursi
        if iterations == 0:
            curve.extend([P0, P2])
        else:
            # Hitung titik kontrol baru
            Midpoint1 = self.midpoint(P0,P1)  # Titik tengah antara P0 dan P1
            Midpoint2 = self.midpoint(P1, P2)  # Titik tengah antara P1 dan P2
            Midpoint_1_and_2 = self.midpoint(Midpoint1, Midpoint2)  # Titik tengah antara Q0 dan Q1

            # Rekursi ke segmen kiri dan kanan(Divide and Conquer)
            # Segmen kiri: dari P0 ke R0
            left_curve = self.QuadraticBezierCurve(P0, Midpoint1, Midpoint_1_and_2, iterations - 1)
            # Segmen kanan: dari R0 ke P2
            right_curve = self.QuadraticBezierCurve(Midpoint_1_and_2, Midpoint2, P2, iterations - 1)

            # Gabungkan hasil dari kedua segmen(Combine)
            curve = left_curve[:-1] + right_curve  # Hilangkan satu titik R0 yang berlebih

        return curve  # Kembalikan larik titik-titik kurva


    def generate_curves(self):
        end_time = 0
        start_time = 0
        for i in range(self.iterations):
            if(i == self.iterations-1):
                start_time = time.time()
                curve = self.QuadraticBezierCurve(self.P0, self.P1, self.P2, i+1)
                end_time = time.time()
            else:
                curve = self.QuadraticBezierCurve(self.P0, self.P1, self.P2, i+1)

            self.curves.append(curve)
            execution_time = (end_time - start_time) * 1000
        return self.curves, execution_time
