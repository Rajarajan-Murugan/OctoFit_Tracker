from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', username='IronMan', team=marvel, is_superhero=True),
            User(email='steve@rogers.com', username='CaptainAmerica', team=marvel, is_superhero=True),
            User(email='bruce@wayne.com', username='Batman', team=dc, is_superhero=True),
            User(email='clark@kent.com', username='Superman', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=timezone.now())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, date=timezone.now())

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        w2 = Workout.objects.create(name='Flight Training', description='Flight workout for superheroes')
        w1.suggested_for.set([users[0], users[2]])
        w2.suggested_for.set([users[1], users[3]])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
