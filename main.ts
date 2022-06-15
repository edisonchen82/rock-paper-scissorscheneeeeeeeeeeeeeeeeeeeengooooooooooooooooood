function doSomething(布尔值: boolean) {
    
}

basic.forever(function on_forever() {
    basic.showIcon(IconNames.Tortoise)
    basic.pause(10)
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . . . . .
                # # # # #
                . . # # .
                . # . . .
                # # # # #
    `)
    basic.showNumber(8)
    basic.clearScreen()
    basic.showArrow(ArrowNames.NorthEast)
})
