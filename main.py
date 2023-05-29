playerCar: game.LedSprite = None
gameOn = False
car0: game.LedSprite = None
car1: game.LedSprite = None
car2: game.LedSprite = None
car3: game.LedSprite = None
car4: game.LedSprite = None

def on_button_pressed_a():
    if playerCar.get(LedSpriteProperty.X) > 0:
        playerCar.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if playerCar.get(LedSpriteProperty.X) < 4:
        playerCar.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def controlCar(car: game.LedSprite):
    global gameOn
    basic.pause(randint(0, 5000))
    while gameOn == True:
        if car.get(LedSpriteProperty.Y) == 4:
            if playerCar.is_touching(car):
                gameOn = False
            else:
                game.set_score(game.score() + 1)
                car.set(LedSpriteProperty.Y, 0)
                basic.pause(randint(0, 5000))
        else:
            car.change(LedSpriteProperty.Y, 1)
            basic.pause(500)

def on_forever():
    global playerCar, gameOn
    game.set_score(0)
    playerCar = game.create_sprite(2, 4)
    gameOn = True
    while gameOn == True:
        basic.pause(100)
    game.game_over()
basic.forever(on_forever)

def on_forever2():
    global car0
    basic.pause(100)
    if gameOn == True:
        car0 = game.create_sprite(0, 0)
        controlCar(car0)
basic.forever(on_forever2)

def on_forever3():
    global car1
    basic.pause(100)
    if gameOn == True:
        car1 = game.create_sprite(1, 0)
        controlCar(car1)
basic.forever(on_forever3)

def on_forever4():
    global car2
    basic.pause(100)
    if gameOn == True:
        car2 = game.create_sprite(2, 0)
        controlCar(car2)
basic.forever(on_forever4)

def on_forever5():
    global car3
    basic.pause(100)
    if gameOn == True:
        car3 = game.create_sprite(3, 0)
        controlCar(car3)
basic.forever(on_forever5)

def on_forever6():
    global car4
    basic.pause(100)
    if gameOn == True:
        car4 = game.create_sprite(4, 0)
        controlCar(car4)
basic.forever(on_forever6)
