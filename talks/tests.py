from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Talk
from .models import Track


class TrackModelTests(TestCase):

    def test_track_creation(self):
        track = Track.objects.create(
            title="Lunes",
            place="Salon 5"
        )
        self.assertIn("Lunes", track.title)
        self.assertIn("Salon 5", track.place)


class TalkModelTests(TestCase):

    def setUp(self):
        self.track = Track.objects.create(
            title="Martes",
            place="Salon 5"
        )

    def test_talk_creation(self):
        talk = Talk.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings.",
            track=self.track
        )
        now = timezone.now()
        self.assertLess(talk.created_at, now)
        self.assertIn(talk, self.track.talk_set.all())


class CourseViewsTests(TestCase):

    def setUp(self):
        self.track = Track.objects.create(
            title="Lunes",
            place="Salon 1"
        )
        self.track2 = Track.objects.create(
            title="Martes",
            place="Salon 2"
        )
        self.talk = Talk.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings.",
            track=self.track
        )

    def test_track_list_view(self):
        resp = self.client.get(reverse('tracks:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.track, resp.context['tracks'])
        self.assertIn(self.track2, resp.context['tracks'])
        self.assertTemplateUsed(resp, 'talks/track_list.html')
        self.assertContains(resp, self.track.title)

    def test_track_detail_view(self):
        resp = self.client.get(
            reverse('tracks:details', kwargs={'pk': self.track.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.track, resp.context['track'])

#     def test_step_detail(self):
#         resp = self.client.get(reverse('courses:step', kwargs={
#                     'course_pk': self.course.pk,
#                     'step_pk': self.step.pk}))
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(self.step, resp.context['step'])
