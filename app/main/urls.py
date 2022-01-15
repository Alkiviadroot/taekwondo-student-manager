from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
login='/login'

urlpatterns = [
    path('', login_required(HomeView.as_view(),login_url=login), name='home'),
    
    #intital form
    path('add', login_required(MathitisForm.as_view(),login_url=login), name='mathitis_add'),
    path('add/<int:pk>/gonios', login_required(GoniosForm.as_view(),login_url=login), name='gonios_add'),
    path('add/<int:pk>/provlimata',login_required(ProvlimataForm.as_view(),login_url=login), name='provlimata_add'),
    path('add/<int:pk>/paralavi',login_required(ParalaviForm.as_view(),login_url=login), name='paralavi_add'),
    path('add/<int:pk>/adies', login_required(AdiesForm.as_view(),login_url=login), name='adies_add'),

    # exetasi
    path('<int:pk>/exetasi', login_required(ProgressForm.as_view(),login_url=login), name='progress'),
    path('<int:pk>', login_required(MathitisDetailView.as_view(),login_url=login), name='mathiti_detail_view'),
    
    # search
    path('all', login_required(AllView.as_view(),login_url=login), name='all_mathites'),
    path('search', login_required(SearchView.as_view(),login_url=login), name='search_mathites'),
    
    # edit
    path('<int:pk>/edit', login_required(MathitisEdit.as_view(),login_url=login), name='mathiti_update'),
    path('<int:pk>/edit/energos', login_required(EnergosEdit.as_view(),login_url=login), name='energos_update'),
    path('<int:pk>/edit/provlimata/<int:f_pk>', login_required(ProvlimataEdit.as_view(),login_url=login), name='provlimata_update'),
    path('<int:pk>/edit/adies/<int:f_pk>', login_required(AdiesEdit.as_view(),login_url=login), name='adies_update'),
    path('<int:pk>/edit/gonios/<int:f_pk>', login_required(GoniosEdit.as_view(),login_url=login), name='gonios_update'),
    path('<int:pk>/edit/paralavi/<int:f_pk>', login_required(ParalaviEdit.as_view(),login_url=login), name='paralavi_update'),
    path('<int:pk>/exetasi/edit/<int:f_pk>', login_required(ProgressEdit.as_view(),login_url=login), name='progress_update'),
    
    # groups
    path('groups', login_required(Groups.as_view(),login_url=login), name='groups'),
    path('groups/<int:pk>', login_required(GroupsEdit.as_view(),login_url=login), name='groups_update'),



    
    #add
    path('<int:pk>/add/gonios', login_required(GoniosAdd.as_view(),login_url=login), name='gonios_add'),
    path('<int:pk>/add/paralavi', login_required(ParalaviAdd.as_view(),login_url=login), name='paralavi_add'),
    
    # parousiologio
    path('parousiologio/group/<int:pk>', ParousiologioView, name='parousiologio'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
