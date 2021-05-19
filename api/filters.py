from django_filters import rest_framework as filters

from .models import Post


class PostFilter(filters.FilterSet):
    search = filters.NumberFilter(
        lookup_expr='exact', field_name='group')

    class Meta:
        model = Post
        fields = ['group']
