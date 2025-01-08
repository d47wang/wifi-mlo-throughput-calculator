import tkinter as tk
from tkinter import ttk

# 定义各频段的吞吐量表
twog_throughput = {
    (20, 2): 344.12,
    (40, 2): 688.24,
    (20, 4): 688.24,
    (40, 4): 1376.47
}

fiveg_throughput = {
    (160, 2): 2882.35,
    (160, 4): 5764.71
}

sixg_throughput = {
    (320, 2): 5764.71,
    (320, 4): 11529.41
}

# 将Mbps转换为Gbps或保持Mbps单位
def convert_units(mbps):
    if mbps >= 1000:
        return f"{mbps / 1000:.2f}Gbps"
    else:
        return f"{int(mbps)}Mbps"

# 计算总吞吐量并更新显示
def calculate_throughput():
    total = 0.0
    components = []
    
    if enable_2g.get():
        bw = twog_bw.get()
        nss = twog_nss.get()
        throughput = twog_throughput.get((int(bw), int(nss)), 0.0)
        components.append(f"{convert_units(throughput)} (2G)")
        total += throughput
    if enable_5g.get():
        bw = fiveg_bw.get()
        nss = fiveg_nss.get()
        throughput = fiveg_throughput.get((int(bw), int(nss)), 0.0)
        components.append(f"{convert_units(throughput)} (5G)")
        total += throughput
    if enable_6g.get():
        bw = sixg_bw.get()
        nss = sixg_nss.get()
        throughput = sixg_throughput.get((int(bw), int(nss)), 0.0)
        components.append(f"{convert_units(throughput)} (6G)")
        total += throughput
    
    total_str = convert_units(total)
    if components:
        result = " + ".join(components) + f" = {total_str}"
    else:
        result = "总吞吐量: 0 Mbps"
    
    total_label.config(text=result)

# 更新UI并重新计算吞吐量
def update_ui(*args):
    calculate_throughput()

# 创建主窗口
root = tk.Tk()
root.title("Wi-Fi MLO TPT Tool by d47wang")

# 创建各频段的框架
frame_2g = ttk.LabelFrame(root, text="2G")
frame_5g = ttk.LabelFrame(root, text="5G")
frame_6g = ttk.LabelFrame(root, text="6G")

frame_2g.grid(row=0, column=0, padx=10, pady=10)
frame_5g.grid(row=0, column=1, padx=10, pady=10)
frame_6g.grid(row=0, column=2, padx=10, pady=10)

# 2G 部分
enable_2g = tk.BooleanVar()
enable_2g.set(True)
enable_2g_check = ttk.Checkbutton(frame_2g, text="启用", variable=enable_2g, command=update_ui)
enable_2g_check.grid(row=0, column=0, columnspan=2)

twog_bw = ttk.Combobox(frame_2g, values=[20, 40], state='readonly', width=5)
twog_bw.set(40)
twog_bw.grid(row=1, column=1)
twog_nss = ttk.Combobox(frame_2g, values=[2, 4], state='readonly', width=5)
twog_nss.set(4)
twog_nss.grid(row=2, column=1)

ttk.Label(frame_2g, text="带宽 (M):").grid(row=1, column=0)
ttk.Label(frame_2g, text="NSS:").grid(row=2, column=0)

# 5G 部分
enable_5g = tk.BooleanVar()
enable_5g.set(True)
enable_5g_check = ttk.Checkbutton(frame_5g, text="启用", variable=enable_5g, command=update_ui)
enable_5g_check.grid(row=0, column=0, columnspan=2)

fiveg_bw = ttk.Combobox(frame_5g, values=[160], state='readonly', width=5)
fiveg_bw.set(160)
fiveg_bw.grid(row=1, column=1)
fiveg_nss = ttk.Combobox(frame_5g, values=[2, 4], state='readonly', width=5)
fiveg_nss.set(4)
fiveg_nss.grid(row=2, column=1)

ttk.Label(frame_5g, text="带宽 (M):").grid(row=1, column=0)
ttk.Label(frame_5g, text="NSS:").grid(row=2, column=0)

# 6G 部分
enable_6g = tk.BooleanVar()
enable_6g.set(True)
enable_6g_check = ttk.Checkbutton(frame_6g, text="启用", variable=enable_6g, command=update_ui)
enable_6g_check.grid(row=0, column=0, columnspan=2)

sixg_bw = ttk.Combobox(frame_6g, values=[320], state='readonly', width=5)
sixg_bw.set(320)
sixg_bw.grid(row=1, column=1)
sixg_nss = ttk.Combobox(frame_6g, values=[2, 4], state='readonly', width=5)
sixg_nss.set(4)
sixg_nss.grid(row=2, column=1)

ttk.Label(frame_6g, text="带宽 (M):").grid(row=1, column=0)
ttk.Label(frame_6g, text="NSS:").grid(row=2, column=0)

# 总吞吐量标签
total_label = ttk.Label(root, text="", foreground="blue")
total_label.grid(row=1, column=0, columnspan=3, pady=10)

# 绑定事件
enable_2g.trace('w', update_ui)
twog_bw.bind('<<ComboboxSelected>>', update_ui)
twog_nss.bind('<<ComboboxSelected>>', update_ui)

enable_5g.trace('w', update_ui)
fiveg_bw.bind('<<ComboboxSelected>>', update_ui)
fiveg_nss.bind('<<ComboboxSelected>>', update_ui)

enable_6g.trace('w', update_ui)
sixg_bw.bind('<<ComboboxSelected>>', update_ui)
sixg_nss.bind('<<ComboboxSelected>>', update_ui)

# 窗口居中
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

calculate_throughput()
root.mainloop()