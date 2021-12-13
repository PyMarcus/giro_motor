# A fully simulated I2C bus and LCD Display
# The framebuf class simplifies graphics in MicroPython
# Use the hardware i2c in example Pong for faster performance
# Make sure you have the I2C LCD checkbox marked!

import machine
import framebuf # cria matrizes

scl = machine.Pin('X9')  # clock
sda = machine.Pin('X10') # data
i2c = machine.I2C(scl=scl, sda=sda)

# o frame é a tela lcd de 64 x 32

fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)
# logo é a área do desenho - divide-se por 8, pois são 8bits
logo = framebuf.FrameBuffer(bytearray(17 * 17 // 8), 17, 17, framebuf.MONO_HLSB)

logo.fill(0)
logo.fill_rect(1, 1, 15, 15, 1)
logo.vline(2, 13, 2, 0)
logo.vline(4, 4, 12, 0)  # linha vertical de 12 pixels
logo.vline(8, 1, 12,  0) # (x, y, tamanho, cor)
logo.vline(12, 4, 12, 0)
logo.vline(14, 13, 2, 0)

#fbuf.fill(0)
fbuf.blit(logo, 23, 7)  # joga o densenho na frente, tela principal, faz aparecer

i2c.writeto(8, fbuf)  # faz a comunicacao do master com slaver
