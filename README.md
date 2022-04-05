# TO-DO-API
#Introduction
```
##Cài đặt:
1. Cơ sở dữ liệu:
   - Create database d
  
   Lấy CSDL [tại link này](https://drive.google.com/file/d/1h8eUZ-pnQnYBI94OZlnGaKzy9ZuDQgrH/view?usp=sharing)

2. Deploy source code to localhost:

   - Install libraries:
    - Django: 

- 2.1 Cài đặt app giảng viên ( Project: *AttendanceOnlineAdminSocket*)
  - Thêm project vào Android StudioFile
    - File =>New =>Import project... =>chọn đường dẫn file=>*chọn OK*
  - Tiến hành build project.

- 2.2 Cài đặt app sinh viên ( Project: *AttendanceOnline*)
  - Thêm project vào Android Studio
    - New => Import project... => chọn đường dẫn file =>*chọn OK*
  - Kết nối CSDL
    - Trên thanh công cụ chọn *Tools*=>*Firebase*=>*RealTime Database*=>*Save and retrieve*=>*Connection*=>*Chuyển đến trang Firebase*=>*Chọn CSDL Attendance Online ở phần 1*=>*Quay lại Android studio*=>*Chọn lại "Connection" bấm "Sync"*.
  - Tiến hành build project.   
  
###Thư viện sử dụng
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
