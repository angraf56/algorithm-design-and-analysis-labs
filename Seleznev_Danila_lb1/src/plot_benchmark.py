import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark_data.csv')

df_odd = df[df['N'] % 2 != 0]

plt.figure(figsize=(10, 6))
plt.plot(df_odd['N'], df_odd['Time_ns'], 'ro-', markersize=8, linewidth=2)
plt.xlabel('Размер квадрата N')
plt.ylabel('Время (наносекунды)')
plt.title('Исследование времени выполнения от размера квадрата (нечетные N)')
plt.grid(True, alpha=0.3)
plt.yscale('log')

plt.tight_layout()
plt.show()
