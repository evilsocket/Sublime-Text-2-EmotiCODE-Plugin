import sublime, sublime_plugin
import subprocess
import webbrowser

def PerformSearch(text):
  if len(text):
    url = 'http://www.emoticode.net/search/' +  text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class EmoticodeSearchSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for selection in self.view.sel():
      if selection.empty():
          text = self.view.word(selection)

      text = self.view.substr(selection).strip()

      PerformSearch(text)

class EmoticodeSearchInputCommand(sublime_plugin.WindowCommand):
    def run(self):
      self.window.show_input_panel('Search EmotiCODE for', '', self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
      PerformSearch(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass