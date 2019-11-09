from tkinter import Tk, Frame
from typing import List


class EmptyPageList(Exception):
    """Exception when a page is not found"""

    def __init__(self):
        message = 'Page list must not be empty'
        super(EmptyPageList, self).__init__(message)


class PageNotFound(Exception):
    """Exception when a page is not found"""

    def __init__(self):
        message = 'No page with that name was found'
        super(PageNotFound, self).__init__(message)


class Page(Frame):
    """Page boilerplate"""

    name: str

    def __init__(self, parent: Frame, root: Tk):
        Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")

        self.root = root
        self.app_state = root.app_state

    def set_state(self, new_state={}):
        """Updates the states"""

        self.root.app_state = new_state

    def show(self, state) -> None:
        """Show the page"""

        self.app_state = state

        self.tkraise()
        self.page_did_mount()

    def page_did_mount(self) -> None:
        """This function will run as soon as the page is shown.

        Similar to React's componentDidMount()
        """
        pass

    def page_did_unmount(self) -> None:
        """This function will run as soon as the page is hidden.

        Similar to React's componentDidUnmount()
        """
        pass


class Container(Page):
    """Container which will wrap the pages"""

    def __init__(self, root: Tk):
        Page.__init__(self, parent=None, root=root)

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class Nav(Tk):
    """Navigation wrapper for Tkinter"""

    app_state = {}

    __pages = {}
    __current_page: Page = None

    def __init__(self, pages: List):
        Tk.__init__(self)

        self.container = Container(self)

        self.__register_pages(pages)

    def show_page(self, name: str) -> None:
        """This method will display the requested page

        Args:
            name: Name of the page to be displayed

        Raises:
            PageNotFound
        """

        page = self.__pages[name]
        if page:
            if self.__current_page:
                self.__current_page.page_did_unmount()

            self.__current_page = page
            page.show(self.app_state)
        else:
            raise PageNotFound()

    def __register_pages(self, pages: List):
        """Registers pages to the application

        Args:
            pages: List containing the page classes

        Raises:
            EmptyPageList
        """

        if len(pages) == 0:
            raise EmptyPageList()

        for P in pages:
            page = P(parent=self.container, root=self)
            name = page.name or P.__name__
            self.__pages[name] = page
