import django_filters

from .models import Follow


class FollowFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        lookup_expr='iexact', field_name='user__username')

    class Meta:
        model = Follow
        fields = ['user']
