from django.db import models


class TaxUpdate(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='tax_updates/',
        blank=True,
        null=True
    )

    short_description = models.CharField(max_length=300)

    content = models.TextField()

    meta_title = models.CharField(
        max_length=200,
        blank=True
    )

    meta_description = models.TextField(
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ContactEnquiry(models.Model):

    SERVICE_CHOICES = (
        ('GST Filing', 'GST Filing'),
        ('Income Tax Filing', 'Income Tax Filing'),
        ('Accounting', 'Accounting'),
        ('TDS Filing', 'TDS Filing'),
        ('Business Registration', 'Business Registration'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Testimonial(models.Model):

    client_name = models.CharField(max_length=100)

    designation = models.CharField(
        max_length=100,
        blank=True
    )

    review = models.TextField()

    rating = models.PositiveSmallIntegerField(
        default=5
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ['-created_at']


class TeamMember(models.Model):

    name = models.CharField(max_length=100)

    designation = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='team/'
    )

    description = models.TextField(
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Feedback(models.Model):

    name = models.CharField(max_length=100)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']