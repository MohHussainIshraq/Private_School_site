from django.db import models

class Welcome_header(models.Model):
    special_name = models.CharField(max_length=30)
    welcome_message = models.CharField(max_length=50)
    education_center_name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="header_image")


    def __str__(self):
        return self.special_name


class About(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to="about_image")

    def __str__(self):
        return self.title


class Info_Teachers(models.Model):
    title = models.CharField(max_length=40)
    info = models.TextField()

    def __str__(self):
        return self.title

class Teachers(models.Model):
    image = models.ImageField(upload_to="teachers_image")
    name_of_teacher = models.CharField(max_length=35)

    def __str__(self):
        return self.name_of_teacher


class Vehicles_Facility(models.Model):
    title_name_of_vehicles = models.CharField(max_length=38)
    description = models.TextField()


    def __str__(self):
        return self.description[:10]


class Kind_of_vehicles(models.Model):
    image = models.ImageField(upload_to="vehicles_image")


class Student(models.Model):
    student_title = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.description[:10]


class Info_Student(models.Model):
    image = models.ImageField(upload_to="student_info_image")
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    description = models.TextField()


    def __str__(self):
        return self.name
    

class Contact(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()


    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name


class Footer(models.Model):
    copy_right = models.CharField(max_length=100)
    tag_message = models.CharField(max_length=100)


    def __str__(self):
        return self.copy_right