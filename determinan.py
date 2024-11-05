# Fungsi untuk menghitung determinan matriks 2x2
def determinant_2x2(matrix):
    # Matriks 2x2: [[a, b], [c, d]]
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Fungsi untuk menghitung determinan matriks 3x3
def determinant_3x3(matrix):
    # Matriks 3x3: [[a, b, c], [d, e, f], [g, h, i]]
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    return (a * (e * i - f * h) -
            b * (d * i - f * g) +
            c * (d * h - e * g))

# Fungsi untuk menghitung determinan matriks 4x4 menggunakan ekspansi kofaktor
def determinant_4x4(matrix):
    def minor(matrix, row, col):
        """Menghapus baris dan kolom untuk membuat minor"""
        return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

    # Ekspansi kofaktor pada baris pertama
    return sum(matrix[0][j] * determinant_3x3(minor(matrix, 0, j)) * (-1 if j % 2 else 1) for j in range(4))

# Fungsi utama untuk memilih ukuran matriks dan menghitung determinan
def main():
    size = int(input("Masukkan ukuran matriks (2, 3, atau 4): "))
    
    # Meminta pengguna memasukkan elemen-elemen matriks
    matrix = []
    print("Masukkan elemen-elemen matriks, baris per baris:")
    for i in range(size):
        row = list(map(int, input(f"Baris {i + 1}: ").split()))
        matrix.append(row)
    
    # Menentukan ukuran matriks dan menghitung determinannya
    if size == 2:
        print("Determinan matriks adalah:", determinant_2x2(matrix))
    elif size == 3:
        print("Determinan matriks adalah:", determinant_3x3(matrix))
    elif size == 4:
        print("Determinan matriks adalah:", determinant_4x4(matrix))
    else:
        print("Ukuran matriks tidak didukung!")

# Menjalankan program
main()
