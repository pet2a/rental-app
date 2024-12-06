

from django.contrib import admin
from django.urls import path
from CribDashApp import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('propertysingle/', views.propertysingle, name='propertysingle'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('sunshine/', views.sunshine, name='sunshine'),
    path('yellowstone/', views.yellowstone, name='yellowstone'),
    path('orangehouse/', views.orangehouse, name='orangehouse'),
    path('contactagent/', views.contact_agent, name='contact_agent'),
    path('landlords/', views.landlords_dashboard, name='landlords_dashboard'),
    path('search/', views.search_results, name='search_results'),

]
