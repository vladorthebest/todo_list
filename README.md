# To Do List


The Web-application has the ability to register users. For further saving and editing tasks. With this application, the user will be able to monitor and control the execution of their tasks.

## Work with tasks

#### Tools for work with tasks:
- TaskList(ListView) - List with all users's tasks (Main page)
- TaskCreate(CreateView) - Class for creating new tasks
- TaskUpdate(UpdateView) - Class for updating task
- TaskDelete(DeleteView) - Class for deleting task
- convert_task(request, pk) - Function to convert task status
 
#### Links for work with tasks:
- / - Main page with all users's tasks 
- create_task/ - Page for creating new tasks
- delete_task/int:pk/ - Page for deleting task
- update_task/int:pk/ - Page for updating task
- convert_task/int:pk/ - Link to convert task status


## Work with users

#### Tools for work with user:
- RegisterPage(FormView) - New User Registration
- UserCreationForm - Form for Registration
- CustomLoginView(LoginView) - Login to an existing user account
- LogoutView - Logout to an existing user account
- LoginRequiredMixin - User Authorization Check
 
#### Links for work with users:
- register/ - New User Registration
- login/ - Login to an existing user account
- logout/ - Logout to an existing user account


## Tools used in the project:
- Python
- Django
- HTML
- CSS
- GIT

### IDE:
Visual Studio Code


