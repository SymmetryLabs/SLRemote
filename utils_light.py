from pythonosc import osc_message_builder
from pythonosc import udp_client

#client = udp_client.SimpleUDPClient("192.168.5.5", 3030)
client = udp_client.SimpleUDPClient("0.0.0.0", 3030)
def send_osc(route, message):
    client.send_message(route, message)

def turn_on(isOn='On'):

    if isOn == 'On':
        
        print(isOn)
        send_osc(output_on_osc_route, 1)
# send osc to turn on lights
    else: 
        # turn off
        print(isOn)
        send_osc(output_on_osc_route, 0)
    return
def change_pattern(pattern):
    pattern_index = next(i for i, pat in enumerate(patterns_full) if pattern in pat)
    print('pat index:', pattern_index)
    send_osc(channel_1_pattern_osc_route, pattern_index)
    return

def change_color(color):
    send_osc(color_osc_route, color)
    return
def change_speed(speed):
    send_osc(speed_osc_route, speed)
    return
def change_brightness(brightness):
    send_osc(bright_osc_route, brightness)
    return

