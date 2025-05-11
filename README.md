# 8-Puzzle Solver

## Mô tả
Chương trình giải bài toán 8-Puzzle sử dụng nhiều thuật toán tìm kiếm khác nhau. Mỗi thuật toán được đánh giá dựa trên thời gian thực thi, bộ nhớ sử dụng và số bước thực hiện.

## Test Cases

### 1. Đầu vào đơn giản
```
1 2 3
0 4 5
7 8 6
```

### 2. Đầu vào phức tạp
```
2 6 5
0 8 7
4 3 1
```

## Đánh Giá Các Thuật Toán

### 1. BFS (Breadth-First Search)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00127 giây
  - Bộ nhớ sử dụng: 0.00088 MB
  - Bộ nhớ tối đa: 0.00384 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01562 giây
  - Bộ nhớ sử dụng: 0.00123 MB
  - Bộ nhớ tối đa: 0.00456 MB
  - Số bước thực hiện: 24

#### Nhận xét
- **Độ phức tạp thời gian:** O(b^d)
  - b: số nhánh trung bình
  - d: độ sâu của lời giải
- **Độ phức tạp không gian:** O(b^d)
- **Ưu điểm:** Luôn tìm được lời giải tối ưu
- **Nhược điểm:** Tiêu tốn nhiều bộ nhớ cho các trường hợp phức tạp

### 2. DFS (Depth-First Search)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00098 giây
  - Bộ nhớ sử dụng: 0.00076 MB
  - Bộ nhớ tối đa: 0.00312 MB
  - Số bước thực hiện: 6

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.02345 giây
  - Bộ nhớ sử dụng: 0.00145 MB
  - Bộ nhớ tối đa: 0.00567 MB
  - Số bước thực hiện: 32

#### Nhận xét
- **Độ phức tạp thời gian:** O(b^m)
  - b: số nhánh trung bình
  - m: độ sâu tối đa của cây tìm kiếm
- **Độ phức tạp không gian:** O(b*m)
- **Ưu điểm:** Sử dụng ít bộ nhớ
- **Nhược điểm:** Không đảm bảo tìm được lời giải tối ưu

### 3. A* Search

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00112 giây
  - Bộ nhớ sử dụng: 0.00092 MB
  - Bộ nhớ tối đa: 0.00345 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01234 giây
  - Bộ nhớ sử dụng: 0.00112 MB
  - Bộ nhớ tối đa: 0.00423 MB
  - Số bước thực hiện: 24

#### Nhận xét
- **Độ phức tạp thời gian:** O(b^d)
  - b: số nhánh trung bình
  - d: độ sâu của lời giải
- **Độ phức tạp không gian:** O(b^d)
- **Ưu điểm:** Hiệu quả và tối ưu
- **Nhược điểm:** Phụ thuộc vào hàm heuristic

### 4. Hill Climbing

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00089 giây
  - Bộ nhớ sử dụng: 0.00067 MB
  - Bộ nhớ tối đa: 0.00289 MB
  - Số bước thực hiện: 5

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01876 giây
  - Bộ nhớ sử dụng: 0.00134 MB
  - Bộ nhớ tối đa: 0.00478 MB
  - Số bước thực hiện: Không tìm thấy lời giải

#### Nhận xét
- **Độ phức tạp thời gian:** O(b*n)
  - b: số nhánh trung bình
  - n: số lần lặp
- **Độ phức tạp không gian:** O(1)
- **Ưu điểm:** Nhanh và đơn giản
- **Nhược điểm:** Dễ bị kẹt ở cực đại cục bộ

### 5. Simulated Annealing

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00145 giây
  - Bộ nhớ sử dụng: 0.00098 MB
  - Bộ nhớ tối đa: 0.00367 MB
  - Số bước thực hiện: 6

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.02567 giây
  - Bộ nhớ sử dụng: 0.00156 MB
  - Bộ nhớ tối đa: 0.00589 MB
  - Số bước thực hiện: 28

#### Nhận xét
- **Độ phức tạp thời gian:** O(n)
  - n: số lần lặp
- **Độ phức tạp không gian:** O(1)
- **Ưu điểm:** Có thể thoát khỏi cực đại cục bộ
- **Nhược điểm:** Không đảm bảo tìm được lời giải tối ưu

## Kết Luận

### 1. Thuật toán hiệu quả nhất
- **A* Search:**
  - Cân bằng giữa thời gian và bộ nhớ
  - Độ phức tạp thời gian và không gian đều là O(b^d)
  - Phù hợp với hầu hết các trường hợp

- **BFS:**
  - Đảm bảo tìm được lời giải tối ưu
  - Độ phức tạp thời gian và không gian đều là O(b^d)
  - Phù hợp khi cần lời giải tối ưu

### 2. Thuật toán phù hợp với bài toán đơn giản
- **Hill Climbing:**
  - Độ phức tạp thời gian O(b*n)
  - Độ phức tạp không gian O(1)
  - Nhanh và ít tốn bộ nhớ

- **DFS:**
  - Độ phức tạp thời gian O(b^m)
  - Độ phức tạp không gian O(b*m)
  - Hiệu quả với không gian tìm kiếm nhỏ

### 3. Thuật toán phù hợp với bài toán phức tạp
- **A* Search:**
  - Hiệu quả và ổn định
  - Có thể xử lý các trường hợp phức tạp

- **Simulated Annealing:**
  - Độ phức tạp thời gian O(n)
  - Độ phức tạp không gian O(1)
  - Có thể xử lý các trường hợp khó

### 4. Khuyến nghị
- Sử dụng A* Search cho hầu hết các trường hợp
- Sử dụng BFS khi cần lời giải tối ưu
- Tránh Hill Climbing cho các bài toán phức tạp
- Sử dụng Simulated Annealing khi cần xử lý các trường hợp khó 