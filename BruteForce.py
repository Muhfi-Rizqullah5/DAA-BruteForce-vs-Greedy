from itertools import permutations

# Matriks jarak antar kota (6x6)
# Representasi jarak dari PDF
distances = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 30, 20],
    [15, 35, 0, 30, 20, 25],
    [20, 25, 30, 0, 15, 10],
    [25, 30, 20, 15, 0, 35],
    [30, 20, 25, 10, 35, 0]
]

def calculate_distance(route):
    """Menghitung total jarak dari sebuah rute"""
    distance = 0
    # Hitung jarak antar kota dalam rute
    for i in range(len(route) - 1):
        distance += distances[route[i]][route[i+1]]
    
    # Tambahkan jarak kembali ke kota asal
    distance += distances[route[-1]][route[0]]
    return distance

def tsp_brute_force():
    """Mencari rute terbaik dengan mencoba SEMUA kemungkinan (Permutasi)"""
    n = len(distances)
    cities_list = list(range(n))
    
    best_route = None
    min_distance = float('inf')

    # Cek setiap kemungkinan permutasi rute
    # Catatan: Ini O(n!) - Sangat berat!
    for route in permutations(cities_list):
        # Asumsikan selalu mulai dari kota 0 untuk mengurangi duplikasi cek
        if route[0] != 0: 
            continue
            
        dist = calculate_distance(route)
        if dist < min_distance:
            min_distance = dist
            best_route = route

    # Format output agar kembali ke kota awal
    final_route = list(best_route) + [best_route[0]]
    return final_route, min_distance

# Eksekusi Program
if __name__ == "__main__":
    print("--- BRUTE FORCE ALGORITHM ---")
    route, distance = tsp_brute_force()
    print(f"Rute Terbaik: {route}")
    print(f"Total Jarak : {distance}")
