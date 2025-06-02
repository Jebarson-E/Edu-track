from django.db import models # type: ignore

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student_name = models.CharField(max_length=100)  # Store student name directly
    date = models.DateField()
    present = models.BooleanField()

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student_name} – {self.date} ({status})"

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Attendance"



class Mark(models.Model):
    student_name = models.CharField(max_length=100)  # Store student name directly
    subject = models.CharField(max_length=100)
    mark = models.FloatField()

    def __str__(self):
        return f"{self.student_name} – {self.subject}: {self.mark}"

    class Meta:
        ordering = ['student_name', 'subject']


class Behavior(models.Model):
    student_name = models.CharField(max_length=100)  # Store student name directly
    date = models.DateField()
    note = models.TextField()

    def __str__(self):
        return f"{self.student_name} – {self.date}: {self.note[:30]}..."

    class Meta:
        ordering = ['-date']
