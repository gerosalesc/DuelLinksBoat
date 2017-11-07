switchApp("BlueStacks")

smallers = [Pattern("1510078948834.png").similar(0.45), Pattern("1510078971047.png").similar(0.44), Pattern("1510079026520.png").similar(0.44)]
mids = [Pattern("1510021627396.png").similar(0.46), Pattern("1510079057005.png").similar(0.45)]

bigs = [ Pattern("1510021808266.png").similar(0.45) ,  Pattern("1510079174148.png").similar(0.45)]

# TODO: small = 

def find_op_match(op_list):
   for op in op_list:
       exist_op = exists(op)
       if exist_op:
           return op

gonnaclick = find_op_match(bigs+mids+smallers)
print(gonnaclick)
click(gonnaclick) # Focus window problem in OSX
click(gonnaclick)


next_dialog = "1510022177979.png"
# Go through dialog
while True:
    try:
        wait(next_dialog, 10)
        click(next_dialog)
    except:
        break
    
# Continue to auto duel
auto_duel = "1510022792534.png"
wait(auto_duel, 10)
click(auto_duel)

