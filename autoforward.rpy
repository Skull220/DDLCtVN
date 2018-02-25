init python:
      
    def getPosition(posHash):
        if posHash == [t11]:
            return "t11"
        elif posHash == [f11]:
            return "f11"
            
        elif posHash == [t21]:
            return "t21"
        elif posHash == [t22]:
            return "t22"
        elif posHash == [f21]:
            return "f21"
        elif posHash == [f22]:
            return "f22"
            
        elif posHash == [t31]:
            return "t31"
        elif posHash == [t32]:
            return "t32"
        elif posHash == [t33]:
            return "t33"
        elif posHash == [f31]:
            return "f31"
        elif posHash == [f32]:
            return "f32"
        elif posHash == [f33]:
            return "f33"
            
        elif posHash == [t41]:
            return "t41"
        elif posHash == [t42]:
            return "t42"
        elif posHash == [t43]:
            return "t43"
        elif posHash == [t44]:
            return "t44"
        elif posHash == [f41]:
            return "f41"
        elif posHash == [f42]:
            return "f42"
        elif posHash == [f43]:
            return "f43"
        elif posHash == [f44]:
            return "f44"

    def auto_focus(event, interact=True, *whoIsThis, **kwargs):
        if event == "begin":
            initial_pos = renpy.get_at_list(whoIsThis)
            renpy.show(whoIsThis, at_list=[wherePos[getPosition(initial_pos)]], zorder=3)
        if event == "end":
            initial_pos = renpy.get_at_list(whoIsThis)
            renpy.show(whoIsThis, at_list=[wherePos[getPosition(initial_pos)]], zorder=1)

    def sayori_focus(event, interact=True, **kwargs):
        if renpy.get_at_list("sayori"):
            auto_focus(event, interact, "sayori", **kwargs)
            
    def yuri_focus(event, interact=True, **kwargs):
        if renpy.get_at_list("yuri"):
            auto_focus(event, interact, "yuri", **kwargs)
            
    def natsuki_focus(event, interact=True, **kwargs):
        if renpy.get_at_list("natsuki"):
            auto_focus(event, interact, "natsuki", **kwargs)
            
    def monika_focus(event, interact=True, **kwargs):
        if renpy.get_at_list("monika"):
            auto_focus(event, interact, "monika", **kwargs)

label groupStart():
    #Applying automatic leans towards the front...
    $ s.display_args["callback"] = sayori_focus
    $ y.display_args["callback"] = yuri_focus
    $ n.display_args["callback"] = natsuki_focus
    $ m.display_args["callback"] = monika_focus
    python:
        wherePos = {
            "t11" : f11,
            "f11" : t11,
            
            "t21" : f21,
            "t22" : f22,
            "f21" : t21,
            "f22" : t22,
            
            "t31" : f31,
            "t32" : f32,
            "t33" : f33,
            "f31" : t31,
            "f32" : t32,
            "f33" : t33,
            
            "t41" : f41,
            "t42" : f42,
            "t43" : f43,
            "t44" : f44,
            "f41" : t41,
            "f42" : t42,
            "f43" : t43,
            "f44" : t44
        }
    return
    
label groupClear():
    #Applying automatic leans towards the front...
    $ s.display_args["callback"] = None
    $ y.display_args["callback"] = None
    $ n.display_args["callback"] = None
    $ m.display_args["callback"] = None
    return