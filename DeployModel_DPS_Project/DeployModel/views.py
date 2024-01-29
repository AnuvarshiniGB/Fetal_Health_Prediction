from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request,"home.html")

def result(request):

    cls = joblib.load('final_lr_model.sav')

    lis = [float(request.GET['baseline value']),
            float(request.GET['accelerations']),
            float(request.GET['fetal_movement']),
            float(request.GET['uterine_contractions']),
            float(request.GET['light_decelerations']),
            float(request.GET['severe_decelerations']),
            float(request.GET['prolongued_decelerations']),
            float(request.GET['abnormal_short_term_variability']),
            float(request.GET['mean_value_of_short_term_variability']),
            float(request.GET['percentage_of_time_with_abnormal_long_term_variability']),
            float(request.GET['mean_value_of_long_term_variability']),
            float(request.GET['histogram_width']),
            float(request.GET['histogram_min']),
            float(request.GET['histogram_max']),
            float(request.GET['histogram_number_of_peaks']),
            float(request.GET['histogram_number_of_zeroes']),
            float(request.GET['histogram_mode']),
            float(request.GET['histogram_mean']),
            float(request.GET['histogram_median']),
            float(request.GET['histogram_variance']),
            float(request.GET['histogram_tendency'])]

    ans = cls.predict([lis])

    return render(request,"result.html",{'ans':ans,'lis':lis})