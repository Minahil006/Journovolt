# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdmInterfaceTb1MasterDomain(models.Model):
    id = models.BigAutoField(primary_key=True)
    domain_name = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'adm_interface_tb1_master_domain'


class AdmInterfaceTb2UrlDetailsTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_url = models.CharField(max_length=100)
    url_string = models.CharField(max_length=200)
    domain = models.ForeignKey(AdmInterfaceTb1MasterDomain, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adm_interface_tb2_url_details_table'


class Article(models.Model):
    url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    article_url = models.CharField(unique=True, max_length=767)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleImgConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_img_configuration'


class ArticlePublishDateConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_publish_date_configuration'


class ArticleTextConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_text_configuration'


class ArticleTopicHeadlineConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    parent_tag_name = models.CharField(max_length=20)
    child_tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_topic_headline_configuration'


class ArticleUrlConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_url_configuration'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class DomainUrl(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING)
    url = models.CharField(max_length=600)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'domain_url'


class ProcesssedScrapeData(models.Model):
    id = models.IntegerField()
    article_id = models.IntegerField()
    processed_news_topic = models.TextField()
    processed_news_description = models.TextField()
    image_href = models.CharField(max_length=767)
    scrape_date_stamp = models.CharField(max_length=20)
    scrape_time_stamp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'processsed_scrape_data'


class UnprocesssedScrapeData(models.Model):
    article = models.OneToOneField(Article, models.DO_NOTHING)
    unprocessed_news_topic = models.TextField()
    unprocessed_news_description = models.TextField()
    publication_date = models.CharField(max_length=767)
    image_href = models.CharField(max_length=767)
    scrape_date_stamp = models.CharField(max_length=20)
    scrape_time_stamp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'unprocesssed_scrape_data'


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
