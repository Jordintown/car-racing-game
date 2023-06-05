basic.showIcon(IconNames.Yes)
basic.pause(1000)
basic.forever(function () {
    if (input.temperature() <= 3) {
        basic.showLeds(`
            # . # . #
            # . # . #
            # . # . #
            . . . . .
            # . # . #
            `)
        basic.showLeds(`
            . # . # .
            # . # . #
            . # # # .
            # . # . #
            . # . # .
            `)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
