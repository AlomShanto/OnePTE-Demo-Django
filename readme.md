<h3>OnePTE Demo</h3>
<p>Author: Md. Shuhayel Alom Shanto</p>
Contact: alomshuhayel.cse@gmail.com
<br><br><h3>Installing Guidelines</h3>
1. Download the project from <a href = "https://github.com/AlomShanto/OnePTE-Demo-Django">OnePTE Demo.</a><br>
2. make a virtual environment of python.<br>
3. Activate the virtual environment<br>
4. install all the dependencies from requrements.txt file.<br>
5. Now run the command from terminal "py manage.py runserver" for windows and "python3 manage.py runserver" for Linux.<br>



<h3>Urls for testing by postman (or similar platforms): </h3>
<p>Example: localhost:8000/new-test/</p><br>


<h5>Summarize Spoken Text (SST)</h5>
1. new-test/<br>
    for creating a new test. <br>
2. test/details/<br>
    for getting all test details.<br>
3. test/update/pk/<br>
    for updating the questions or answers. here "pk" in link means primary key of the object. replace it by primary key.<br>
4. test/delete/pk/<br>
    for deleting SST question data from database. here "pk" in link means primary key of the object. replace it by primary key.<br>

<h5>Reordering the Questions (RO)</h5>
1. new-ro-test/<br>
for creating a new test. <br>
2. test/all-ro/<br>
    for getting all test details.<br>
3. test/update-ro/pk/<br>
    for updating the questions or answers. here "pk" in link means primary key of the object. replace it by primary key.<br>
4. test/delete-ro/pk/<br>
    for deleting RO question data from database. here "pk" in link means primary key of the object. replace it by primary key.<br>

<h5>Reading Multiple Choice (RMMCQ)</h5>
1. new-rmmcq-test/<br>
for creating a new test. <br>
2. test/all_rmmcq/<br>
    for getting all test details.<br>
3. test/update-rmmcq/pk/<br>
    for updating the questions or answers. here "pk" in link means primary key of the object. replace it by primary key.<br>
4. test/delete-rmmcq/pk/<br>
    for deleting RMMCQ question data from database. here "pk" in link means primary key of the object. replace it by primary key.<br>

<h5>Practice History with and without filter</h5>
<h6>Without Filter: </h6>
--> history/user_id/<br>
here user_id refers to the primary key of the user. Replace it by user id. <br>

<h6>With Filter: </h6>
--> history/user_id/?exam_type=sst<br>
here user_id refers to the primary key of the user. Replace it by user id. And for different type of exams, just replace the sst with the type you want to see. <br>

<h5>Create new Submissions</h5>
--> create-new-submission/<br>
Use this link to createa new submission of any type of exam. <br><br><br>

All the api's use form data input and respond as json format. <br>