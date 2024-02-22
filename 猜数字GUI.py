import tkinter as tk
import random

# 创建主窗口
root = tk.Tk()
root.title("猜数字游戏")

# 生成随机数
number_to_guess = random.randint(1, 100)

# 猜数字的函数
def guess():
    guess_number = int(guess_entry.get())
    if guess_number == number_to_guess:
        guess_label.config(text="小猫娘：恭喜你，猜对了喵！")
        guess_entry.delete(0, tk.END)
        guess_button.config(state=tk.DISABLED)
    elif guess_number < number_to_guess:
        guess_label.config(text="小猫娘：太小了喵，再试试看！")
    elif guess_number > number_to_guess:
        guess_label.config(text="小猫娘：太大了喵，再试试看！")

# 创建标签
guess_label = tk.Label(root, text="小猫娘：猜猜我心里的数字（1-100）")
guess_label.pack()

# 创建输入框
guess_entry = tk.Entry(root)
guess_entry.pack()

# 创建按钮
guess_button = tk.Button(root, text="猜！", command=guess)
guess_button.pack()

# 运行游戏
root.mainloop()