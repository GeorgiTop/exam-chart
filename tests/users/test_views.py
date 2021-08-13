import random
from django.conf import settings
from tests.base.client_set_up import ChartTestCase
from chart.users.models import Profile
from django.urls import reverse


class UserCreateViewTest(ChartTestCase):
    def test_user_is_loged_in_after_creation(self):
        response = self.client.get(reverse('top20-home'))

        self.assertEqual(self.user.id, response.context['user'].id)


    # def test_has_success_message_after_log_in(self, cleaned_data):
    #     self.success_message = f'Welcome {self.object}! Your account has been created!'
    #     return self.success_message % cleaned_data
    #
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     login(self.request, self.object)
    #     return result