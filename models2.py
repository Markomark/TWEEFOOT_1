# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Mix2(models.Model):
    index_u = models.BigIntegerField(blank=True, null=True)
    follow_request_sent_u = models.NullBooleanField()
    has_extended_profile_u = models.NullBooleanField()
    profile_use_background_image_u = models.NullBooleanField()
    idd_u = models.BigIntegerField(blank=True, null=True)
    default_profile_u = models.NullBooleanField()
    verified_u = models.NullBooleanField()
    profile_text_color_u = models.TextField(blank=True, null=True)
    profile_image_url_https_u = models.TextField(blank=True, null=True)
    profile_sidebar_fill_color_u = models.TextField(blank=True, null=True)
    is_translator_u = models.NullBooleanField()
    geo_enabled_u = models.NullBooleanField()
    followers_count_u = models.BigIntegerField(blank=True, null=True)
    profile_sidebar_border_color_u = models.TextField(blank=True, null=True)
    location_u = models.TextField(blank=True, null=True)
    default_profile_image_u = models.NullBooleanField()
    id_str_u = models.TextField(blank=True, null=True)
    is_translation_enabled_u = models.NullBooleanField()
    utc_offset_u = models.FloatField(blank=True, null=True)
    statuses_count_u = models.BigIntegerField(blank=True, null=True)
    description_u = models.TextField(blank=True, null=True)
    friends_count_u = models.BigIntegerField(blank=True, null=True)
    profile_link_color_u = models.TextField(blank=True, null=True)
    profile_image_url_u = models.TextField(blank=True, null=True)
    notifications_u = models.NullBooleanField()
    profile_background_image_url_https_u = models.TextField(blank=True, null=True)
    profile_background_color_u = models.TextField(blank=True, null=True)
    profile_background_image_url_u = models.TextField(blank=True, null=True)
    name_u = models.TextField(blank=True, null=True)
    lang_u = models.TextField(blank=True, null=True)
    profile_background_tile_u = models.NullBooleanField()
    favourites_count_u = models.BigIntegerField(blank=True, null=True)
    screen_name_u = models.TextField(blank=True, null=True)
    url_u = models.TextField(blank=True, null=True)
    created_at_u = models.TextField(blank=True, null=True)
    contributors_enabled_u = models.NullBooleanField()
    time_zone_u = models.TextField(blank=True, null=True)
    protected_u = models.NullBooleanField()
    translator_type_u = models.TextField(blank=True, null=True)
    following_u = models.NullBooleanField()
    listed_count_u = models.BigIntegerField(blank=True, null=True)
    profile_banner_url_u = models.TextField(blank=True, null=True)
    id_u = models.BigIntegerField(blank=True, null=True)
    index = models.FloatField(blank=True, null=True)
    unnamed_0 = models.TextField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contributors = models.TextField(blank=True, null=True)
    truncated = models.NullBooleanField()
    text = models.TextField(blank=True, null=True)
    is_quote_status = models.TextField(blank=True, null=True)
    in_reply_to_status_id = models.TextField(blank=True, null=True)
    idd = models.FloatField(blank=True, null=True)
    favorite_count = models.FloatField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    retweeted = models.TextField(blank=True, null=True)
    in_reply_to_screen_name = models.TextField(blank=True, null=True)
    in_reply_to_user_id = models.TextField(blank=True, null=True)
    retweet_count = models.FloatField(blank=True, null=True)
    id_str = models.TextField(blank=True, null=True)
    favorited = models.TextField(blank=True, null=True)
    in_reply_to_user_id_str = models.FloatField(blank=True, null=True)
    lang = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    in_reply_to_status_id_str = models.FloatField(blank=True, null=True)
    id_twit = models.TextField(blank=True, null=True)
    media_url = models.TextField(blank=True, null=True)
    id = models.FloatField(blank=True, null=True)
    col = models.DateTimeField(blank=True, null=True)
    country_league = models.TextField(db_column='Country_league', blank=True, null=True)  # Field name made lowercase.
    league_field = models.TextField(db_column='League ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    club = models.TextField(blank=True, null=True)
    t_id = models.BigIntegerField(blank=True, null=True)
    last_tw = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mix2'


class Ref(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    follow_request_sent = models.NullBooleanField()
    has_extended_profile = models.NullBooleanField()
    profile_use_background_image = models.NullBooleanField()
    idd = models.BigIntegerField(blank=True, null=True)
    default_profile = models.NullBooleanField()
    verified = models.NullBooleanField()
    profile_text_color = models.TextField(blank=True, null=True)
    profile_image_url_https = models.TextField(blank=True, null=True)
    profile_sidebar_fill_color = models.TextField(blank=True, null=True)
    is_translator = models.NullBooleanField()
    geo_enabled = models.NullBooleanField()
    followers_count = models.BigIntegerField(blank=True, null=True)
    profile_sidebar_border_color = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    default_profile_image = models.NullBooleanField()
    id_str = models.TextField(blank=True, null=True)
    is_translation_enabled = models.NullBooleanField()
    utc_offset = models.FloatField(blank=True, null=True)
    statuses_count = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    friends_count = models.BigIntegerField(blank=True, null=True)
    profile_link_color = models.TextField(blank=True, null=True)
    profile_image_url = models.TextField(blank=True, null=True)
    notifications = models.NullBooleanField()
    profile_background_image_url_https = models.TextField(blank=True, null=True)
    profile_background_color = models.TextField(blank=True, null=True)
    profile_background_image_url = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    lang = models.TextField(blank=True, null=True)
    profile_background_tile = models.NullBooleanField()
    favourites_count = models.BigIntegerField(blank=True, null=True)
    screen_name = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    contributors_enabled = models.NullBooleanField()
    time_zone = models.TextField(blank=True, null=True)
    protected = models.NullBooleanField()
    translator_type = models.TextField(blank=True, null=True)
    following = models.NullBooleanField()
    listed_count = models.BigIntegerField(blank=True, null=True)
    profile_banner_url = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    country_league = models.TextField(db_column='Country_league', blank=True, null=True)  # Field name made lowercase.
    league_field = models.TextField(db_column='League ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    club = models.TextField(blank=True, null=True)
    t_id = models.BigIntegerField(blank=True, null=True)
    last_tw = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REF'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
