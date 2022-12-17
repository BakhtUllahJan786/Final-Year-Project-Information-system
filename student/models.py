from django.db import models

# Create your models here.

class Batch(models.Model):
    batch=models.IntegerField(blank=True,null=True,unique=True)
    DateOfAdmission = models.DateField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.batch)

    
    class Meta:
        verbose_name_plural = 'Batch'
        
        
class Student(models.Model):
    SECTION_CHIOICES=(
    ('Morning','Morning'),
    ('Evening','Evening'),
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D')
)
    GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('TransGender','TransGender'),
)
    PROJECT_STATUS=(
        ('Started' , 'Started'),
        ('Not Started','Not Started'),
    )

    name=models.CharField(max_length=50)
    batch_no=models.ForeignKey(Batch,null=True,on_delete=models.CASCADE)
    section=models.CharField(max_length=50,choices=SECTION_CHIOICES)
    roll_number=models.IntegerField()
    projet_status=models.CharField(max_length=20,choices=PROJECT_STATUS,default='Started')
    gender=models.CharField(max_length=50,choices=GENDER,default='Male')
    dues=models.BooleanField(default=False)
    remarks=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

