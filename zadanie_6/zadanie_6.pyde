class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self,x,y):
        fill(280,10,300) # wypadałoby zapamiętać poprzedni kolor i przywrócić go po narysowaniu, bo wszystkie rzeczy rysowane po obiekcie tej klasy będą w tym kolorze
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
   
    
            
def setup():
    size(500, 500)
    background(250,200,4)
    malyKwadrat = Kwadrat(15.0)
    malyKwadrat.sketch(100,100)
    duzyKwadrat = Kwadrat(150.0)
    duzyKwadrat.sketch(200,5)
    malyKwadrat.sketch(5,200) 
    malyPasiastyKwadrat = PasiastyKwadrat(50.0) 
    malyPasiastyKwadrat.sketchPasiasty(200, 300, 5) 
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) 
    duzyPasiastyKwadrat  = PasiastyKwadrat(100.0)
    duzyPasiastyKwadrat.sketchPasiasty(200, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300)
    duzyKolorowyKwadrat= KolorowyKwadrat (100.0)
    duzyKolorowyKwadrat.sketchKolorowy(10,250)
    malyKolorowyKwadrat= KolorowyKwadrat (25.0)
    malyKolorowyKwadrat.sketchKolorowy (250,100)
    
#1,75pkt
