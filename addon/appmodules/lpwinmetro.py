import appModuleHandler
import NVDAObjects
import controlTypes
import NVDAObjects.UIA



class AppModule(appModuleHandler.AppModule):
    def event_NVDAObject_init(self, obj : NVDAObjects.NVDAObject):
        if (obj.role == controlTypes.ROLE_RADIOBUTTON) or (obj.role == controlTypes.ROLE_BUTTON):
            # the object is a radiobutton or a button, let's extract the children labels
            if (obj.childCount != 0):
                nameresult = ""
                for child in obj.children:
                    if (child.role == controlTypes.ROLE_STATICTEXT):
                        nameresult = child.name
                obj.name = nameresult
        if isinstance(obj, NVDAObjects.UIA.UIA):
            # well, try to give the add button a label
            obj.__class__ = NVDAObjects.UIA.UIA
            if (obj.UIAElement.CurrentAutomationId =="sideAddButton"):
                # the add button has this automationId at the moment
                obj.name = "add"



