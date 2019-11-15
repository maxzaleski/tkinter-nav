import tkinter as tk
import tkinter_nav as tknav

class App(tknav.Wrapper):

    def __init__(self):
        tknav.Wrapper.__init__(
            self,
            pages=[PageOne, PageTwo],
            start_state={'previous_page': None}
        )
        self.geometry('300x300')
        self.show_page('page_one')


class PageOne(tknav.Page):

    def __init__(self, parent):
        tknav.Page.__init__(self, parent, 'page_one')

        tk.Label(
            self,
            text='Page One'
        ).pack()

        tk.Button(
            self,
            text='Navigate to Page Two',
            command=lambda: self.__navigate(),
        ).pack()

    def page_did_mount(self) -> None:
        print('Page one did mount')
        print('State on mount:', self.app_state)

    def page_did_unmount(self) -> None:
        self.app_state['previous_page'] = 'Page One'
        print('Page one did unmount')

    def __navigate(self):
        print('navigating to page two')
        self.navigate('page_two')


class PageTwo(tknav.Page):

    def __init__(self, parent):
        tknav.Page.__init__(self, parent, 'page_two')

        tk.Label(
            self,
            text='Page Two'
        ).pack()

        tk.Button(
            self,
            text='Navigate to Page One',
            command=lambda: self.__navigate(),
        ).pack()

    def page_did_mount(self) -> None:
        print('Page two did mount')
        print('State on mount:', self.app_state)

    def page_did_unmount(self) -> None:
        self.app_state['previous_page'] = 'Page Two'
        print('Page two did unmount')

    def __navigate(self):
        print('navigating to page one')
        self.navigate('page_one')


if __name__ == '__main__':
    App().mainloop()
