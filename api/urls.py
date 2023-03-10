from rest_framework.routers import DefaultRouter

from api import views


app_name = 'api'

router = DefaultRouter()
router.register(
    'users',
    views.UserViewSet,
    basename='users'
)
router.register(
    'things',
    views.ThingViewSet,
    basename='things'
)
router.register(
    'current-user',
    views.CurrentUserViewSet,
    basename='current-user'
)

urlpatterns = router.urls + [

]