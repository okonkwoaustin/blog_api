from rest_framework import routers
from . views import BlogViewset, UserViewset

router = routers.SimpleRouter()

router.register("blogs", BlogViewset, basename="blogs"),
router.register("users", UserViewset, basename="users"),

urlpatterns = router.urls