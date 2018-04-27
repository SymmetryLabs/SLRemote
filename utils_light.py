from pythonosc import osc_message_builder
from pythonosc import udp_client

output_on_osc_route = '/lx/output/enabled'
channel_1_pattern_osc_route = '/lx/channel/1/activePattern'
color_osc_route = '/lx/palette/color/hue'
speed_osc_route = '/lx/engine/speed'
blur_osc_route = '/lx/channel/1/effect/1/amount/'
bright_osc_route = '/lx/output/brightness'

patterns_full = ['AskewPlanes', 'Balance', 'Ball', 'BassPod', 'Blank', 'Bubbles', 'CrossSections', 'CubeEQ', 
                 'CubeFlash', 'Noise', 'Palette', 'Pong', 'Rings', 'ShiftingPlane', 'SoundParticles', 'SpaceTime',
                'Spheres', 'StripPlay', 'Swarm', 'Swim', 'TelevisionStatic', 'Traktor', 'ViolinWave']

patterns_lower = [x.lower() for x in patterns_full]
color_labels_encoding = ['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'magenta']
speed_labels = ['slow', 'medium', 'fast']
effect_labels = ['low', 'medium', 'high']
brightness_labels = ['off', 'dim', 'down', 'half', 'up', 'full', 'bright']

bright_unencode = [0.0, 0.3, 0.3, 0.5, 0.7, 1.0, 1.0]
speed_unencode = [0.2, 0.5, 0.8]
color_unencode = [0.0, 0.08, 0.15, 0.35, 0.48, 0.67, 0.76, 0.84]
effect_unencode = [0.0, 0.3, 0.6, 0.9]

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

