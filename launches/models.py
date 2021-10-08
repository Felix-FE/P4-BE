from django.db import models

class Launch(models.Model):
  launch_name = models.CharField(max_length = 500)
  date_time = models.CharField(max_length = 500)
  current_stage = models.CharField(max_length = 500)
  launch_status = models.CharField(max_length = 1000)
  launch_provider = models.CharField(max_length = 500)
  rocket_config = models.CharField(max_length = 500)
  payload_name = models.CharField(max_length = 500)
  payload_mission = models.CharField(max_length = 2000)
  location = models.CharField(max_length = 500)
  followed_by = models.ManyToManyField( 
    'jwt_auth.User',
    related_name= 'following',
    blank=True
  )

  def __str__(self):
    return f'{self.launch_name}'


class Update(models.Model):
  update = models.CharField(max_length= 500)
  source = models.CharField(max_length= 500)
  created_at = models.DateTimeField(auto_now=True)
  launch = models.ForeignKey(
    Launch,
    related_name='updates',
    on_delete=models.CASCADE )
  owner = models.ForeignKey(
    'jwt_auth.User',
    related_name='updates_posted',
    on_delete=models.CASCADE
  )
  reliable = models.ManyToManyField(
    'jwt_auth.User',
    related_name='verified_reliable_by',
    blank=True,
  )
  unreliable = models.ManyToManyField(
    'jwt_auth.User',
    related_name='verified_unreliable_by',
    blank=True,
  )
  official = models.ManyToManyField(
    'jwt_auth.User',
    related_name='verified_official_by',
    blank=True,
  )
  false = models.ManyToManyField(
    'jwt_auth.User',
    related_name='verified_false_by',
    blank=True,
  )
  launch_status = models.BooleanField(blank=True, null=True)
  time_change = models.BooleanField(blank=True, null=True)
  general_announcements = models.BooleanField(blank=True, null=True)

  def __str__(self):  
    return f'{self.update}'


