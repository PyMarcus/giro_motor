import machine
import pyb

# conversor de 8 bits, ou seja, 2^8 = 256 possibilidades de inteiros, a tensao máxima será em 255 e a mínima em 0


# pega a posição do potenciômetro no circuito, poderia ser um sensor:
sensor = machine.Pin('Y4')
converte_analogico_digital = pyb.ADC(sensor) # retorna o número equivalente aos inteiros decimais de 0 a 255, analógico para digital
print(converte_analogico_digital.read())

# converter o valor para nível de tensão:
volts = converte_analogico_digital.read() * 3.3 / 255  #255, pois é a capacidade de inteiros para a placa
print('{} V'.format(volts))