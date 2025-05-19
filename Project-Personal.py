import math
import random
import pygame
import time
import tkinter as tk
from tkinter import messagebox, ttk
import sys
from collections import deque
import heapq
import psutil
import os
import tracemalloc
from tkinter import font as tkfont
from datetime import datetime
from PIL import Image

# Trạng thái đích của bài toán 8-Puzzle
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def find_zero(state):
    """Tìm vị trí của ô trống (số 0) trong ma trận trạng thái"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    """Tạo danh sách các trạng thái có thể di chuyển từ trạng thái hiện tại"""
    x, y = find_zero(state)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Các hướng di chuyển: lên, xuống, trái, phải
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Kiểm tra vị trí mới có hợp lệ không
            new_state = [row[:] for row in state]  # Tạo bản sao của trạng thái hiện tại
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]  # Hoán đổi vị trí
            neighbors.append(new_state)
    
    return neighbors

def bfs(initial_state):
    """Thuật toán BFS (Breadth-First Search) - Tìm kiếm theo chiều rộng"""

    queue = deque([(initial_state, [])])  # Hàng đợi chứa (trạng thái hiện tại, đường đi)
    visited = set()  # Tập các trạng thái đã thăm
    
    while queue:
        state, path = queue.popleft()  # Lấy trạng thái đầu tiên từ hàng đợi
        if state == GOAL_STATE:  # Nếu là trạng thái đích
            return path + [state]  # Trả về đường đi từ trạng thái ban đầu đến đích
        
        visited.add(tuple(map(tuple, state)))  # Đánh dấu trạng thái đã thăm
        
        for neighbor in get_neighbors(state):  # Xét các trạng thái con
            if tuple(map(tuple, neighbor)) not in visited:  # Nếu chưa thăm
                queue.append((neighbor, path + [state]))  # Thêm vào hàng đợi
    
    return None  # Không tìm thấy lời giải

# Thuật toán DFS có giới hạn độ sâu
def dfs(initial_state, max_depth=30):
    stack = [(initial_state, [], 0)]  # (trạng thái hiện tại, đường đi, độ sâu)
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))

    while stack:
        state, path, depth = stack.pop()

        if state == GOAL_STATE:
            return path + [state]

        if depth < max_depth:
            for neighbor in get_neighbors(state):
                neighbor_tuple = tuple(map(tuple, neighbor))
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)
                    stack.append((neighbor, path + [state], depth + 1))

    return None  # Không tìm thấy lời giải trong giới hạn độ sâu

def uniform_cost_search(initial_state):
    """Thuật toán Uniform Cost Search (UCS) - Tìm kiếm theo chi phí đồng nhất"""
    pq = [(0, initial_state, [])]  # Hàng đợi ưu tiên chứa (chi phí, trạng thái, đường đi)
    visited = set()  # Tập các trạng thái đã thăm
    
    while pq:
        cost, state, path = heapq.heappop(pq)  # Lấy trạng thái có chi phí nhỏ nhất
        
        if state == GOAL_STATE:  # Nếu là trạng thái đích
            return path + [state]  # Trả về đường đi
        
        visited.add(tuple(map(tuple, state)))  # Đánh dấu trạng thái đã thăm
        
        for neighbor in get_neighbors(state):  # Xét các trạng thái con
            if tuple(map(tuple, neighbor)) not in visited:  # Nếu chưa thăm
                heapq.heappush(pq, (cost + 1, neighbor, path + [state]))  # Thêm vào hàng đợi ưu tiên
    
    return None  # Không tìm thấy lời giải

def iterative_deepening(initial_state, max_depth=20):
    """Thuật toán ID (Iterative Deepening) - Tìm kiếm theo độ sâu tăng dần"""
    def dls(state, path, depth):
        """Hàm tìm kiếm theo độ sâu giới hạn"""
        if state == GOAL_STATE:  # Nếu là trạng thái đích
            return path + [state]  # Trả về đường đi
        if depth == 0:  # Nếu đã đạt độ sâu tối đa
            return None  # Không tìm thấy lời giải
        
        for neighbor in get_neighbors(state):  # Xét các trạng thái con
            result = dls(neighbor, path + [state], depth - 1)  # Tìm kiếm đệ quy
            if result:  # Nếu tìm thấy lời giải
                return result
        
        return None  # Không tìm thấy lời giải
    
    for depth in range(max_depth):  # Tăng dần độ sâu tìm kiếm
        result = dls(initial_state, [], depth)  # Tìm kiếm với độ sâu hiện tại
        if result:  # Nếu tìm thấy lời giải
            return result
    return None  # Không tìm thấy lời giải

def greedy(initial_state):
    """Thuật toán Greedy Best-First Search - Tìm kiếm tham lam"""
    def heuristic(state):
        """Hàm đánh giá heuristic - số ô sai vị trí"""
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    pq = [(heuristic(initial_state), initial_state, [])]  # Hàng đợi ưu tiên
    visited = set()  # Tập các trạng thái đã thăm
    
    while pq:
        _, state, path = heapq.heappop(pq)  # Lấy trạng thái có giá trị heuristic nhỏ nhất
        
        if state == GOAL_STATE:  # Nếu là trạng thái đích
            return path + [state]  # Trả về đường đi
        
        visited.add(tuple(map(tuple, state)))  # Đánh dấu trạng thái đã thăm
        
        for neighbor in get_neighbors(state):  # Xét các trạng thái con
            if tuple(map(tuple, neighbor)) not in visited:  # Nếu chưa thăm
                heapq.heappush(pq, (heuristic(neighbor), neighbor, path + [state]))  # Thêm vào hàng đợi
    
    return None  # Không tìm thấy lời giải

def heuristic(state):
    """Hàm đánh giá heuristic - số ô sai vị trí"""
    return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))

def simple_hill_climbing(initial_state):
    """Thuật toán Simple Hill Climbing - Leo đồi đơn giản"""
    current = initial_state
    path = [current]  # Lưu lại đường đi

    while True:
        if current == GOAL_STATE:
            return path  # Đã đến đích

        neighbors = get_neighbors(current)
        if not neighbors:
            return path  # Không còn neighbor tốt hơn, dừng lại

        next_state = min(neighbors, key=heuristic, default=None)
        # Nếu không cải thiện hoặc không có neighbor tốt hơn, dừng lại
        if next_state is None or heuristic(next_state) >= heuristic(current):
            return path

        current = next_state
        path.append(current)

def astar(initial_state):
    """Thuật toán A* - Kết hợp chi phí và heuristic"""
    def heuristic(state):
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    pq = [(heuristic(initial_state), 0, initial_state, [])]  # (f, g, state, path)
    visited = set()
    
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == GOAL_STATE:
            return path + [state]
        visited.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [state]))
    return None

def ida_star(initial_state):
    """Thuật toán IDA* - Kết hợp ID và A*"""
    def heuristic(state):
        """Hàm đánh giá heuristic - số ô sai vị trí"""
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    def search(state, path, g, threshold):
        """Hàm tìm kiếm đệ quy với ngưỡng f(n)"""
        f = g + heuristic(state)  # Tính giá trị f(n)
        if f > threshold:  # Nếu vượt ngưỡng
            return f, None
        if state == GOAL_STATE:  # Nếu là trạng thái đích
            return f, path + [state]  # Trả về đường đi
        
        min_threshold = float("inf")  # Ngưỡng nhỏ nhất cho lần lặp tiếp
        for neighbor in get_neighbors(state):  # Xét các trạng thái con
            if neighbor not in path:  # Nếu chưa thăm
                new_threshold, result = search(neighbor, path + [state], g + 1, threshold)  # Tìm kiếm đệ quy
                if result:  # Nếu tìm thấy lời giải
                    return new_threshold, result
                min_threshold = min(min_threshold, new_threshold)  # Cập nhật ngưỡng
        
        return min_threshold, None  # Không tìm thấy lời giải

    threshold = heuristic(initial_state)  # Khởi tạo ngưỡng
    while True:
        new_threshold, result = search(initial_state, [], 0, threshold)  # Tìm kiếm với ngưỡng hiện tại
        if result:  # Nếu tìm thấy lời giải
            return result
        if new_threshold == float("inf"):  # Nếu không thể tìm thấy lời giải
            return None
        threshold = new_threshold  # Tăng ngưỡng cho lần lặp tiếp

def steepest_ascent_hill_climbing(initial_state):
    """Thuật toán Steepest Ascent Hill Climbing - Leo đồi dốc nhất"""
    current = initial_state
    path = [current]  # Lưu lại đường đi
    
    while True:
        neighbors = get_neighbors(current)  # Lấy các trạng thái con
        best_neighbor = min(neighbors, key=heuristic, default=None)  # Chọn trạng thái tốt nhất
        
        if best_neighbor and heuristic(best_neighbor) < heuristic(current):  # Nếu có cải thiện
            current = best_neighbor
            path.append(current)
        else:
            return path  # Trả về đường đi đã tìm được

def stochastic_hill_climbing(initial_state):
    """Thuật toán Stochastic Hill Climbing - Leo đồi ngẫu nhiên"""
    current = initial_state
    path = [current]  # Lưu lại đường đi
    
    while True:
        neighbors = get_neighbors(current)  # Lấy các trạng thái con
        better_neighbors = [n for n in neighbors if heuristic(n) < heuristic(current)]  # Lọc các trạng thái tốt hơn
        
        if better_neighbors:  # Nếu có trạng thái tốt hơn
            current = random.choice(better_neighbors)  # Chọn ngẫu nhiên một trạng thái
            path.append(current)
        else:
            return path  # Trả về đường đi đã tìm được

def simulated_annealing(initial_state, max_iterations=10000, initial_temp=100, cooling_rate=0.99):
    """Thuật toán Simulated Annealing - Mô phỏng ủ kim loại"""
    current = initial_state
    path = [current]  # Lưu lại đường đi
    temp = initial_temp  # Nhiệt độ ban đầu
    
    for _ in range(max_iterations):  # Lặp tối đa max_iterations lần
        neighbors = get_neighbors(current)  # Lấy các trạng thái con
        if not neighbors:  # Nếu không có trạng thái con
            break
        
        next_state = random.choice(neighbors)  # Chọn ngẫu nhiên một trạng thái
        delta_e = heuristic(current) - heuristic(next_state)  # Tính độ chênh lệch
        
        if delta_e > 0 or math.exp(delta_e / temp) > random.random():  # Quyết định chấp nhận trạng thái mới
            current = next_state
            path.append(current)
        
        temp *= cooling_rate  # Giảm nhiệt độ
        if heuristic(current) == 0:  # Nếu đã đạt trạng thái đích
            break
    
    return path  # Trả về đường đi đã tìm được

def beam_search(initial_state, beam_width=2):
    """Thuật toán Beam Search - Tìm kiếm chùm"""
    queue = [(heuristic(initial_state), initial_state, [])]  # Hàng đợi chứa (heuristic, trạng thái, đường đi)
    
    while queue:
        queue.sort()  # Sắp xếp theo giá trị heuristic
        queue = queue[:beam_width]  # Chỉ giữ lại số lượng trạng thái tốt nhất theo beam_width
        new_queue = []  # Hàng đợi mới cho lần lặp tiếp
        
        for _, state, path in queue:  # Xét từng trạng thái trong hàng đợi
            if state == GOAL_STATE:  # Nếu là trạng thái đích
                return path + [state]  # Trả về đường đi
            
            for neighbor in get_neighbors(state):  # Xét các trạng thái con
                new_queue.append((heuristic(neighbor), neighbor, path + [state]))  # Thêm vào hàng đợi mới
        
        queue = new_queue  # Cập nhật hàng đợi
    
    return None  # Không tìm thấy lời giải

def backtracking_search(initial_state, max_depth=30):
    """Thuật toán Backtracking Search - Quay lui"""
    visited = set()  # Tập các trạng thái đã thăm

    def backtrack(state, path, depth):
        """Hàm quay lui đệ quy"""
        if state == GOAL_STATE:  # Nếu là trạng thái đích
            return path + [state]  # Trả về đường đi
        if depth == 0:  # Nếu đã đạt độ sâu tối đa
            return None  # Không tìm thấy lời giải
        
        visited.add(tuple(map(tuple, state)))  # Đánh dấu trạng thái đã thăm

        for neighbor in get_neighbors(state):  # Xét các trạng thái con
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:  # Nếu chưa thăm
                result = backtrack(neighbor, path + [state], depth - 1)  # Tìm kiếm đệ quy
                if result:  # Nếu tìm thấy lời giải
                    return result
        
        visited.remove(tuple(map(tuple, state)))  # Quay lui: bỏ khỏi visited
        return None  # Không tìm thấy lời giải

    return backtrack(initial_state, [], max_depth)  # Bắt đầu tìm kiếm

def local_search_csp(initial_state, max_steps=10000):
    """Thuật toán Local Search cho CSP - Min-Conflicts"""
    
    def conflicts(state):
        """Hàm đánh giá số lượng xung đột"""
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    current = initial_state
    path = [current]  # Lưu lại đường đi
    
    for step in range(max_steps):  # Lặp tối đa max_steps lần
        if conflicts(current) == 0:  # Nếu không còn xung đột
            return path  # Trả về đường đi
        
        neighbors = get_neighbors(current)  # Lấy các trạng thái con
        if not neighbors:  # Nếu không có trạng thái con
            break
        
        next_state = min(neighbors, key=conflicts)  # Chọn trạng thái ít xung đột nhất
        if conflicts(next_state) >= conflicts(current):  # Nếu không cải thiện
            next_state = random.choice(neighbors)  # Chọn ngẫu nhiên một trạng thái
        
        current = next_state
        path.append(current)
    
    return path  # Trả về đường đi đã tìm được

def draw_board(state, screen):
    """Vẽ bảng trạng thái hiện tại lên màn hình"""
    screen.fill((255, 255, 255))  # Xóa màn hình với màu trắng
    font = pygame.font.Font(None, 50)  # Tạo font chữ
    TILE_SIZE = 100  # Kích thước mỗi ô
    
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:  # Nếu không phải ô trống
                pygame.draw.rect(screen, (100, 100, 250), (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Vẽ ô
                text = font.render(str(value), True, (255, 255, 255))  # Tạo text
                screen.blit(text, (j*TILE_SIZE + TILE_SIZE//3, i*TILE_SIZE + TILE_SIZE//3))  # Vẽ text
    
    pygame.display.flip()  # Cập nhật màn hình

def visualize_solution(solution, delay=500):
    """Hiển thị quá trình giải bài toán và lưu ảnh từng bước, sau đó tạo GIF"""
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("8-Puzzle Solver")
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    image_paths = []

    prev_state = None
    for i, state in enumerate(solution):
        draw_board(state, screen)
        pygame.time.wait(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Lưu ảnh màn hình pygame
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(screenshots_dir, f"step_{i+1}_{timestamp}.png")
        pygame.image.save(screen, filename)
        image_paths.append(filename)

    pygame.time.wait(1000)
    pygame.quit()

    # Tạo GIF từ các ảnh đã lưu
    if image_paths:
        create_gif(image_paths, os.path.join(screenshots_dir, f"puzzle_{timestamp}.gif"))
        # Xóa các file ảnh sau khi tạo GIF (nếu muốn)
        for path in image_paths:
            os.remove(path)

def create_gif(image_files, output_file):
    """Tạo file GIF từ danh sách ảnh"""
    from PIL import Image
    frames = [Image.open(img) for img in image_files]
    frames[0].save(output_file, format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)

def evaluate_algorithm(algorithm_func, initial_state):
    """Đánh giá hiệu suất của thuật toán"""
    # Bắt đầu theo dõi bộ nhớ
    tracemalloc.start()
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    # Bắt đầu đo thời gian
    start_time = time.time()
    
    # Chạy thuật toán
    solution = algorithm_func(initial_state)
    
    # Kết thúc đo thời gian
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Kết thúc theo dõi bộ nhớ
    current_memory = process.memory_info().rss / 1024 / 1024  # MB
    max_memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # MB
    tracemalloc.stop()
    
    # Tính số bước
    steps = len(solution) - 1 if solution else 0

    # In ra console bộ nhớ sử dụng
    print(f"Bộ nhớ ban đầu: {initial_memory:.5f} MB")
    print(f"Bộ nhớ hiện tại: {current_memory:.5f} MB")
    print(f"Bộ nhớ tối đa: {max_memory:.5f} MB")

    return {
        "execution_time": execution_time,
        "initial_memory": initial_memory,
        "current_memory": current_memory,
        "max_memory": max_memory,
        "steps": steps,
        "solution": solution
    }

def start_solver():
    """Xử lý khi nhấn nút 'Giải' trong giao diện"""
    try:
        initial_state = [[int(entry.get()) for entry in row] for row in entries]  # Lấy trạng thái ban đầu
        algorithm = algorithm_var.get()  # Lấy thuật toán được chọn
        
        algorithms = {
            "BFS": bfs,
            "DFS": dfs,
            "UCS": uniform_cost_search,
            "ID": iterative_deepening,
            "Greedy": greedy,
            "A*": astar,
            "IDA*": ida_star,
            "Simple Hill Climbing": simple_hill_climbing,
            "Steepest Ascent Hill Climbing": steepest_ascent_hill_climbing,
            "Stochastic Hill Climbing": stochastic_hill_climbing,
            "Simulated Annealing": simulated_annealing,
            "Beam Search": beam_search,
            "Backtracking": backtracking_search,
            "Local Search CSP": local_search_csp
        }
        
        # Đánh giá thuật toán
        results = evaluate_algorithm(algorithms[algorithm], initial_state)
        
        if results["solution"]:  # Nếu tìm thấy lời giải
            # Hiển thị kết quả đánh giá
            evaluation_message = f"""Kết quả đánh giá thuật toán {algorithm}:
Thời gian thực thi: {results['execution_time']:.5f} giây
Bộ nhớ ban đầu: {results['initial_memory']:.5f} MB
Bộ nhớ hiện tại: {results['current_memory']:.5f} MB
Bộ nhớ tối đa: {results['max_memory']:.5f} MB
Số bước thực hiện: {results['steps']}"""
            
            messagebox.showinfo("Kết quả đánh giá", evaluation_message)
            visualize_solution(results["solution"])
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy lời giải.")
            
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số cho trạng thái ban đầu.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    # Khởi tạo cửa sổ chính
    root = tk.Tk()
    root.title("8-Puzzle Solver")
    root.configure(bg='#f0f0f0')
    
    # Thiết lập kích thước và vị trí cửa sổ
    window_width = 500
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Tạo frame chính với padding
    main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
    main_frame.pack(expand=True, fill='both')
    
    # Tiêu đề
    title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
    title_label = tk.Label(main_frame, text="8-Puzzle Solver", font=title_font, bg='#f0f0f0', fg='#2c3e50')
    title_label.pack(pady=(0, 20))
    
    # Tạo frame cho nhập liệu
    input_frame = tk.LabelFrame(main_frame, text="Nhập trạng thái ban đầu", font=("Helvetica", 12), 
                              bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
    input_frame.pack(pady=10, fill='x')
    
    # Tạo lưới cho các ô nhập liệu
    entries = []
    for i in range(3):
        row_entries = []
        for j in range(3):
            entry = tk.Entry(input_frame, width=5, font=("Helvetica", 20), justify="center",
                           bg='#ffffff', fg='#2c3e50', relief='solid', bd=1)
            entry.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
            row_entries.append(entry)
        entries.append(row_entries)
    
    # Cấu hình trọng số cho lưới
    for i in range(3):
        input_frame.grid_columnconfigure(i, weight=1)
        input_frame.grid_rowconfigure(i, weight=1)
    
    # Frame chọn thuật toán
    algo_frame = tk.LabelFrame(main_frame, text="Chọn thuật toán", font=("Helvetica", 12),
                             bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
    algo_frame.pack(pady=10, fill='x')
    
    # Tạo style cho combobox
    style = ttk.Style()
    style.configure('Custom.TCombobox', 
                   fieldbackground='#ffffff',
                   background='#ffffff',
                   foreground='#2c3e50',
                   arrowcolor='#2c3e50')
    
    # Tạo combobox chọn thuật toán
    algorithm_var = tk.StringVar(root)
    algorithm_var.set("BFS")
    algorithms = ["BFS", "DFS", "UCS", "ID", "Greedy", "A*", "IDA*", 
                 "Simple Hill Climbing", "Steepest Ascent Hill Climbing", 
                 "Stochastic Hill Climbing", "Simulated Annealing", 
                 "Beam Search", "Backtracking", "Local Search CSP"]
    
    algo_combo = ttk.Combobox(algo_frame, textvariable=algorithm_var, 
                             values=algorithms, state="readonly",
                             font=("Helvetica", 12), style='Custom.TCombobox')
    algo_combo.pack(fill='x', padx=5, pady=5)
    
    # Nút giải với style tùy chỉnh
    solve_button = tk.Button(main_frame, text="Giải", command=start_solver,
                           font=("Helvetica", 14, "bold"),
                           bg='#3498db', fg='white',
                           activebackground='#2980b9',
                           activeforeground='white',
                           relief='flat',
                           padx=20, pady=10,
                           cursor='hand2')
    solve_button.pack(pady=20)
    
    # Thêm hiệu ứng hover cho nút
    def on_enter(e):
        solve_button['background'] = '#2980b9'
    
    def on_leave(e):
        solve_button['background'] = '#3498db'
    
    solve_button.bind("<Enter>", on_enter)
    solve_button.bind("<Leave>", on_leave)
    
    # Thêm hướng dẫn
    instructions = """Hướng dẫn:
1. Nhập trạng thái ban đầu của puzzle (0-8)
2. Chọn thuật toán giải
3. Nhấn 'Giải' để xem kết quả"""
    
    instruction_label = tk.Label(main_frame, text=instructions,
                               font=("Helvetica", 10),
                               bg='#f0f0f0', fg='#7f8c8d',
                               justify='left')
    instruction_label.pack(pady=10)
    
    root.mainloop()
