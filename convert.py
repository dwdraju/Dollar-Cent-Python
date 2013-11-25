import simplegui
value = 0.0
def c_units(val, name):
    result = str(val) + " " + name
    if val >1:
        result = result + "s"
    return result

def convert(val):
    dollars = int (val)
    cents = round ( 100 * (val - dollars))
    dollars_string = c_units(dollars, "dollar")
    cents_string = c_units (cents, "cent")
    if	dollars == 0 and cents == 0:
                return "Broke"
    elif dollars == 0:
                return cents_string
    elif cents == 0:
         return dollars_string
    else:
          return dollars_string + " and " + cents_string
        
def draw(canvas):
    canvas.draw_text(convert(value), [100, 100], 30, "blue")
    
def input_handler(text):
    global value
    value = float(text)
    

frame = simplegui.create_frame("Converter", 400, 300)



frame.set_draw_handler(draw)
frame.add_input("Enter a value", input_handler, 100)
frame.start()
