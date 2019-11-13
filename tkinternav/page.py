from tkinter import Frame


class Page(Frame):
    """Page boilerplate"""

    def __init__(self, parent, name=None):
        Frame.__init__(self, parent)

        self.grid(row=0, column=0, sticky='nsew')

        self.__name = name
        self.__parent = parent
        self.__root = parent.root

    @property
    def name(self):
        """Name of the page

        Used as ID
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def parent(self):
        """Root frame - responsible for container grid
        """
        return self.__parent

    @property
    def app_state(self):
        """Global app state"""
        return self.parent.root.app_state

    def update_state(self):
        """Do not override

        -----

        Updates the global app state"""
        self.__root.app_state = self.app_state

    def navigate(self, name):
        """Do not override

        -----

        Navigate to another page

        :param name: Name (ID) of the page
        """
        self.parent.root.show_page(name)

    def page_did_mount(self):
        """Is called when the page is shown"""
        pass

    def page_did_unmount(self):
        """Is called when the page is hidden"""
        pass
