import machine
import utime
from DFPModule import DFPlayer
import time
import network
import ntptime
from machine import Pin, I2C
import ssd1306


sensor_temp = machine.ADC(4)

# ADCの最大電圧3.3Vを16bit(65535)で割って、
# 16bitの 1 目盛りのあたりの電圧(変換係数)を計算します( 約 0.00005V)
conversion_factor = 3.3 / (65535)

i2c = I2C(0, sda=Pin(16), scl=Pin(17) )

display = ssd1306.SSD1306_I2C(128, 64, i2c)


SSID = 'あなたのネットのSSID'
PW = 'ネットのパスワード'



#SSID = '



display.fill(0)
display.text("Hello", 40, 25, 1)
display.show()
time.sleep(1)

addr = i2c.scan()
print("address is :" + str(addr))




# Wi-Fi接続の設定
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PW)

# 接続が確立されるまで待機
while not wlan.isconnected():
    print('Connecting to Wi-Fi...')
    time.sleep(1)
    display.fill(0)
    display.text('Connecting to Wi', 0, 25, 1)
    display.text("-Fi...",0,35,1)
    display.show()
    

print('Connected to Wi-Fi')
display.fill(0)
display.text('Connected to Wi-', 0, 25, 1)
display.text("Fi",0,35,1)
display.show()
time.sleep(0.5)

# NTPサーバーを設定
ntptime.host = 'pool.ntp.org'

# NTPサーバーからの時間を同期
try:
    ntptime.settime()
    print('Time synchronized')
    display.fill(0)
    display.text('Time synchronize', 0, 25, 1)
    display.text('d', 0, 35, 1)
    display.show()
    time.sleep(1)
except OSError as e:
    print(f'Failed to synchronize time: {e}')
    display.fill(0)
    display.text('Failed to synchr', 0, 0, 1)
    display.text("onize time with NTP server",0,10,1)
    display.text("NTP server",0,20,1)
    display.show()
    time.sleep(1)

# 日本標準時（JST）に変換する関数
def to_jst(utc_time):
    # UTCからJSTへ変換
    jst_time = list(utc_time)
    jst_time[3] = (jst_time[3] + 9) % 24  # 時間を9時間進める
    return tuple(jst_time)

player = DFPlayer(8, 9, 20)

btn1 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
btn2 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
btn3 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
btn4 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
btn5 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
btn6 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
btn7 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
btn8 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)

ON = 0
OFF = 1

btn1_prev = OFF
btn2_prev = OFF
btn3_prev = OFF
btn4_prev = OFF
btn5_prev = OFF
btn6_prev = OFF
btn7_prev = OFF
btn8_prev = OFF

pause = False
repeat = False

track = 1
max = 25


# アラームを設定する時間 自由に変えてください
alarm_time = "13:02:50"

while True:
    reading = sensor_temp.read_u16() * conversion_factor
   
    temperature = 27 - (reading - 0.706)/0.001721
    
    btn1_state = btn1.value()
    btn2_state = btn2.value()
    btn3_state = btn3.value()
    btn4_state = btn4.value()
    btn5_state = btn5.value()
    btn6_state = btn6.value()
    btn7_state = btn6.value()
    btn8_state = btn6.value()

    # 次のトラックを再生
    if btn1_prev == OFF and btn1_state == ON:
        track += 1
        display.fill(0)
        display.text("Play the next tr", 0, 10, 1)
        display.text("ack", 0, 20, 1)
        display.show()
        if track > max:
            track = 1
            player.play(track)
            display.fill(0)
            display.text("Play the next tr", 0, 10, 1)
            display.text("ack", 0, 20, 1)
            display.show()
        player.play(track)
        time.sleep(1.5)
        

    # 前のトラックを再生
    if btn2_prev == OFF and btn2_state == ON:
        track -= 1
        display.fill(0)
        display.text("Play the previou", 0, 10, 1)
        display.text("s track", 0, 20, 1)
        display.show()
        if track < 1:
            player.play(track)
            track = max
            player.play(track)
            display.fill(0)
            display.text("Play the previou", 0, 10, 1)
            display.text("s track", 0, 20, 1)
            display.show()
        player.play(track)
        time.sleep(1.5)
        
        

    # 現在のトラックを再生。一時停止時は途中から再生
    if btn3_prev == OFF and btn3_state == ON:
        if pause == False:
            player.play(track)
            display.fill(0)
            display.text("Play the current", 0, 10, 1)
            display.text("track", 0, 20, 1)
            display.show()
            time.sleep(1.5)
        else:
            player.resume()
            pause = False

    # 一時停止
    if btn4_prev == OFF and btn4_state == ON:
        pause = True
        player.pause()
        display.fill(0)
        display.text("Pause", 0, 10, 1)
        display.show()
        time.sleep(1.5)

    # リピートON／リピートOFF（Stop）
            
    if btn8_prev == OFF and btn8_state == ON:
        if repeat == False:
            player.repeat()
            repeat = True
            display.fill(0)
            display.text("Repeat ON", 0, 10, 1)
            display.show()
            time.sleep(1.5)
        else:
            player.stop()
            repeat = False
            display.fill(0)
            display.text("Repeat OFF (Stop)", 0, 10, 1)
            display.show()
            time.sleep(1.5)
            


    btn1_prev = btn1_state
    btn2_prev = btn2_state
    btn3_prev = btn3_state
    btn4_prev = btn4_state
    btn5_prev = btn5_state
    btn6_prev = btn6_state
    btn7_prev = btn7_state
    btn8_prev = btn8_state

    # 時刻の表示
    utc_time = time.localtime()
    jst_time = to_jst(utc_time)
    formatted_time = f"{jst_time[0]}年{jst_time[1]}月{jst_time[2]}日 {jst_time[3]:02d}時{jst_time[4]:02d}分{jst_time[5]:02d}秒"
    formatted_time2 = f"{jst_time[0]} {jst_time[1]:02d} {jst_time[2]:02d} {jst_time[3]:02d}:{jst_time[4]:02d}:{jst_time[5]:02d}"
    formatted_time3 = f"{jst_time[3]:02d}:{jst_time[4]:02d}:{jst_time[5]:02d}"
    print(f"{formatted_time}")

    # アラーム時刻と現在時刻を比較
    if formatted_time3 == alarm_time:
        display.fill(0)
        display.text("Alarm!", 0, 10, 1)
        display.show()
        player.play(0001)#()のなかのトラックの曲を再生　この場合は、1曲目
        time.sleep(90)# アラーム音を10秒間再生する
        player.stop()
        display.fill(0)  # ディスプレイをクリア
        display.show()

    display.fill(0)  # ディスプレイをクリア
    display.text(f"{formatted_time3}", 30, 0, 1)
    display.text(f"{formatted_time2}", 0, 10, 1)
    display.text("alarm  "+alarm_time,0,20,1)
    display.text("temperature:"+str(temperature), 0, 30, 1)
    display.show()
    display.show()
    time.sleep(1)
    


