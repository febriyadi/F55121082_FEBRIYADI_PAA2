import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Menambahkan penanda untuk pertukaran elemen
        swapped = False

        print(f"Iterasi ke-{i + 1}:")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(arr)  # Menampilkan array setiap kali terjadi pertukaran

        # Jika tidak ada pertukaran dalam satu iterasi, hentikan iterasi
        if not swapped:
            break
        print("")

    print("Array yang telah diurutkan:")
    print(arr)


# Array yang akan diurutkan
arr = [6, 5, 5, 1, 2, 1, 0, 8, 2]

# Mencatat waktu awal
start_time = time.time()

# Memanggil fungsi bubble_sort
bubble_sort(arr)

# Mencatat waktu akhir
end_time = time.time()

# Menghitung waktu eksekusi dalam milidetik
execution_time = (end_time - start_time) * 1000

print("Waktu eksekusi: %.2f milidetik" % execution_time)
