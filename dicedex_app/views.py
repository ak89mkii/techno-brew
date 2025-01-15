from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, Link, Theme
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm


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

# SECTION MAIN: Link Share (Link)
@login_required
def library_index(request):
    not_form = 'not_form'
    links = Link.objects.order_by('description')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Link'
    switches = Theme.objects.filter(user=request.user).order_by('color')
    # References the last Theme entry to change the "background" color id.
    themes = Theme.objects.filter(user=request.user).order_by('color').last()
    return render(request, 'library/index.html', { 'links' : links, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })

# SECTION MAIN: Sites and Software Tools Reference (Item)
@login_required
def library_index_01(request):
    not_form = 'not_form'
    items = Item.objects.filter(type='Tool').order_by('label')
    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    context = 'Tools'
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

# SECTION MAIN: TDI Demo "Membership Page"
@login_required
# def library_demo(request):
#     not_form = 'not_form'
#     return render(request, 'library/demo.html', { 'not_form' : not_form })   

def library_demo_search(request):
    results = None
    form = SearchForm(request.GET or None)  # Use GET for the search form

    if form.is_valid():
        search_type = form.cleaned_data['search_type']
        query = form.cleaned_data['query']

        # Filter the results based on search type
        if search_type == 'label':
            results = Item.objects.filter(label__icontains=query)
        elif search_type == 'type':
            results = Item.objects.filter(type__icontains=query)
        elif search_type == 'color':
            results = Item.objects.filter(color__icontains=query)

    return render(request, 'library/demo.html', {'form': form, 'results': results})

# # SECTION LISTS: Personal Items
# @login_required
# def library_index(request):
#     not_form = 'not_form'
#     games = Item.objects.filter(user=request.user, wishlist_user=False).order_by('title')
#     l = request.user.groups.values_list('name',flat = True)
#     groups = list(l)
#     context = ['Personal', 'Personal']
#     switches = Theme.objects.filter(user=request.user).order_by('color')
#     # References the last Theme entry to change the "background" color id.
#     themes = Theme.objects.filter(user=request.user).order_by('color').last()
#     return render(request, 'library/index.html', { 'games' : games, 'groups' : groups, 'context' : context, 'switches' : switches, 'themes' : themes, not_form : 'not_form' })
    
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


# Item
class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['label','description', 'image', 'type', 'note', 'color', 'link', 'favorited',  ]
    success_url = '/library_01'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['label','description', 'image', 'type', 'note', 'color', 'link', 'favorited', ]
    success_url = '/library_01'

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/library_01'


# Link
class LinkCreate(LoginRequiredMixin, CreateView):
    model = Link
    fields = ['description', 'color', 'link',  ]
    success_url = '/library'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class LinkUpdate(LoginRequiredMixin, UpdateView):
    model = Link
    fields = ['description', 'color', 'link',  ]
    success_url = '/library'

class LinkDelete(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = '/library'


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