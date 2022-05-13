from django.db import models


# Create your models here.


class JobInfo(models.Model):
    coid = models.CharField('工作ID', max_length=64, db_index=True)
    company_name = models.CharField('公司名', max_length=264, null=True, blank=True)
    job_name = models.CharField('岗位名字', max_length=264, null=True, blank=True)
    workarea_text = models.CharField('工作地址', max_length=264, null=True, blank=True)
    providesalary_text = models.CharField('薪资', max_length=264, null=True, blank=True)
    issuedate = models.CharField('发布时间', max_length=264, null=True, blank=True)
    companytype_text = models.CharField('公司类型', max_length=264, null=True, blank=True)
    companysize_text = models.CharField('员工人数', max_length=264, null=True, blank=True)
    companyind_text = models.CharField('所属行业', max_length=264, null=True, blank=True)
    job_href = models.CharField('岗位连接', max_length=264, null=True, blank=True)
    jobwelf = models.CharField('公司福利', max_length=264, null=True, blank=True)
    attribute_text = models.CharField('岗位要求', max_length=264, null=True, blank=True)

    min_salary = models.FloatField('最低薪资', null=True, blank=True)
    max_salary = models.FloatField('最高薪资', null=True, blank=True)
    mean_salary = models.FloatField('平均薪资', null=True, blank=True)
    city = models.CharField('城市', max_length=128, null=True, blank=True)
    province = models.CharField('省份', max_length=128, null=True, blank=True)
    education = models.CharField('学历', max_length=128, null=True, blank=True)
