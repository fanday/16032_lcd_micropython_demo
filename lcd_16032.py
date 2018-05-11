from machine import SPI
from machine import Pin
import utime

V0 = Pin(0, Pin.OUT)
V0.value(1)

print("V0")
SCK = Pin(2, Pin.OUT)
print(SCK)
SID = Pin(15, Pin.OUT)
CS = Pin(4, Pin.OUT)
MISO = Pin(16, Pin.OUT)
print("cs")
dev_16032_spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=SCK, mosi=SID, miso=MISO)
print("spi device ok")

def write_cmd(cmd):
  global dev_16032_spi
  start_data = 0xf8
  Hdata = cmd &0xf0
  Ldata = (cmd<<4)&0xf0

  d = bytearray([start_data])
  dev_16032_spi.write(d)
  utime.sleep_ms(5)
  d = bytearray([Hdata])
  dev_16032_spi.write(d)
  utime.sleep_ms(5)
  d = bytearray([Ldata])
  dev_16032_spi.write(d)
  utime.sleep_ms(5)

def write_char(data):
  global dev_16032_spi
  start_data = 0xfa
  print(ord(data))
  Hdata = ord(data) &0xf0
  Ldata = (ord(data)<<4)&0xf0

  d = bytearray([start_data])
  dev_16032_spi.write(d)
  utime.sleep_ms(5)
  d = bytearray([Hdata])
  dev_16032_spi.write(d)
  utime.sleep_ms(5)
  d = bytearray([Ldata])
  dev_16032_spi.write(d)
  utime.sleep_ms(5)

def lcd_init():
  utime.sleep_ms(50)
  CS.value(1)
  write_cmd(0x30)
  write_cmd(0x0c)
  write_cmd(0x01)

def display_str(text):
  for t in text:
    write_char(t)



print("init lcd")
lcd_init()
display_str('hello 123456')
