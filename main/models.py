from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم الطالب')
    homework = models.PositiveSmallIntegerField(
        verbose_name='درجة الواجبات المسلمة', validators=[MaxValueValidator(10)])
    homework_link = models.CharField(max_length=1000, verbose_name='رابط الواجبات المدرسية للطالب', blank=True)
    contribution = models.PositiveSmallIntegerField(
        verbose_name='درجة المشاركة الفعالة', validators=[MaxValueValidator(10)])
    summer = models.PositiveSmallIntegerField(
        verbose_name='درجة الأنشطة الصيفية', validators=[MaxValueValidator(10)])
    reserach = models.PositiveSmallIntegerField(
        verbose_name='درجة البحوث', validators=[MaxValueValidator(15)])
    research_link = models.CharField(max_length=1000, verbose_name='رابط البحوث للطالب', blank=True)
    attendance = models.PositiveSmallIntegerField(
        verbose_name='درجة الحضور', validators=[MaxValueValidator(5)])
    paper_test = models.PositiveSmallIntegerField(
        verbose_name='درجة الاختبار النظري', validators=[MaxValueValidator(10)])
    practical_test = models.PositiveSmallIntegerField(
        verbose_name='درجة الاختبار العملي', validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.name

    def performance(self):
        total = self.paper_test + self.practical_test + self.attendance + \
            self.reserach + self.summer + self.homework + self.contribution
        if total >= 50:
            return total, 'ممتاز'
        elif total >= 40:
            return total, 'جيد جدًا'
        elif total >= 30:
            return total, 'جيد'
        elif total >= 20:
            return total, 'مقبول'
        else:
            return total, 'ضعيف'
