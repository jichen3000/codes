import sublime, sublime_plugin
from pprint import pprint

from .core import jh_util

SETTINGS = None


def plugin_loaded():
    global SETTINGS
    SETTINGS = sublime.load_settings('JavaHelper.sublime-settings')

def get_setting(the_key, default_value=None):
    if default_value:
        return SETTINGS.get(the_key, default_value)
    return SETTINGS.get(the_key)

# class JavaHelperCommand(sublime_plugin.WindowCommand):
class JavaHelperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # check file type should be java
        # sub_project_paths = self.view.window().project_data()
        sub_project_paths = jh_util.extract_path_list(
            self.view.window().project_data()['folders'])
        current_sub_project_path = jh_util.match_path(
            self.view.file_name(),sub_project_paths)
        print(current_sub_project_path)
        print("ok")




