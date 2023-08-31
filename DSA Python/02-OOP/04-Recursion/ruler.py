def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for i in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))

def draw_interval(center_length):
    if center_length >= 1:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

# To draw a 2-inch ruler with major tick length of 4
draw_ruler(2, 5)
