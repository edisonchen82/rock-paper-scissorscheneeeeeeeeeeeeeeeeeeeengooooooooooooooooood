def doSomething(布尔值: bool):
    pass

def on_forever():
    basic.show_icon(IconNames.TORTOISE)
    basic.pause(10)
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        . . . . .
                # # # # #
                . . # # .
                . # . . .
                # # # # #
    """)
    basic.show_number(8)
    basic.clear_screen()
    basic.show_arrow(ArrowNames.NORTH_EAST)
basic.forever(on_forever)
