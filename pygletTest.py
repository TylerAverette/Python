import pyglet

game_window = pyglet.window.Window()

@game_window.event
def on_draw():
    game_window.clear()

def update():
    pass

if __name__ == '__main__':
    pyglet.clock.schedule.interval(update, 1/60.0)
    pyglet.app.run()
