# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Task, Comment, Team
from access.models import Friends


@login_required(login_url='access:login')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        assignees = request.POST.getlist('assignee')

        task = Task(title=title, description=description,
                    status=status, created_by=request.user)

        team_id = request.POST.get('team_id', None)

        if team_id is not None:
            try:
                team = Team.objects.get(pk=team_id)
                task.team = team
            except Team.DoesNotExist:
                return redirect('access:home')

        task.save()

        if len(assignees) == 0:
            task.assigned_to.add(request.user)

        for assignee in assignees:
            task.assigned_to.add(User.objects.get(username=assignee))

        task.save()

        '''
        If request from team page, then redirect back to team
        '''
        if team_id is not None:
            return redirect('access:team_detail', team_id=team_id)

        return redirect('access:home')

    users = User.objects.all()
    friends = Friends.objects.get(pk=request.user.id) # added after 2nd update
    # members = friends.members.all() #testings # added after 2nd update
    # print(members) #testings # added after 2nd update

    return render(request, 'todo/create.html', {'users': users, "friends": friends,})


@login_required(login_url='access:login')
def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return redirect('access:home')

    team = task.team

    if team is None:
        ''' Check whether user can view details of another task '''
        if request.user != task.created_by and request.user not in task.assigned_to.all():
            messages.error(request, "You can't view this task")
            return redirect('access:home')
    else:
        if request.user not in team.members.all():
            messages.error(request, "You can't view this task")
            return redirect('access:home')

    users = User.objects.all()

    comments = Comment.objects.filter(task=task)

    friends = Friends.objects.get(pk=request.user.id) # added after 2nd update

    statuses = ['Planned', 'Ongoing', 'Done']

    return render(request, "todo/detail.html", {
        "id": task_id, "task": task,
        "users": users, "statuses": statuses,
        "comments": comments, "friends": friends,
    })


@login_required(login_url='access:login')
def edit(request):
    if request.method == 'POST':
        try:
            task = Task.objects.get(pk=request.POST.get("task_id"))
        except Task.DoesNotExist:
            messages.error(request, "Task not found")
            return redirect('access:home')

        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        assignees = request.POST.getlist('assignee')

        task.title = title
        task.description = description
        task.status = status

        for assignee in assignees:
            task.assigned_to.add(User.objects.get(username=assignee))

        task.save()

        return redirect('access:home')

    return redirect('access:home')


@login_required(login_url='access:login')
def delete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        messages.error(request, "Task doesn't exist")
        return redirect('access:home')

    if task:
        if request.user == task.created_by:
            task.delete()
        else:
            messages.error(request, "Only task creator can delete task.")
    else:
        messages.error(request, "Task doesn't exist")

    return redirect('access:home')


@login_required()
def post_comment(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        messages.error(request, "Task doesn't exist")
        return redirect('access:home')

    if request.method == 'POST':
        body = request.POST.get("comment")
        team_id = request.POST.get("team_id", None)

        flag = False

        # If team is none, check if user created/assigned task
        if team_id is None:
            if request.user == task.created_by or request.user in task.assigned_to.all():
                flag = True
            else:
                messages.error(request, "You can't comment on this task")
        else:
            team = Team.objects.get(pk=team_id)
            # Check if user is present in team
            if request.user in team.members.all():
                flag = True
            else:
                messages.error(
                    request, "Only team members can comment on this task")

        if flag:
            comment = Comment(body=body, author=request.user, task=task)
            comment.save()

        # print(body)

    return redirect('tasks:detail', task_id=task_id)


# ----------------------------------------- After 2nd Update -------------------------------------------------------

@login_required(login_url='access:login')
def complete_archive(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        messages.error(request, "Task doesn't exist")
        return redirect('access:home')

    if task:
        # if request.user == task.created_by or request.user in task.assigned_to.all():
        if request.user == task.created_by:
            task.complete_archive = 'True'
            task.save()
        else:
            messages.error(request, "Only task creator can archive task.")
    else:
        messages.error(request, "Task doesn't exist")

    return redirect('access:home')


@login_required(login_url='access:login')
def not_complete_archive(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        messages.error(request, "Task doesn't exist")
        return redirect('access:home')

    if task:
        # if request.user == task.created_by or request.user in task.assigned_to.all():
        if request.user == task.created_by:
            task.complete_archive = 'False'
            task.save()
        else:
            messages.error(request, "Only task creator can restore task.")
    else:
        messages.error(request, "Task doesn't exist")

    return redirect('access:complete_archive_all')