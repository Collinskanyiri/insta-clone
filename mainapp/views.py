from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,CreateNewPostForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from mainapp.models import *
from django.shortcuts import get_object_or_404
from django.urls import reverse
import cloudinary
import cloudinary.uploader
import cloudinary.api


