import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.WindowCommand):
    def run(self):
        # self.view.insert(edit, 0, "Hello, World!")
        # print(self.view.file_name(), "ok")
        # obj = self.view.window
        obj = self.window
        print(obj)
        print(dir(obj))
        print(obj.project_file_name())
        print("ok")



