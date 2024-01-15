from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, Theme
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Using this view with "home_logged_in" because "l" breaks page when logged out.
def home(request):
    not_form = 'not_form'
    context = 'Home'
    return render(request, 'home.html', { 'not_form' : not_form, 'context' : context })   

@login_required
def home_logged_in(request):
    not_form = 'not_form'
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    # Used for rendering "Mode" button. Need loop to render button that can be updated with db object id.
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'home_logged_in.html', { 'groups' : groups, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })


@login_required
def groups(request):
    not_form = 'not_form'
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Personal'
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'groups.html', { 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })

# SECTION MAIN: Link Share
@login_required
def library_index(request):
    not_form = 'not_form'
    games = Item.objects.filter(user=request.user, wishlist_user=False).order_by('title')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Link'
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })

# SECTION MAIN: Sites and Software Tools Reference
@login_required
def library_index_01(request):
    not_form = 'not_form'
    items = Item.objects.filter(type='Tool', wishlist_user=False).order_by('label')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Sites'
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'items' : items, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })

@login_required
def library_index_02(request):
    not_form = 'not_form'
    games = Item.objects.filter(hoth_group=True, wishlist_user=False).order_by('title')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Hoth'
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })

@login_required
def library_index_03(request):
    not_form = 'not_form'
    games = Item.objects.filter(gundam_group=True, wishlist_user=False).order_by('title')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Gundam'
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes , not_form : 'not_form'})

# SECTION LISTS: Personal Items
@login_required
def library_index(request):
    not_form = 'not_form'
    games = Item.objects.filter(user=request.user, wishlist_user=False).order_by('title')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = ['Personal', 'Personal']
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })
    
@login_required
def event(request):
    not_form = 'not_form'
    games = Item.objects.filter(event=True).order_by('title')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = ['Personal', 'Event']
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes , not_form : 'not_form'})

@login_required
def wishlist_user(request):
    not_form = 'not_form'
    games = Item.objects.filter(wishlist_user=True, user=request.user).order_by('title')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = ['Personal', 'Wishlist User']
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes , not_form : 'not_form'})


# Game
class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['label','decription', 'image', 'type', 'note', 'color', 'link', 'event', 'wishlist_user', ]
  
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['label','decription', 'image', 'type', 'note', 'color', 'link', 'event', 'wishlist_user', ]

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/home_logged_in'


# Theme
class ThemeCreate(LoginRequiredMixin, CreateView):
    model = Theme
    fields = ['color']
  
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ThemeUpdate(LoginRequiredMixin, UpdateView):
    model = Theme
    fields = ['color']

class ThemeDelete(LoginRequiredMixin, DeleteView):
    model = Theme
    success_url = '/home_logged_in/'


# Signup
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('library/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)   


# Error 404
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)