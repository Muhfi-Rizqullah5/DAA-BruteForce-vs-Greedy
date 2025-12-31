# Matriks jarak yang sama
distances = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 30, 20],
    [15, 35, 0, 30, 20, 25],
    [20, 25, 30, 0, 15, 10],
    [25, 30, 20, 15, 0, 35],
    [30, 20, 25, 10, 35, 0]
]

def tsp_greedy(start=0):
    """Mencari rute dengan memilih kota terdekat yang belum dikunjungi"""
    n = len(distances)
    visited = [False] * n
    
    current_city = start
    route = [current_city]
    visited[current_city] = True
    total_distance = 0

    # Loop untuk mengunjungi n-1 kota berikutnya
    for _ in range(n - 1):
        next_city = None
        min_dist = float('inf')

        # Cari tetangga terdekat yang belum dikunjungi
        for city in range(n):
            if not visited[city] and distances[current_city][city] < min_dist:
                min_dist = distances[current_city][city]
                next_city = city
        
        if next_city is not None:
            visited[next_city] = True
            route.append(next_city)
            total_distance += min_dist
            current_city = next_city

    # Tambahkan jarak kembali ke kota awal
    total_distance += distances[current_city][start]
    route.append(start)
    
    return route, total_distance

# Eksekusi Program
if __name__ == "__main__":
    print("--- GREEDY ALGORITHM ---")
    route, distance = tsp_greedy(start=0)
    print(f"Rute (Greedy): {route}")
    print(f"Total Jarak  : {distance}")
