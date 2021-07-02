import views.MainView as MainView
import os

while(True):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    MainView.MainView.show(dir_path)