# TO-DO-API
#Introduction
```
##Deploy source code to localhost:
1. 
   - Install libraries: Django, djangorestframework, PyJWT, django-cors-headers, datetime
     + pip install django
     + pip install djangorestframework
     + pip install django-cors-headers
     + pip install datetime
   - Start Project:
     + python manage.py runserver <port>
     + <port>: 8000
###Database:
   - Connect database:
      + Update database section in settings.py file with the following setting:
         DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME'    : 'mydata', 
              'USER'    : 'root',
              'PASSWORD': '',
              'HOST'    : 'localhost',
              'PORT'    : '3306',
                   }
               }
    - Create database: run in terminal
      + python manage.py makemigrations
      + python manage.py migration
      Database is used in testing: [link](https://drive.google.com/file/d/1h8eUZ-pnQnYBI94OZlnGaKzy9ZuDQgrH/view?usp=sharing)


Thư viện sử dụng
1. App giảng viên
```
    //Google Support
    implementation 'androidx.appcompat:appcompat:1.1.0'
    //Layout
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
    //xuất excel
    implementation files('libs/dom4j-1.6.1.jar')
    implementation files('libs/poi-3.9.jar')
    implementation files('libs/poi-ooxml-3.9.jar')
    implementation files('libs/xmlbeans-3.0.0.jar')
    //Listiew
    implementation 'androidx.recyclerview:recyclerview:1.1.0'
    //Layout Tạo độ bóng
    implementation 'androidx.cardview:cardview:1.0.0'
    //Chuyển sang file json
    implementation 'com.google.code.gson:gson:2.8.6'
```
2. App sinh viên:
```
    //Layout Tạo độ bóng
    implementation 'androidx.cardview:cardview:1.0.0' 
    //khung tròn cho image
    implementation 'de.hdodenhof:circleimageview:3.0.0' 
    //listview
    implementation 'androidx.recyclerview:recyclerview:1.1.0' 
    //xem hình ảnh
    implementation 'com.github.chrisbanes:PhotoView:2.3.0' 
    //Google Support
    implementation 'androidx.appcompat:appcompat:1.1.0'
    //library bottom navigation
    implementation 'com.google.android.material:material:1.3.0-alpha01'
    //Suport Gson
    implementation 'com.google.code.gson:gson:2.8.6'
    //sử dụng hình ảnh từ địa chỉ ảnh trên internet
    implementation 'com.github.bumptech.glide:glide:4.11.0' 
    // support for glide
    annotationProcessor 'com.github.bumptech.glide:compiler:4.11.0' 
    //Layout
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
    //CSDL firebase
    implementation 'com.google.firebase:firebase-database:19.3.1'
```
