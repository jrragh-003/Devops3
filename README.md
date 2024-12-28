In order to pull the image : 
``` docker pull urmsandeep/ai-artistic-style-service``` 

In order to run : 
``` docker run -d -p 5001:5001 urmsandeep/ai-artistic-style-service ```

API Testing : 
```curl -X POST http://127.0.0.1:5001/styleTransfer -F "image=@test.jpg" --output styled_image.jpg ```

Docker Images : 

![Screenshot from 2024-12-28 14-39-50](https://github.com/user-attachments/assets/fee3330d-061d-4a96-9dc4-f40997e0248c)




Grafana Readings
![Screenshot from 2024-12-28 14-19-26](https://github.com/user-attachments/assets/468e4b28-96ee-4b01-86ca-7708c604b7e1)


Prometheus Readings
![Screenshot from 2024-12-28 14-22-00](https://github.com/user-attachments/assets/3342af21-ad10-472d-ad38-4d21bcfd3faf)


Jenkins Final Output

![Screenshot from 2024-12-28 14-24-10](https://github.com/user-attachments/assets/d17f5cc9-0e32-4bd8-b09d-c5d1462d362e)
