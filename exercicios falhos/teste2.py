velocidade = 50
carro_local = 61

RADAR_1 = 50
LOCAL_RADAR_1 = 60
RANGE = 1

multa = velocidade > RADAR_1 and carro_local >= \
(LOCAL_RADAR_1 - RANGE) and carro_local <= (LOCAL_RADAR_1 + RANGE)

carro_passou = (carro_local < LOCAL_RADAR_1 - RANGE) or \
(carro_local > LOCAL_RADAR_1 + RANGE)

if multa:
    print("Carro foi multado!")

elif carro_passou:
    print("Carro longe")

else:
    print("Carro passou no radar 1")
