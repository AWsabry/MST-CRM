from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Register_Login.models import Profile

# Create your models here.

quarter = [
    ('Q1', 'Q1'),
    ('Q2', 'Q2'),
    ('Q3', 'Q3'),
    ('Q4', 'Q4'),
]



class Industry(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Industry"

class Organizations(models.Model):
    organization_name = models.CharField(max_length=100,blank=True,null=True)
    organization_type = models.CharField(max_length=100,blank=True,null=True)
    contact_name = models.CharField(max_length=100,blank=True,null=True)
    contact_title = models.CharField(max_length=100,blank=True,null=True)
    contact_email = models.CharField(max_length=100,blank=True,null=True)
    contact_phone_number = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.organization_name)
    
    def save(self, *args, **kwargs):
        if self.organization_name == None or " ":
            self.organization_name == "Not Recorded"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Organizations"



class Projects(models.Model):
    sales_name = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null = True,)
    project_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    total_project_cost = models.PositiveIntegerField(blank=True,null=True)
    percentage_rate = models.IntegerField(default = 0, blank=True,null=True,validators=[MaxValueValidator(100), MinValueValidator(0)])
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE,blank=True,null = True,)
    organizations = models.ForeignKey(Organizations, on_delete=models.CASCADE,blank=True,null = True,)
    quarter_closed = models.CharField(max_length=20, choices=quarter, blank=True,null = True,)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.project_name)
    
    def save(self, *args, **kwargs):
        total_cost = 0
        total_all = Project_Services.objects.filter(project = self.id)
        for service in total_all:
            total_cost += service.single_service_cost
        self.total_project_cost = total_cost
        # print(total_all)
        print(total_cost)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Projects"


class Project_Services(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    service_percentage_rate = models.IntegerField(default = 0, blank=True,null=True,validators=[MaxValueValidator(100), MinValueValidator(0)])
    project = models.ForeignKey(Projects, on_delete=models.CASCADE,blank=True,null = True,)
    single_service_cost = models.PositiveIntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        total_cost = 0
        total_all = Projects.objects.filter(id = self.project.id)

        for service in total_all:
            total_cost += service.total_project_cost + self.single_service_cost # Need to be subtracted when deleted



        Projects.objects.filter(id = self.project.id).update(total_project_cost = total_cost)

        print(total_cost)
        print(total_all)
        
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Project Services"



class Documents(models.Model):
    file_name = models.CharField(max_length=100,blank=True,null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE,blank=True,null = True,)
    files = models.FileField(upload_to='uploads/',)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file_name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Documents"