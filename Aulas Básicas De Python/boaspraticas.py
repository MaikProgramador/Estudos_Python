velocidade = 50
local_carro = 70

RADAR_1 = 50
LOCAL_1 = 70
RADAR_RANGE = 1

velocidade_ultrapassada = velocidade > RADAR_1 and \
    local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_longe = local_carro < (LOCAL_1 - RADAR_RANGE) or \
local_carro > (LOCAL_1 + RADAR_RANGE)


if velocidade_ultrapassada:
    print("O carro foi multado!")

elif carro_longe:
    print("Carro está longe")

else:
    print("Carro passou no radar1")