from .Menuitem import Menuitem
class ItemDescription:
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description", '') or ''
        canTry = True
        index = 0
        while canTry:
            try:
                obj = Menuitem(**self.Menuitems.get(str(index)))
                index += 1
                self.menuItems.Append(obj)
            except:
                canTry = False
        self.secondaryDescription = kwargs.get("SecondaryDescription", '') or ''
