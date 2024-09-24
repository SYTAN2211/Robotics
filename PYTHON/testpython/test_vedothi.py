import matplotlib.pyplot as plt
import numpy as np

def plot_quadratic(a, b, c):
    # Tạo dãy giá trị x từ -10 đến 10 với bước nhảy 0.1
    x = np.linspace(-10, 10, 400)
    # Tính giá trị y dựa trên hàm bậc hai
    y = a * x**2 + b * x + c

    # Vẽ đồ thị
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.title('Đồ thị hàm bậc hai')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)  # Trục x
    plt.axvline(0, color='black',linewidth=0.5)  # Trục y
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("Nhập các hệ số cho hàm bậc hai (ax^2 + bx + c):")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    plot_quadratic(a, b, c)
