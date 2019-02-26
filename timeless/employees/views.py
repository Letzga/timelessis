"""Employees views module.
@todo #57:30min Continue implementing List to enable sorting and filtering
 for every column. For this, probably there will be a need to create a new
 generic view that all other List views will extend. This generic view should
 use GenericFilter implemented in #317.
"""
from flask import Blueprint
from timeless.employees.forms import EmployeeForm
from timeless import views
from timeless.employees.models import Employee

bp = Blueprint("employee", __name__, url_prefix="/employees")


class Create(views.CreateView):
    """Create employee"""
    template_name = "employees/create_edit.html"
    form_class = EmployeeForm
    model = Employee
    success_view_name = "employee.list"

    def get(self, **kwargs):
        context = self.get_context(action="create")
        return self.render_to_response(context)


"""
@todo #348:30min Continue implementing Edit view when generic view UpdateView
 would be implemented. Template "employees/create_edit.html" has already
 provided, so uncomment and modify. Write IT to verify behaviour.
"""
# class Edit(views.UpdateView):
#     """Update employee"""
#     template_name = "employees/create_edit.html"
#     form_class  = EmployeeForm
#     model = Employee


class Delete(views.DeleteView):
    """Delete employee"""
    model = Employee
    success_view_name = "employee.list"
    """
    @todo #348:30min Delete "template_name" from Delete 
     after #312 will be pulled. Uncomment and test IT test. 
     "template_name" is using now due to current implementation of
     views.DeleteView.
    """
    template_name = "employees/list.html"


class List(views.ListView):
    """List all employees"""
    model = Employee
    success_view_name = "employee.list"
    """
    @todo #348:15min Delete template_name from List after #312 will be pulled 
     to the master branch. "template_name" is using now due to current 
     implementation of views.DeleteView.
    """
    template_name = "employees/list.html"


List.register(bp, "/")
Create.register(bp, "/create")
# Edit.register(bp, "/edit/<int:id>")
Delete.register(bp, "/<int:id>/delete")
