# Assignment-1-Ch-2-and-Ch-3-Activities
Assignment 1: Chapters 2 and 3 Activities

What I did for activity 2.01:

After creating code ran in PyCharm the following line by line:

python manage.py makemigrations

python manage.py migrate

python manage.py shell

In Python shell ran the following line by line:

from projectp.models import Project, Task                    

project_name = Project.objects.create(name='Juggler project')  

Task.objects.create(task_name='create Juggler project',description='make Django startproject',project_name=project_name,time_for_completion='5 minutes',completion_status='Completed')  

Task.objects.create(task_name='create projectp myapp',description='make Django myapp',project_name=project_name,time_for_completion='5 minutes',completion_status='Completed')       

Task.objects.create(task_name='create Classes',description='Classes Project and Task',project_name=project_name,time_for_completion='20 minutes',completion_status='Completed') 

Task.objects.create(task_name='create Tasks',description='Creating tasks assocaited with Project',project_name=project_name,time_for_completion='10 minutes',completion_status='Completed')  

Task.objects.create(task_name='create query list of tasks',description='query tasks and obtain status',project_name=project_name,time_for_completion='10 minutes',completion_status='Pending') 

Results listing all the tasks in the project:
>>> project_name.task_set.all()                        
<QuerySet [<Task: create Juggler project>, <Task: create projectp myapp>, <Task: create Classes>, <Task: create Tasks>, <Task: Query list of tasks>]>
