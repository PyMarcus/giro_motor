"""pwm é modularização por largura de pulso"""
"""Usado para controlar intesidades"""
"""é uma técnica que usa uma saída digital para
simular uma analógica"""
import machine
import pyb
import time

# instanciando o motor:
servo = pyb.Servo(1)
vetor = [0, 90, -90, -60, -45, 30, 12, 0, 90, -24]
for n in range(10):
    time.sleep(1)
    servo.angle(vetor[n], 5000) # angulo de 90,giro horario, e 5000 ms
