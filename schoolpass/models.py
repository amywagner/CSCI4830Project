from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    student_first_name = models.CharField(max_length=15)
    student_last_name = models.CharField(max_length=15)
    student_id = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],
        unique=True,)
    student_password = models.CharField(max_length=25)
    accommodations = models.TextField(default='None')
    notes = models.TextField(default='No notes')
    number_of_passes = models.PositiveIntegerField(default=0)
    number_of_rejections = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.student_first_name + " " + self.student_last_name

    def get_id(self):
        return self.student_id

    def get_accommodations(self):
        return self.accommodations

    def get_notes(self):
        return self.notes

    def get_passes(self):
        return self.number_of_passes

    def get_rejections(self):
        return self.number_of_rejections


class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    teacher_first_name = models.CharField(max_length=15)
    teacher_last_name = models.CharField(max_length=15)
    teacher_id = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],
        unique=True,)
    departments = models.CharField(max_length=50)
    room_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    teacher_password = models.CharField(max_length=25)

    def __str__(self):
        return self.teacher_first_name + " " + self.teacher_last_name

    def get_departments(self):
        return self.departments

    def get_room_number(self):
        return self.room_number

class Pass(models.Model):
    id_pass = models.AutoField(primary_key=True)
    WATERFOUNTAIN = 'WF'
    RESTROOM = 'RR'
    NURSE = 'N'
    OFFICE = 'O'
    OTHERCLASSROOM = 'OC'
    PASS_CHOICES = (
        (WATERFOUNTAIN, 'Water Fountain'),
        (RESTROOM, 'Sophomore'),
        (NURSE, 'Nurse'),
        (OFFICE, 'Office'),
        (OTHERCLASSROOM, 'Other Classroom'),
    )
    kind_of_pass = models.CharField(max_length=15, choices=PASS_CHOICES, default=WATERFOUNTAIN)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
