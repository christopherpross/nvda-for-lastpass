import appModuleHandler
import NVDAObjects
import controlTypes



class AppModule(appModuleHandler.AppModule):
    def event_NVDAObject_init(self, obj):
        if (obj.role == controlTypes.ROLE_RADIOBUTTON):

            # the object is a radiobutton
            if (obj.childCount != 0):
                nameresult = ""
                for child in obj.children:
                    if (child.role == controlTypes.ROLE_STATICTEXT):
                        nameresult = child.name
                obj.name = nameresult

