# Vehicle Advertising System

A project which a client can do two things :

1. Create an advertisement using email, description and Image. After detecting Image as Vehicle, User will know if ad got accepted or not by sending and Email to him/her. (POST METHOD)

2. User get ad state using the id of ad. (id generated when posting an ad) (GET METHOD)
   
   ---

In this project we learnt about how to work with cloud services such as :

1. Remote database services : [Aiven](https://aiven.io/), [MongoDB atlas](https://www.mongodb.com/cloud/atlas/lp/try4?utm_content=controldbaasterms&utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_core_prosp-brand_gic-null_emea-nl_ps-all_desktop_eng_lead&utm_term=mongodb%20dbaas&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624536&adgroup=115749708663)

2. Storing images at S3 Aws bucket

3. [RabbitMQ service](https://www.cloudamqp.com/)

4. Image classifier service: [Imagga](https://imagga.com/)

5. Email service : [Mailgun](https://www.mailgun.com/)

### System architecture

![](/Users/rojina/Desktop/CC1/pictures/system-arch.png)

### Database architecture

![](https://github.com/rojinakashefi/CloudComputing/blob/main/advertisment-manager/pictures/db-arch.png)

Used [Django rest framework](https://blog.logrocket.com/django-rest-framework-create-api/) as backend and postman for sending requests.

### System output

![](https://github.com/rojinakashefi/CloudComputing/blob/main/advertisment-manager/pictures/sys-out.png)
