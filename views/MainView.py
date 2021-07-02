import controllers.PageHelper as PageHelper


class MainView:

    @staticmethod
    def show(dir_path):
        PageHelper.PageHelper.menu(dir_path)


