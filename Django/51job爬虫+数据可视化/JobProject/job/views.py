from django.core.cache import cache
from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from job.models import JobInfo


def home(request):
    """
    首页
    :param request:
    :return:
    """
    jobs = JobInfo.objects.all().order_by('id')
    job_name = request.GET.get('job_name', '')
    if job_name:
        jobs = jobs.filter(job_name__contains=job_name)
    city = request.GET.get('city', '')
    if city:
        jobs = jobs.filter(city__contains=city)
    salary = request.GET.get('salary', '')
    if salary:
        min_salary, max_salary = salary.split('-')
        jobs = jobs.filter(Q(min_salary__gte=int(min_salary)) & Q(max_salary__lte=int(max_salary)))
    education = request.GET.get('education', '')
    if education:
        jobs = jobs.filter(attribute_text__contains=education)
    companytype_text = request.GET.get('companytype_text', '')
    if companytype_text:
        jobs = jobs.filter(companytype_text__contains=companytype_text)
    companysize_text = request.GET.get('companysize_text', '')
    if companysize_text:
        jobs = jobs.filter(companysize_text__contains=companysize_text)

    working_years = request.GET.get('working_years', '')
    if working_years:
        jobs = jobs.filter(attribute_text__contains=working_years)

    return render(request, 'home.html',
                  context={
                      'jobs': jobs,
                      'job_name': job_name,
                      'city': city,
                      'salary': salary,
                      'education': education,
                      'companytype_text': companytype_text,
                      'working_years': working_years,
                      'companysize_text': companysize_text
                  })


def data_show(request):
    return render(request, 'job_echarts.html')


def json_data(request):
    """
    数据分析
    """
    # 热门行业的用人需求Top10
    top_companyind = JobInfo.objects.values_list('companyind_text').annotate(Count('companyind_text'))
    sort_top_companyind = sorted(list(top_companyind), key=lambda x: x[1], reverse=True)
    companyind_list, companyind_count_list = zip(*(sort_top_companyind[:10]))

    # 热门城市的岗位数量Top10
    top_city = JobInfo.objects.values_list('city').annotate(Count('city'))
    sort_top_city = sorted(list(top_city), key=lambda x: x[1], reverse=True)
    city_list, city_count_list = zip(*(sort_top_city[:10]))

    # 全国各省岗位数量
    province = JobInfo.objects.values_list('province').filter(province__isnull=False).annotate(Count('province'))
    province_list, province_list_val = zip(*list(province))
    province_data = []
    for name, val in province:
        province_data.append(
            {
                'name': name,
                'value': val
            }
        )

    # 一线城市占饼图
    city = ['北京', '上海', '杭州', '广州']
    city_val = [
        JobInfo.objects.filter(city__icontains='北京').count(),
        JobInfo.objects.filter(city__icontains='上海').count(),
        JobInfo.objects.filter(city__icontains='杭州').count(),
        JobInfo.objects.filter(city__icontains='广州').count(),
    ]
    city_pie = []
    for name, vale in zip(city, city_val):
        city_pie.append({
            'name': name,
            'value': vale
        })

    data = cache.get('data', '')
    if data:
        res = data
    else:
        data = {
            'top_companyind': [companyind_list, companyind_count_list],
            'top_city': [city_list, city_count_list],
            'province': [province_list, province_list_val],
            'city': city,
            'city_pie': city_pie,
            'province_data': province_data

        }
        cache.set('data', data, 60 * 60 * 12)
        res = data

    return JsonResponse(res)
