from kivy.app import App
import kivy.uix.boxlayout as Box
import kivy.uix.textinput as Text
import kivy.uix.label as Label
import kivy.uix.button as butt

class MyApp(App):
	def build(self):
		self.boxLayout = Box.BoxLayout(orientation="vertical")
		self.button = butt.Button(text="Origem")
		self.button.bind(on_press=self.display)
		self.boxLayout.add_widget(self.button)
		return self.boxLayout
	
	def display(self, btn):
		print("hello")
		
if __name__ =="__main__":
	MyApp().run()
		