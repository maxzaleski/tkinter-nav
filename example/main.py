import tkinter as tk

from tknav import Nav, Page


class App(Nav):

    def __init__(self):
        Nav.__init__(self, [PageOne, PageTwo])
        self.geometry('300x300')
        self.app_state = {'previous_page': None}
        self.show_page('page_one')


class PageOne(Page):

    def __init__(self, parent: tk.Frame, root: Nav):
        Page.__init__(self, parent, root)
        self.name = 'page_one'

        tk.Label(
            self,
            text="Page One"
        ).pack()

        button = tk.Button(
            self,
            text='Navigation to Page Two',
            command=lambda: root.show_page('page_two'),
        )
        button.pack()

    def page_did_mount(self) -> None:
        print('State on mount:', self.app_state)
        print('Page one did mount')

    def page_did_unmount(self) -> None:
        self.set_state({'previous_page': 'Page One'})
        print('Page one did unmount')


class PageTwo(Page):

    def __init__(self, parent: tk.Frame, root: Nav):
        Page.__init__(self, parent, root)
        self.name = 'page_two'

        tk.Label(
            self,
            text="Page Two"
        ).pack()

        tk.Button(
            self,
            text="Navigation to Page One",
            command=lambda: root.show_page('page_one')
        ).pack()

    def page_did_mount(self) -> None:
        print('State on mount:', self.app_state)
        print('Page two did mount')

    def page_did_unmount(self) -> None:
        self.set_state({'previous_page': 'Page two'})
        print('Page two did unmount')


if __name__ == '__main__':
    App().mainloop()
