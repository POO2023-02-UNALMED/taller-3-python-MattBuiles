class Control:
  def __init__(self):
    self.tv=self
  def turnOn(self): self.tv.turnOn()
  def turnOff(self): self.tv.turnOff()
  def canalUp(self): self.tv.canalUp()
  def canalDown(self): self.tv.canalDown()
  def volumenUp(self): self.tv.volumenUp()
  def volumenDown(self): self.tv.volumenDown()
  def setCanal(self,value): self.tv.setCanal(value)
  def setVolumen(self,value): self.tv.setVolumen(value)

  def enlazar(self,tele):
    self.tv=tele
    #tele.control=self
  def getTv(self): return self.tv
  def setTv(self,value): self.tv=value