from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("timetable/", views.timetable, name="timetable"),
    path("timetable/", views.timetable, name="timetable"),
    path("student/", views.student_home, name="student_home"),
    path("teacher/", views.teacher_home, name="teacher_home"),
    path("", views.LoginView.as_view(), name="login"),
    path("signup/student/", views.StudentSignUpView.as_view(), name="student-signup"),
    path("signup/teacher/", views.TeacherSignUpView.as_view(), name="teacher-signup"),
    path("signup/adminis/", views.AdminisSignUpView.as_view(), name="adminis-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("teacher/question/create/", views.create_question, name="create-question"),
    path("teacher/lesson/create/", views.create_lesson, name="create-lesson"),
    path("question/<int:question_id>/answer/", views.create_answer, name="create-answer"),
    path("lesson/<int:lesson_id>/comment/", views.create_comment, name="create-comment"),
    path("question/<int:question_id>/", views.student_question_detail, name="student-question-detail"),
    path("lesson/<int:lesson_id>/", views.student_lesson_detail, name="student-lesson-detail"),
    path("teacher/lesson/<int:lesson_id>/", views.teacher_lesson_detail, name="teacher-lesson-detail"),
    path("teacher/question/<int:lesson_id>/", views.teacher_question_detail, name="teacher-question-detail"),
    path('listetudiant', views.listetudiant, name="listetudiant"),
    path('listprofesseur', views.listprofesseur, name="listprofesseur"),
    path('listmodul', views.listmodul, name="listmodul"),
    path('listclasse', views.listclasse, name="listclasse"),
    path('listfiliere', views.listfiliere, name="listfiliere"),
]