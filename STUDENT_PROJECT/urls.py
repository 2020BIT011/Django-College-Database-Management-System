from django.contrib import admin
from django.urls import include, re_path,path

from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static

from Student.views import view_record,view_Student_Data,view_Addmission_Data,StudentList,AdmissionList

from Teacher.views import teacherList

from Student.views import StudentListCreate,StudentListUpdate,StudentListDelete,MarksList,FeedbackList
#from django.conf.urls import url

#from django.urls import include, re_path
#from myapp.views import home


urlpatterns = [
  
    path('admin/', admin.site.urls),
    
    
    re_path(r'^record1/', view_record, name='link_record'),
    re_path(r'^student_data/', view_Student_Data, name='link_student_data'),
    re_path(r'^addmission_Data/', view_Addmission_Data, name='link_addmision_data'),
    
    path('student', StudentList.as_view(), name='student_list'),

    path('new', StudentListCreate.as_view(), name='Student_new'),
	path('edit/<int:pk>', StudentListUpdate.as_view(), name='Student_edit'),
  	path('delete/<int:pk>', StudentListDelete.as_view(), name='Student_delete'),

    path('admission', AdmissionList.as_view(), name='Admission_list'),
    path('', teacherList.as_view(), name='teacher_list'),
    path('Marks', MarksList.as_view(), name='Marks_list'),
    path('Feedback', FeedbackList.as_view(), name='Feedback_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



