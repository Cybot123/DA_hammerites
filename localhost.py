#First HTTP Server
import socket;
#Define the host as a tuple
HOST, PORT = "", 8080;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1);
s.bind((HOST,PORT));
s.listen(True);

print("Serving HTTP on port %s...." %PORT);

while True:
    client_connection, client_address = s.accept();
    request = client_connection.recv(1024); #Buffer Size
    print(request.decode("utf-8")); #Display the HTTP request
    #Define the Web response message
    http_reponse = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<html>
<body style="background-color:powderblue;">
<head>
<title>The hammerites webpage</title>
</head>

<body>
<div style="text-align:center">
  <br />
  Alvin
</div>
<img src="https://scontent.fsin2-1.fna.fbcdn.net/v/t31.0-8/13909211_1508765882482969_6609958311137836869_o.jpg?_nc_cat=105&ccb=2&_nc_sid=174925&_nc_ohc=lkhyelQbnt4AX8IiTqr&_nc_ht=scontent.fsin2-1.fna&oh=81e1c487b4f589ecd8093fb12e8b14e0&oe=604386F6" width="400" height="400" alt="hammerite">
<div style="text-align:center">
  <br />
  Hairul
</div>
<img src="https://lh3.googleusercontent.com/mc65-PSwZtZwbtf2l4Ou1XePzLVQeli6I3f8rRyRi0nArW7sTbnnJNFMkU0ujLXbT8Q0h9686njSdJ2HzaZwKMxWICSNmfkWGqLMwD3iFHR8Hq-tlMpDmtZ65RCkzR7GHJ52bFGcrQchD4_kYUutb9tb0Ue0-ieVWsjviLBwl-9FLB-xZXgF42ihoxOR0fQ6wGwRN3My4uHukyZqI-uNxUnM4DT7pWWSbgEBbcFK4Zr2fUShAp1Iw8qNJH36dnvhdDQORmrVCQ7G_8DHuheXN5nXUYm_ugRh4ylqOfSjy_sdoqMB3cLk8DLZ6I84gGUAg0JT21rYU3VtXGJy5w8lcYeEYVmJaNYFlSvGhGfJOFQrn7j23YM4sxoYMX1JKb7NnKhJU1mqwG-Mfh7zmiQwLFvYC2YvrhYHXZSyxZo_CmpoNLtRlLwElJfmxEb8NrKOMharPvxYXSM8jVlv1d7Sg5Nu4T_CyivGXqt6YPrvxANulRu1RF-3Bpmxk5HScZvYgzMQNkmQ2EreTSd3vSM55ftJe6qeANbjRUt51zWSpGoUysz1ziQXxyYb5e8Ai3Qo9jSUlcv8WRqZ0O0nSC7_mPKLeaILeuupd_xpOOAkTYofzfcxPn9lBqv1nlcARirs4mG1gpcjrP-RhXtdMHaR5gNrYTHzKZwzeO3p-F-oodLAeNKmaRmNAsgsrOVVt4I=w694-h927-no?authuser=0"width="400" height="400" alt="hairul">
<div style="text-align:center">
  <br />
  Afif
</div>
<img src="https://media.discordapp.net/attachments/696996342165143604/807511004560490527/image0.jpg?width=507&height=676" alt="afif picture">
<div style="text-align:center">
  <br />
 The hammerites and Mr Hoh
</div>
<img src=https://raw.githubusercontent.com/Cybot123/DA_hammerites/master/Hammerites%20photo.jpeg?token=AQCWM5TS3223QPQFQFJ3KK3AGSY26
</body>
</html>
"""
    client_connection.sendall(bytes(http_reponse, "utf-8"));
    client_connection.close();

