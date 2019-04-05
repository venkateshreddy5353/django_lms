from django.urls import path
from .views import MembershipSelectView, PaymentView, updateTransactions

app_name = 'memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subsciption_id>/', updateTransactions, name='update-transactions' )
]