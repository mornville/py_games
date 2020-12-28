from ursina import *

def update():
    print('test')
app = Ursina()

test_square = Entity(model = 'circle', color=color.red)

app.run()
