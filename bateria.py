
import psutil

bateria = psutil.sensors_battery()

percentual_bateria = str(bateria.percent)

print(f'Este notebook está com {percentual_bateria}% de bateria!')
