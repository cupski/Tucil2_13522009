import numpy as np
import time

class BruteForce:
    def __init__(self, P0, P1, P2, iterations):
        self.P0 = P0
        self.P1 = P1
        self.P2 = P2
        self.iterations = iterations
        self.curves = []

    def QuadraticBezierCurveBruteForce(self):
        # Inisialisasi daftar titik pada kurva
        curve = []
        
        # Hitung total titik yang akan dibuat
        iterations_new = self.total_dots(self.iterations)
        
        # Iterasi untuk menghasilkan titik pada kurva
        for i in range(iterations_new):
            # Hitung parameter t berdasarkan indeks iterasi
            t = i / (iterations_new - 1)
            
            # Hitung posisi titik pada kurva menggunakan rumus kurva Bézier
            curve.append((1 - t)**2 * self.P0 + 2 * (1 - t) * t * self.P1 + t**2 * self.P2)
        
        # Kembalikan daftar titik yang membentuk kurva Bézier
        return curve


    def total_dots(self, n):
        if n == 1:
            return 3
        else:
            return 2 * self.total_dots(n-1) - 1

    def generate_curves(self):
        end_time = 0
        start_time = 0
        for i in range(self.iterations):
            if(i == self.iterations-1):
                start_time = time.time()
                curve = self.QuadraticBezierCurveBruteForce()
                end_time = time.time()
            else:
                curve = self.QuadraticBezierCurveBruteForce()

            self.curves.append(curve)
            execution_time = (end_time - start_time) * 1000
        return self.curves, execution_time
